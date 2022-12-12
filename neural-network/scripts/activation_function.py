import tensorflow.keras.backend as K


def custom_sigmoid(x):
    return 1.99 * K.sigmoid(37 * x) - 1
