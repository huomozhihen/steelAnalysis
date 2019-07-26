"""
Time： 2019-7-19
Description： 差分自回归移动平均模型
            AutoRegressive Integrated Moving Average
"""

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data_process.steel_demand_data import steel_demand_data_initial
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def draw_ts(ts):
    # 绘制时间序列图
    # 输入：
    #       ts：时间序列，series
    f = plt.figure(facecolor='white')
    ts.plot(color='blue')
    plt.show()


def draw_trend(ts, size):
    # 绘制移动平均图、加权移动平均图。
    # 输入：
    #       ts：时间序列，series
    #       size：窗口大小
    f = plt.figure(facecolor='white')
    rol_mean = ts.rolling(window=size).mean()
    rol_weighted_mean = pd.ewma(ts, span=size)

    ts.plot(color='blue', label='Original')
    rol_mean.plot(color='red', label='Rolling Mean')
    rol_weighted_mean.plot(color='black', label='Weighted Rolling Mean')
    plt.legend(loc='best')
    plt.title('Rolling Mean')
    plt.show()


def draw_acf_pacf(ts, lags=20):
    # 绘制自相关和偏相关图
    # 输入
    #       ts：时间序列，series
    #       lags：阶数
    f = plt.figure(facecolor='white')
    ax1 = f.add_subplot(211)
    plot_acf(ts, lags=lags, ax=ax1)
    ax2 = f.add_subplot(212)
    plot_pacf(ts, lags=lags, ax=ax2)
    plt.show()


def adf_test(ts):
    adf_res = adfuller(ts)
    # adf稳定性检验
    # 输入
    #       ts：时间序列，series
    # 输出
    #       output：检验结果，series
    adf_output = pd.Series(adf_res[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in adf_res[4].items():
        adf_output['Critical Value (%s)' % key] = value
    return adf_output


def ARIMA_model(p, d, q):
    SteelDemand = steel_demand_data_initial.SteelDemand()
    steel_df = SteelDemand.steel_demand_year_on_year_data()
    steel_series = steel_df[steel_df.columns[0]]

    fore_result = []
    for i in range(-12, 0, 1):
        train = steel_series[:i]
        model = ARIMA(train, order=(p, d, q))
        arima = model.fit()  # 训练
        # pred = arima.predict(start='2006-1', end='2018-5')  # 预测
        fore = arima.forecast()[0]
        fore_result.append(fore[0])
    ground_truth = steel_series[-12:]
    predict_mse = mean_squared_error(fore_result, ground_truth)
    # print(predict_mse)
    return predict_mse
