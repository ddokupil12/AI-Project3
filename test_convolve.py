import models
from torch import tensor, sum, zeros, randn

a = randn(4, 5)
b = randn(2, 2)

print(models.Convolve(a, b))


def Convolve(input: tensor, weight: tensor):
    input_tensor_dimensions = input.shape
    weight_dimensions = weight.shape
    Output_Tensor = tensor(())
    print('output...')
    inputHeight, inputWidth = input_tensor_dimensions
    weightHeight, weightWidth = weight_dimensions
    outputHeight = (inputHeight - weightHeight)
    outputWidth = (inputWidth - weightWidth)

    Output_Tensor = zeros(outputHeight, outputWidth)

    for i in range(outputHeight):
        for k in range(outputWidth):
            window = input[i:i + weightHeight, k:k + weightWidth]
            Output_Tensor[i, k] = sum(window * weight)


    print(Output_Tensor.shape)
    print(Output_Tensor)
    return Output_Tensor