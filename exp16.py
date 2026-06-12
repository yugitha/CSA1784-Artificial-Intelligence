import math

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input from user
x1 = float(input("Enter Input 1: "))
x2 = float(input("Enter Input 2: "))

# Weights from Input Layer to Hidden Layer
w1 = 0.2
w2 = 0.4
w3 = 0.3
w4 = 0.5

# Hidden Layer Calculations
h1 = sigmoid(x1 * w1 + x2 * w2)
h2 = sigmoid(x1 * w3 + x2 * w4)

# Weights from Hidden Layer to Output Layer
w5 = 0.6
w6 = 0.7

# Output Layer Calculation
output = sigmoid(h1 * w5 + h2 * w6)

print("Output of Feed Forward Neural Network =", output)
