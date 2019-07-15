"""
Time： 2019-7-12
Description： SVM回归
"""

from model.com_mod import model_method
from sklearn import svm


def svm_regression():
    train_attr, train_label, test_attr, test_label = model_method.load_data()

    model = svm.SVR()
    model.fit(train_attr, train_label)

    model_method.result_analysis(train_attr, train_label, test_attr, test_label, model)


if __name__ == '__main__':
    svm_regression()
