def custom_sigmoid(x, a=1.99, b=37, c=-1):
    return a / (1 + np.exp(-b * x)) + c
