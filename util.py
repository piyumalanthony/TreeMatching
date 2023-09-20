import numpy as np


def rmse(arr1, arr2):
    arr_1 = np.array(arr1)
    arr_2 = np.array(arr2)
    err = arr_1 - arr_2
    err_sqr = np.power(err, 2)
    err_sqr_mean = np.sum(err_sqr) / np.shape(err_sqr)[0]
    return np.sqrt(err_sqr_mean)
