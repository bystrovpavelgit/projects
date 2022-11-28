""" Apache License 2.0 Copyright (c) 2022 Pavel Bystrov
    test LogisticRegression
"""
from sklearn import datasets
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import RidgeClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_iris_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


def get_logistic_cv():
    cv = LogisticRegressionCV(solver='lbfgs', n_jobs=1, random_state=1, cv=4)
    return cv


def get_ridge_cv():
    cv = RidgeClassifierCV(cv=4)
    return cv


def compare_accuracy():
    X, y = load_iris_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    log_cv = get_logistic_cv()
    log_cv.fit(X_train, y_train)
    ridge_cv = get_ridge_cv()
    ridge_cv.fit(X_train, y_train)
    return accuracy_score(y_test, log_cv.predict(X_test)), accuracy_score(y_test, ridge_cv.predict(X_test))


print("Logistic Regression vs Ridge Clsf accuracy", compare_accuracy())
