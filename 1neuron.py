# Моделируем ситуацию для одного нейрона
inputs = [4.5, 2.3, 4.2, 1.7]
weights = [1.5, 6.2, 3.9, 2.4]
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
print(output)