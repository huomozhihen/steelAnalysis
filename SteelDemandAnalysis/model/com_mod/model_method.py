"""
Time： 2019-7-112
Description： 一些通用方法
"""

from config import path_config
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

config = path_config.GlobalConfig()


def load_data():
    # 加载训练与验证数据
    # 返回：
    #       train_attr:训练集属性
    #       train_label:训练集标签
    #       test_attr:测试集属性
    #       test_label:测试集标签
    train_data_file = open(config.train_data)
    test_data_file = open(config.test_data)

    train_data_df = pd.read_csv(train_data_file, header=0, index_col=0)
    train_data = train_data_df.values
    train_attr = train_data[:, :-1]
    train_label = train_data[:, -1]
    test_data_df = pd.read_csv(test_data_file, header=0, index_col=0)
    test_data = test_data_df.values
    test_attr = test_data[:, :-1]
    test_label = test_data[:, -1]

    return train_attr, train_label, test_attr, test_label


def result_analysis(train_attr, train_label, test_attr, test_label, model):
    # 结果展示
    # 输入：
    #       train_attr:训练集属性
    #       train_label:训练集标签
    #       test_attr:测试集属性
    #       test_label:测试集标签
    #       model:模型
    test_predict = model.predict(test_attr)
    train_predict = model.predict(train_attr)

    test_mae = mean_absolute_error(test_label, test_predict)
    test_mse = mean_squared_error(test_label, test_predict)
    train_mae = mean_absolute_error(train_label, train_predict)
    train_mse = mean_squared_error(train_label, train_predict)
    print('训练集均方误差：' + str(train_mse))
    print('训练集平均绝对误差：' + str(train_mae))
    print('测试集均方误差：'+str(test_mse))
    print('测试集平均绝对误差：' + str(test_mae))

    ground_truth = np.hstack((train_label, test_label))
    predict = np.hstack((train_predict, test_predict))
    plt.figure(figsize=(22, 10), dpi=60)
    plt.plot(ground_truth, 'o--', color="blue")
    plt.plot(predict, 'o--', color='red')
    plt.axvline(x=len(train_label) - 0.5)
    plt.show()


if __name__ == '__main__':
    pass
