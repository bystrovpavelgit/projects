""" Apache License 2.0 Copyright (c) 2022 Pavel Bystrov
    test PCA
"""
import numpy as np
from sklearn.decomposition import PCA
from sklearn import datasets


def load_mnist_data():
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    return X, y


def min_cumsum_index(arr):
    cum_sum = np.cumsum(arr)
    zeros_indexes = np.where(cum_sum[:] > .9)[0]
    if not zeros_indexes.size:
        return None, None
    return np.min(zeros_indexes)


def test_pca():
    X, y = load_mnist_data()
    pca = PCA().fit(X)
    idx = min_cumsum_index(pca.explained_variance_ratio_)
    cum_sum = np.cumsum(pca.explained_variance_ratio_)
    print("var ratio for main components ", cum_sum[0:idx+1])
    print('principle components number to explain 90% =', idx+1,' ratio =', cum_sum[idx])


test_pca()

