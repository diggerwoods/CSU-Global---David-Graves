import numpy as np

# **Activation Function (Sigmoid) and its Derivative**
def sigmoid(x):
    x = np.clip(x, -500, 500)  # Prevent overflow
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# **Loss Function (Mean Squared Error)**
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# **Training Data**
X = np.array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7],
              [2,4,6], [3,6,9], [4,8,12], [5,10,15], [6,12,18],
              [1,3,5], [2,5,8], [3,7,11], [10,20,30], [5,15,25]])
y = np.array([[4], [5], [6], [7], [8], 
              [8], [12], [16], [20], [24],
              [7], [11], [15], [40], [35]])

# **Normalize Data**
X_mean, X_std = X.mean(axis=0), X.std(axis=0)
y_mean, y_std = y.mean(), y.std()
X_std = np.where(X_std == 0, 1, X_std)  # Prevent division by zero
y_std = 1 if y_std == 0 else y_std
X_norm = (X - X_mean) / X_std
y_norm = (y - y_mean) / y_std

# **Network Parameters**
input_neurons = X.shape[1]
hidden_neurons = 8
output_neurons = 1

# **Weight and Bias Initialization**
np.random.seed(42)
weights_input_hidden = np.random.rand(input_neurons, hidden_neurons) * 0.1
bias_hidden = np.zeros((1, hidden_neurons))
weights_hidden_output = np.random.rand(hidden_neurons, output_neurons) * 0.1
bias_output = np.zeros((1, output_neurons))

# **Training Parameters**
learning_rate = 0.01
epochs = 1000

# **Training Loop**
try:
    for epoch in range(epochs):
        # **1. Feedforward**
        hidden_layer_input = np.dot(X_norm, weights_input_hidden) + bias_hidden
        hidden_layer_input = np.clip(hidden_layer_input, -10, 10)
        hidden_layer_output = sigmoid(hidden_layer_input)
        
        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
        predicted_output = output_layer_input
        
        # **2. Calculate Error**
        error_output = y_norm - predicted_output
        loss = mean_squared_error(y_norm, predicted_output)
        
        if np.isnan(loss) or np.isinf(loss):
            print(f"Training stopped at epoch {epoch} due to numerical instability")
            break
        
        # **3. Backpropagation**
        gradient_output = -2 * error_output / len(y_norm)
        
        error_hidden = np.dot(gradient_output, weights_hidden_output.T)
        gradient_hidden = error_hidden * sigmoid_derivative(hidden_layer_input)
        
        # **4. Update Weights and Biases**
        weights_hidden_output -= np.dot(hidden_layer_output.T, gradient_output) * learning_rate
        bias_output -= np.sum(gradient_output, axis=0, keepdims=True) * learning_rate
        
        weights_input_hidden -= np.dot(X_norm.T, gradient_hidden) * learning_rate
        bias_hidden -= np.sum(gradient_hidden, axis=0, keepdims=True) * learning_rate
        
        # **5. Print Loss Every 200 Epochs**
        if epoch % 200 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.6f}")
except Exception as e:
    print(f"Training error: {e}")

# **Prediction Function**
def predict_next(sequence):
    if len(sequence) != 3:
        print(f"Error: Please provide exactly 3 numbers. You provided {len(sequence)}.")
        return None
    
    try:
        test_input = np.array([sequence])
        test_input_norm = (test_input - X_mean) / X_std
        hidden_layer_input = np.dot(test_input_norm, weights_input_hidden) + bias_hidden
        hidden_layer_input = np.clip(hidden_layer_input, -10, 10)
        hidden_layer_output = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
        prediction_norm = output_layer_input[0][0]
        result = prediction_norm * y_std + y_mean
        
        if np.isnan(result) or np.isinf(result):
            return 0.0
        return result
    except Exception as e:
        print(f"Prediction error: {e}")
        return None

# **Interactive Testing**
print("\n=== Improved Sequence Predictor Ready ===")
print("Training completed. You can now predict the next number in a sequence.")
print("Examples: [1,2,3] -> 4, [2,4,6] -> 8, [5,10,15] -> 20")

while True:
    try:
        user_input = input("\nEnter 3 numbers separated by commas (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        sequence = [float(x.strip()) for x in user_input.split(',')]
        prediction = predict_next(sequence)
        
        if prediction is not None:
            print(f"Input sequence: {sequence}")
            print(f"Predicted next number: {prediction:.2f}")
            
    except ValueError:
        print("Invalid input. Please enter 3 numbers separated by commas.")
    except KeyboardInterrupt:
        break

print("\nGoodbye!")