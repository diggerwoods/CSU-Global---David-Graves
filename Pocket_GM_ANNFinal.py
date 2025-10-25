# Python 3
# Dependencies:
# pip install pandas scikit-learn numpy joblib

import os
import argparse
import joblib
import time
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

# --- Config (relative defaults) ---
DEFAULT_CSV = os.path.join(BASE_DIR, "data", "2015-2025 basic MLB batting stats.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.joblib")
REGRESSOR_PATH = os.path.join(MODEL_DIR, "regressor.joblib")
CLASSIFIER_PATH = os.path.join(MODEL_DIR, "classifier.joblib")

NUMERIC_COLS = [
    'batting_avg', 'on_base_percent', 'slg_percent', 'ab', 'pa', 'hit', 'single', 'double', 'triple', 'home_run',
    'strikeout', 'walk', 'k_percent', 'bb_percent', 'woba', 'xwoba', 'sweet_spot_percent', 'barrel_batted_rate', 'hard_hit_percent'
]
INT_COLS = {'ab', 'pa', 'hit', 'single', 'double', 'triple', 'home_run', 'strikeout', 'walk'}
STAT_PROMPTS = {
    'batting_avg': "Batting average (.xxx): ",
    'on_base_percent': "On-base percentage (.xxx): ",
    'slg_percent': "Slugging percent (.xxx): ",
    'ab': "At bats (whole number): ",
    'pa': "Plate appearances (whole number): ",
    'hit': "Hits (whole number): ",
    'single': "Singles (whole number): ",
    'double': "Doubles (whole number): ",
    'triple': "Triples (whole number): ",
    'home_run': "Home runs (whole number): ",
    'strikeout': "Strikeouts (whole number): ",
    'walk': "Walks (whole number): ",
    'k_percent': "Strikeout percent (xx.x): ",
    'bb_percent': "Walk percent (xx.x): ",
    'woba': "Weighted on-base average (.xxx): ",
    'xwoba': "Expected weighted on-base average (.xxx): ",
    'sweet_spot_percent': "Sweet spot percent (xx.x): ",
    'barrel_batted_rate': "Barrel batted rate (xx.x): ",
    'hard_hit_percent': "Hard hit percent (xx.x): "
}
TIER_NAMES = {5: "All Pro", 4: "All Star", 3: "Great", 2: "Good", 1: "Farm Player"}

def print_time(msg, start):
    print(f"{msg} ({time.time() - start:.2f} seconds)")

def fill_missing(data):
    for col in data.columns:
        if data[col].dtype == 'O':
            data[col] = data[col].fillna('')
        else:
            data[col] = data[col].fillna(data[col].mean())
    return data

def prepare_shifted_data(data, numeric_cols):
    data = data.sort_values(['player_name', 'year'])
    future_stats = data.groupby('player_name')[numeric_cols].shift(-1)
    future_stats.columns = [f'next_{col}' for col in numeric_cols]
    data_with_targets = pd.concat([data, future_stats], axis=1)
    data_with_targets = data_with_targets.dropna(subset=[f'next_{col}' for col in numeric_cols])
    return data_with_targets

def assign_tier_row(row):
    slg = row.get('slg_percent', 0.0)
    if slg >= 0.550:
        return 5
    elif slg >= 0.500:
        return 4
    elif slg >= 0.450:
        return 3
    elif slg >= 0.400:
        return 2
    else:
        return 1

def predict_player_stats(player_stats, scaler, model, numeric_cols):
    numeric_stats = np.array([player_stats.get(col, 0.0) for col in numeric_cols])
    numeric_scaled = scaler.transform([numeric_stats])
    predictions = model.predict(numeric_scaled)[0]
    return dict(zip(numeric_cols, predictions))

def predict_player_tier(player_stats, scaler, clf, numeric_cols):
    numeric_stats = np.array([player_stats.get(col, 0.0) for col in numeric_cols])
    numeric_scaled = scaler.transform([numeric_stats])
    tier = clf.predict(numeric_scaled)[0]
    return tier

def find_most_similar_players(predicted_stats, data, numeric_cols, top_n=3):
    if data is None:
        return None, None
    pred_vec = np.array([predicted_stats[col] for col in numeric_cols])
    player_matrix = data[numeric_cols].values
    distances = np.linalg.norm(player_matrix - pred_vec, axis=1)
    closest_indices = np.argsort(distances)[:top_n]
    return data.iloc[closest_indices], distances[closest_indices]

def ensure_columns_exist(df, cols):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns in CSV: {missing}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pocket GM predictor")
    parser.add_argument("--data", "-d", default=DEFAULT_CSV,
                        help="Path to CSV file with historical data (default: ./data/2015-2025 basic MLB batting stats.csv)")
    parser.add_argument("--force-train", "-f", action="store_true",
                        help="Force retraining even if saved models exist (optional)")
    args = parser.parse_args()

    csv_path = args.data
    os.makedirs(MODEL_DIR, exist_ok=True)

    start_time = time.time()
    print(f"Loading historical player data from: {csv_path}")
    data = None

    # If model artifacts exist and we're not forcing retrain, load them and attempt to load CSV for similarity only
    models_exist = os.path.exists(SCALER_PATH) and os.path.exists(REGRESSOR_PATH) and os.path.exists(CLASSIFIER_PATH)
    if models_exist and not args.force_train:
        print("Found saved models; loading models (skipping retraining)...")
        scaler = joblib.load(SCALER_PATH)
        model = joblib.load(REGRESSOR_PATH)
        clf = joblib.load(CLASSIFIER_PATH)
        # load CSV for similarity lookup if present
        if os.path.exists(csv_path):
            data = pd.read_csv(csv_path)
            data = data.rename(columns={'last_name, first_name': 'player_name'}) if 'last_name, first_name' in data.columns else data
            try:
                ensure_columns_exist(data, ['player_name', 'year'])
                data = fill_missing(data)
                data = prepare_shifted_data(data, NUMERIC_COLS)
                print_time("Models and data loaded.", start_time)
            except Exception as e:
                print(f"Warning: CSV present but failed preparation: {e}")
                data = None
        else:
            print("CSV not found; similarity lookup will be disabled.")
    else:
        # Training path (CSV required)
        if not os.path.exists(csv_path):
            raise FileNotFoundError(
                f"CSV file not found at: {csv_path}\nPlace the CSV at that path or run with --data \"path/to/your.csv\""
            )
        data = pd.read_csv(csv_path)
        print_time("Data loaded.", start_time)

        # rename and basic checks
        if 'player_name' not in data.columns and 'last_name, first_name' in data.columns:
            data = data.rename(columns={'last_name, first_name': 'player_name'})
        ensure_columns_exist(data, ['player_name', 'year'])

        print("Filling missing values...")
        data = fill_missing(data)
        print_time("Missing values filled.", start_time)

        print("Preparing shifted data for next-season prediction...")
        data = prepare_shifted_data(data, NUMERIC_COLS)
        print_time("Shifted data prepared.", start_time)

        print("Assigning tiers to historical data...")
        data['tier'] = data.apply(assign_tier_row, axis=1)
        print_time("Tiers assigned.", start_time)

        print("Scaling numeric features...")
        X = data[NUMERIC_COLS].values
        y = data[[f'next_{col}' for col in NUMERIC_COLS]].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        print_time("Numeric features scaled.", start_time)

        print("Splitting data and training neural network model...")
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        mlp = MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=3000, random_state=42)
        model = MultiOutputRegressor(mlp)
        model.fit(X_train, y_train)
        print_time("Neural network model trained.", start_time)

        print("Training tier classifier...")
        tier_y = data['tier'].values
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_scaled, tier_y)
        print_time("Tier classifier trained.", start_time)

        # save artifacts
        try:
            joblib.dump(scaler, SCALER_PATH)
            joblib.dump(model, REGRESSOR_PATH)
            joblib.dump(clf, CLASSIFIER_PATH)
            print(f"Saved scaler/model/classifier to {MODEL_DIR}")
        except Exception as e:
            print(f"Warning: failed to save model artifacts: {e}")

    # --- User Input & Prediction ---
    while True:
        print("\nEnter new player information (or type 'q' to quit):")
        player_name = input("Player name (Last, First): ")
        if player_name.strip().lower() == 'q':
            print("Exiting program.")
            break

        player_stats = {}
        for col in NUMERIC_COLS:
            prompt = STAT_PROMPTS.get(col, f"{col}: ")
            val = input(prompt)
            if val.strip().lower() == 'q':
                print("Exiting program.")
                exit()
            try:
                if col in INT_COLS:
                    player_stats[col] = int(float(val))
                    if player_stats[col] < 0:
                        print(f"{col} cannot be negative. Setting to 0.")
                        player_stats[col] = 0
                else:
                    player_stats[col] = float(val)
            except ValueError:
                player_stats[col] = 0.0

        predicted_stats = predict_player_stats(player_stats, scaler, model, NUMERIC_COLS)
        print("\nPredicted Next-Season Stats:")
        for stat, value in predicted_stats.items():
            print(f"{stat}: {value:.3f}")

        tier = predict_player_tier(player_stats, scaler, clf, NUMERIC_COLS)
        print(f"\nPredicted Tier: {tier} ({TIER_NAMES[tier]})")
        print("Tier scale: 5 = Highest (All Pro), 4 = All Star, 3 = Great, 2 = Good, 1 = Lowest (Farm Player)")

        similar_players, sim_distances = find_most_similar_players(predicted_stats, data, NUMERIC_COLS, top_n=3)
        if similar_players is None:
            print("\nSimilarity lookup disabled (no dataset loaded).")
        else:
            print("\nMost Statistically Similar Players (from last season):")
            for idx, (i, row) in enumerate(similar_players.iterrows()):
                print(f"{idx+1}. {row['player_name']} (distance: {sim_distances[idx]:.3f})")
                for stat in NUMERIC_COLS:
                    print(f"   {stat}: {row[stat]:.3f}")