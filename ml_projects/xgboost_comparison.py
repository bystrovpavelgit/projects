""" Apache License 2.0 Copyright (c) 2019 Pavel Bystrov
    compare accuracy for XGBClassifier and LGBMClassifier
"""
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor
from sklearn.datasets import load_iris
import numpy as np


def get_xgboost_grid():
    clsf = XGBClassifier(random_state=17, n_estimators=64)
    params = {'learning_rate': np.linspace(0.005, 0.1, 20),
              'num_leaves': [2, 3, 7, 15, 31],
              'max_depth': [32,64,99]}
    cv = GridSearchCV(clsf, params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def get_lgbm_grid():
    clsf = LGBMClassifier(seed = 17, n_estimators=64)
    params = {'learning_rate': np.linspace(0.005, 0.1, 20),
              'num_leaves': [2, 3, 7, 15],
              'max_depth': [32,64,-1]}
    cv = GridSearchCV(clsf, params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def compare_accuracy():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)
    grid1 = get_xgboost_grid()
    grid1.fit(X_train, y_train)
    grid2 = get_lgbm_grid()
    grid2.fit(X_train, y_train)
    print("xgboost", grid1.best_params_)
    print("lgb", grid2.best_params_)
    print("F1 score:", f1_score(y_test, grid1.predict(X_test), average='macro'),
          f1_score(y_test, grid2.predict(X_test), average='macro'))
    return accuracy_score(y_test, grid1.predict(X_test)), accuracy_score(y_test, grid2.predict(X_test))


print("Accuracy", compare_accuracy())
