import models
import torch

a = torch.randn(4, 5)
b = torch.randn(2, 2)

print(models.Convolve(a, b))