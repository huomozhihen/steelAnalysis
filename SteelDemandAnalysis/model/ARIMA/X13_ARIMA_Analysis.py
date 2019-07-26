import pandas as pd
from pandas import Timestamp, datetime
from data_process.steel_demand_data import steel_demand_data_initial
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

PATH = r'E:\htsc\WinX13\x13as'  # 美国普查局x13as工具
os.chdir(PATH)


def analysis_entry():
    steel_demand = steel_demand_data_initial.SteelDemand()
    steel_df = steel_demand.steel_demand_cumulative_data()
    steel_series = steel_df[steel_df.columns[0]]
    steel_series.index = pd.to_datetime(steel_series.index)
    steel_series.name = 'TimeSeries'
    res_list = []
    for period in range(-60, 0, 1):
        time_series = steel_series[:period]
        res = X13_ARIMA_predict(time_series, 1)
        res_list.append(res[0])
    for i in res_list:
        print(i)
    X13_ARIMA_predict(steel_series, 12)


def X13_ARIMA_predict(time_series, predict_periods):
    # 采用X13_ARIMA的时序分析方式进行预测
    # 输入：
    #       data_series：时序数据series
    #       predict_periods：预测期数int
    # 返回：
    #       res：预测值list
    analysis_res = sm.tsa.x13_arima_analysis(time_series, forecast_years=predict_periods, log=True)
    analysis_results = analysis_res.results
    # analysis_res.plot()
    # plt.show()
    intern_info = analysis_results[analysis_results.find(
        'Date   Forecast      Error\n   ------------------------------'):analysis_results.find(
        '   ------------------------------\n\n  Confidence intervals')]
    split_info = intern_info.split()
    res = []
    for i in range(predict_periods):
        res.append(np.exp(float(split_info[5 + 3 * i])))
    return res


if __name__ == '__main__':
    analysis_entry()
