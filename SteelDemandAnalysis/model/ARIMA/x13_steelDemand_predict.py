import pandas as pd
import numpy as np
import os
from SteelDemandAnalysis.data_process.steel_demand_data import steel_demand_data_initial
from SteelDemandAnalysis.model.ARIMA import x13_arima


def analysis_entry():
    steel_demand = steel_demand_data_initial.SteelDemand()
    steel_df = steel_demand.steel_demand_data()
    steel_series = steel_df[steel_df.columns[0]]
    # steel_series.index = pd.to_datetime(steel_series.index)
    steel_series.index = pd.DatetimeIndex(start='2006-01-01', periods=161, freq='M')
    steel_series.name = 'TimeSeries'
    return steel_series


def read_df():
    f = open('E:\\htsc\\行业景气度\\数据\\模型数据\\converted_model_data.dat')
    data_df = pd.read_csv(f, header=0, index_col=0)
    return data_df


def fun():
    model = x13_arima.X13Arima('E:\\htsc\\行业景气度\\X13_ARIMA\\WinX13\\x13as\\x13as.exe')
    data_series = analysis_entry()[12:]
    user_params = read_df()
    user_params.index = data_series.index
    data_series.name = 'a'
    res = []
    for period in range(-60, 0, 1):
        time_series = data_series[:period]
        exog_df = user_params[:period + 1] if period != -1 else user_params
        exog_df.name = 'b'
        exog_df.columns = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6',
                           'b7', 'b8', 'b9', 'b10', 'b11', 'b12']
        model.x13_arima_analysis(time_series, exog=exog_df, forecast_periods=1)
        y_pre = model.x13_forecast()
        res.append(y_pre[0])
    for i, k in enumerate(res):
        print(k)


if __name__ == '__main__':
    fun()
