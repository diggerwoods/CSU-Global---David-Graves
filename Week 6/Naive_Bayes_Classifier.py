# Naive Bayes Classifier Example using scikit-learn

from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example binary features:
# [has_fur, lays_eggs, can_fly]
X = [
    [1, 0, 0],  # Cat
    [1, 0, 0],  # Dog
    [1, 0, 0],  # Rabbit
    [1, 0, 0],  # Cat
    [1, 0, 0],  # Dog
    [1, 0, 0],  # Rabbit
    [0, 1, 1],  # Bird
    [0, 1, 0],  # Snake
    [1, 0, 1],  # Bat
    [0, 1, 0],  # Turtle
]
# Labels: 0 = Cat, 1 = Dog, 2 = Rabbit, 3 = Bird, 4 = Snake, 5 = Bat, 6 = Turtle
y = [0, 1, 2, 0, 1, 2, 3, 4, 5, 6]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create and train the classifier
clf = BernoulliNB()
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Print results
print("Test set predictions:", y_pred)
print("Actual labels:      ", y_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Example prediction
sample = [[1, 0, 0]]  # Example: has fur, does not lay eggs, cannot fly
animal_names = {0: "Cat", 1: "Dog", 2: "Rabbit", 3: "Bird", 4: "Snake", 5: "Bat", 6: "Turtle"}
pred = clf.predict(sample)
print(f"Predicted class for {sample[0]}: {animal_names[pred[0]]}")

# Example prediction with user input in a loop
print("\nClassify new animals! Type 'q' at any prompt to quit.")
while True:
    try:
        has_fur = input("Has fur? (1 for Yes, 0 for No, q to quit): ")
        if has_fur.lower() == 'q':
            break
        if has_fur not in ('0', '1'):
            print("Please enter 1, 0, or q.\n")
            continue

        lays_eggs = input("Lays eggs? (1 for Yes, 0 for No, q to quit): ")
        if lays_eggs.lower() == 'q':
            break
        if lays_eggs not in ('0', '1'):
            print("Please enter 1, 0, or q.\n")
            continue

        can_fly = input("Can fly? (1 for Yes, 0 for No, q to quit): ")
        if can_fly.lower() == 'q':
            break
        if can_fly not in ('0', '1'):
            print("Please enter 1, 0, or q.\n")
            continue

        user_sample = [[int(has_fur), int(lays_eggs), int(can_fly)]]
        user_pred = clf.predict(user_sample)
        print(f"Predicted class for {user_sample[0]}: {animal_names[user_pred[0]]}\n")
    except Exception:
        print("Invalid input. Please enter 1 or 0 for each feature, or 'q' to quit.\n")