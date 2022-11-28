""" Apache License 2.0 Copyright (c) 2019 Pavel Bystrov
    compare accuracy for Decision Tree and Nearest Neighbors Classifier
"""
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def load_iris_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


def get_tree_grid():
    tree = DecisionTreeClassifier()
    tree_params = {'max_depth': range(1,25)}
    cv = GridSearchCV(tree, tree_params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def get_knn_grid():
    knn = KNeighborsClassifier()
    knn_params = {'n_neighbors': range(1,15)}
    cv = GridSearchCV(knn, knn_params, cv = 4, n_jobs=-1, verbose=0)
    return cv


def compare_tree_knn():
    X, y = load_iris_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)
    tree_grid = get_tree_grid()
    tree_grid.fit(X_train, y_train)
    print("tree ",tree_grid.best_params_)
    knn_grid = get_knn_grid()
    knn_grid.fit(X_train, y_train)
    print("knn ",knn_grid.best_params_)
    return accuracy_score(y_test, tree_grid.predict(X_test)), accuracy_score(y_test, knn_grid.predict(X_test))


print("Decision Tree vs kNN", compare_tree_knn())
