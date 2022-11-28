""" Apache License 2.0 Copyright (c) 2019 Pavel Bystrov
    compare accuracy for BaggingClassifier and RandomForestClassifierr
"""
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier


def load_iris_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


def get_rf_grid():
    rf = RandomForestClassifier(random_state=1)
    params = {'n_estimators': range(5,90)}
    cv = GridSearchCV(rf, params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def get_bagging_grid():
    bagging = BaggingClassifier(DecisionTreeClassifier())
    params = {'n_estimators': range(5,90)}
    cv = GridSearchCV(bagging, params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def compare_forest_and_bagging():
    X, y = load_iris_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)
    rf_grid = get_rf_grid()
    rf_grid.fit(X_train, y_train)
    print(rf_grid.best_params_)
    bag_grid = get_bagging_grid()
    bag_grid.fit(X_train, y_train)
    print(bag_grid.best_params_)
    return accuracy_score(y_test, rf_grid.predict(X_test)), accuracy_score(y_test, bag_grid.predict(X_test))


print(compare_forest_and_bagging())

