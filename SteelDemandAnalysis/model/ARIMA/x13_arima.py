# -*- coding: utf-8 -*-
"""
Created on Mon July  29 10:00:00 2019

@author:
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.tools.tools import Bunch


class X13Arima:
    """
    美国普查局x12a/x13as分析结果python解析
    windows
    数据：至少三年的月度数据或季度数据，带有时间标签
    """

    def __init__(self, tool_path='WinX13/x13as/x13as.exe'):
        self.tool_path = tool_path  # 美国普查局x13as工具路径，默认放在工作目录下

    def initial_tool_path(self, path):
        """
        设置x12a/x13as工具路径, 指向x12a.exe/x13as.exe
        """
        self.tool_path = path

    def x13_arima_analysis(self, ts, maxorder=(2, 1), maxdiff=(2, 1), diff=None,
                           exog=None, log=False, outlier=True, trading=False, forecast_periods=None):
        """
        调用statsmodels中的X13接口，获取工具分析结果

        Paramaters
        ----------
        ts : pandas.Series
            至少三年完整的时间序列，必须包含pandas.DatetimeIndex或pandas.PeriodIndex。
        maxorder : tuple
            regular与seasonal最大多项式阶数，其中regular取值范围(0，4]，seasonal取值范围[1，2]。
        maxdiff : tuple
            regular与seasonal最大差分阶数，其中regular取值范围[1，2]，seasonal取值为1。
            可将maxdiff设为None，此时必须设置diff。
        diff : tuple
            默认为None。当maxdiff为None时，可设置diff。regular取值范围[0，2]，seasonal取值范围[0，1]。
        exog : pandas.Series 或者 pandas.DataFrame
            自定义的外部变量，一般用于设置移动假日效应。
            必须包含原始数据时间（即ts所包含的时期）与预测时间（即forecase_periods所指的具体时期）的全部数据。
        log : bool
            对series取log，默认置False。
        outier : bool
            是否检测处理离群点，默认为True。
        trading ：bool
            是否检测处理交易日影响，默认为False。
        forecase_periods : int
            预测期，置为None时默认12。
        """
        self.ts = ts
        self.trading = trading
        self.forecast_periods = 12 if forecast_periods == None else forecast_periods

        self.analysis_res = sm.tsa.x13_arima_analysis(endog=ts, maxorder=maxorder, maxdiff=maxdiff, diff=diff,
                                                      exog=exog, log=log, outlier=outlier, trading=trading,
                                                      forecast_years=forecast_periods, x12path=self.tool_path)

    def x13_seasonal_decompose(self):
        """
        获取分析结果中调整后的数据、趋势循环数据、不规则数据、季节调整数据及日历调整数据。

        Returns
        ----------
        res : Bunch
            一个包含以下元素的Bunch对象:

            - seasadj: pandas.Series
            季节分解后最终因素调整完后的数据（即原始数据去除季节调整因素与日历调整因素）
            - trend: pandas.Series
            季节分解后最终的趋势-循环部分
            - irregular: pandas.Series
            季节分解后最终的不规则部分
            - seasonal: pandas.Series
            最终的季节调整因素（离群点调整与移动假日效应等调整已在先验调整中处理，包含在季节调整因素中）
            - calendar: pandas.Series 或 None
            若trading为True，calendar为最终的日历调整因素（主要是交易日调整）；若trading为False，则为None。
        """

        seasadj, trend, irregular = self.analysis_res.seasadj, self.analysis_res.trend, self.analysis_res.irregular
        seasonal = self._seasonal_resolution()
        calendar = self._calendar_resolution()

        res = Bunch(seasadj=seasadj, trend=trend, irregular=irregular, seasonal=seasonal, calendar=calendar)

        return res

    def x13_forecast(self):
        """
        获取分析结果中的预测值

        Returns
        ----------
        res : list
            沿时间线forecast_periods个预测结果
        """
        res = []
        if self.forecast_periods <= 0:
            return res
        else:
            res_str = self.analysis_res.results
            intern_info = res_str[res_str.find('Date   Forecast      Error'):res_str.find('Confidence intervals')]
            split_info = intern_info.split()
            for i in range(self.forecast_periods):
                res.append(float(split_info[5 + 3 * i]))
            return res

    def _seasonal_resolution(self):
        if self.trading:
            res_str = self.analysis_res.results
            chosen_info = res_str[res_str.find(' D 10  Final seasonal factors'):res_str.find(
                ' D 10.A  Final seasonal component forecasts')]
            return self._format_decoder1(chosen_info)
        else:
            return self.ts - self.analysis_res.seasadj

    def _calendar_resolution(self):
        if self.trading:
            res_str = self.analysis_res.results
            chosen_info = res_str[res_str.find(' D 18  Combined calendar adjustment factors'):res_str.find(
                ' D 18.A  Combined calendar adjustment component forecasts')]
            return self._format_decoder1(chosen_info)
        else:
            return None

    def _format_decoder1(self, chosen_info):
        selected_info = chosen_info[chosen_info.find('AVGE  \n ---') + 10:chosen_info.find('\n \n  AVGE')]
        line_split = selected_info.split("\n")
        data = []
        if 'monthly' in self.analysis_res.results:
            for i in range(len(line_split) // 3):
                space_split1 = line_split[3 * i + 1].split()[1:]
                space_split2 = line_split[3 * i + 2].split()[:-1]
                data = data + space_split1 + space_split2
        else:
            for i in range(len(line_split) // 2):
                space_split = line_split[2 * i + 1].split()[1:-1]
                data = data + space_split
        data = list(map(float, data))
        data_series = pd.Series(data, index=self.ts.index)
        return data_series


if __name__ == '__main__':
    import random
    import numpy as np
    num1 = 48
    ts = pd.Series(np.array([random.uniform(1,200) for k in range(num1)]))
    ts.index = pd.DatetimeIndex(start='2006-01', periods=num1, freq='M')
    ts.name = 'a'
    num2 = 49
    user_params = pd.DataFrame(np.array([[random.uniform(1,200) for k in range(2)] for j in range(num2)]))
    user_params.index = pd.DatetimeIndex(start='2006-01', periods=num2, freq='M')
    user_params.name = 'b'
    user_params.columns = ['b1','b2']
    model = X13Arima('E:/htsc/WinX13/x13as/x13as.exe')
    model.x13_arima_analysis(ts, exog=user_params, forecast_periods=1)
    forecast_res = model.x13_forecast()
    print(forecast_res)
