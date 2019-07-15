"""
Time: 2019-7-11
Description: 数据集划分
"""

from config import path_config
import pandas as pd

config = path_config.GlobalConfig


def divide_data(initial_data):
    # 划分训练集与测试集
    # 输入：
    #       initial_data：全部数据dataFrame
    train_data = initial_data[0:-12]
    test_data = initial_data[-12:]
    train_data.to_csv(config.train_data, sep=',', header=True, index=True)
    test_data.to_csv(config.test_data, sep=',', header=True, index=True)
    return


if __name__ == '__main__':
    # f = open(config.converted_model_data)
    f = open(config.initial_model_data)
    all_data_df = pd.read_csv(f, header=0, index_col=0)
    divide_data(all_data_df)
