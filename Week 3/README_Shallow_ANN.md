# Shallow Artificial Neural Network (ANN)

A 3-layer neural network implementation for sequence prediction using backpropagation.

## Features

- **3-Layer Architecture**: Input (3) → Hidden (8) → Output (1)
- **Sigmoid Activation**: Applied to hidden layer
- **Backpropagation**: Full gradient descent implementation
- **Data Normalization**: Prevents numerical overflow
- **Interactive Interface**: Real-time sequence prediction

## Requirements

```bash
pip install numpy
```

## Usage

```bash
python Shallow_ANN.py
```

Enter 3 numbers separated by commas to predict the next number in the sequence.

## Examples

- `1,2,3` → predicts `4` (arithmetic sequence)
- `2,4,6` → predicts `8` (even numbers)
- `5,10,15` → predicts `20` (multiples of 5)

## Architecture

- **Input Layer**: 3 neurons (normalized sequence values)
- **Hidden Layer**: 8 neurons with sigmoid activation
- **Output Layer**: 1 neuron (linear activation)
- **Training**: 1000 epochs with learning rate 0.01

## Training Data

15 diverse sequences including arithmetic, geometric, and mixed patterns for robust learning.

## Exit

Type `quit` to exit the program.