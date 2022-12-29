import tensorflow.keras.backend as K


def custom_sigmoid(x):
    return 2 * K.sigmoid(37 * x) - 1
