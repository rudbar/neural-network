# Моделируем ситуацию для 3 нейронов (целый слой)
inputs = [4.5, 2.3, 4.2, 1.7]

weights1 = [1.5, 6.2, 3.9, 2.4]
weights2 = [1.6, -0.2, 1.75, -0.55]
weights3 = [0.6, -0.23, 0.34, 0.32]

bias1 = 3
bias2 = 4
bias3 = 0.7

output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1, 
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
print(output)