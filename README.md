# [DEPRECATED] AI-Project 3

# Security warnings
This code uses NumPy version 1 and Torch version 2.2. There are many security vulnerabilities with torch<=2.6, but this can't be easily maintained to use the latest versions of Torch and Numpy. Among the vulnerabilities are remote code execution. Use this code at your own risk.

# Installation guide

1. Clone the repository

2. Install required dependencies

```bash
pip install -r requirements.txt
```

3. Test PyTorch, which requires NumPy (which was giving me issues)

```python
>>> import torch
>>>
```

4. Run the autograder (use `python3` if `python` doesn't work)

```bash
$ python autograder.py
```
