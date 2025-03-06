"""
Created: 2025.03.05
Modified: 2025.03.05

Single layer for loop
"""
inputs: list[float] = [1, 2, 3, 2.5]
weights: list[list[float]] = [[0.2, 0.8, -0.5, 1.0],
                        [0.5, -0.91, 0.26, -0.5],
                        [-0.26, -0.27, 0.17, 0.87]]
biases: list[float] = [2, 3, 0.5]   

# Output for current layer
layer_outputs: list[float] = []

# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    # Zeroed output of given neuron
    neuron_output: float = 0
    for n_input, n_weight in zip(inputs, neuron_weights):
        neuron_output += n_input * n_weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)





