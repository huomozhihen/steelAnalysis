"""
Time: 2019-7-10
Description: 属性相关性分析
"""

from data_process.estate_data import estate_data_initial
from data_process.homeAppAndCar_data import homeAppAndCar_data_initial
from data_process.infrastructure_data import infrastructure_data_initial
from data_process.machinery_data import machinery_data_initial
from data_process.macro_data import macro_data_initial
from data_process.manufacturing_data import manufacturing_data_initial
from data_process.steel_demand_data import steel_demand_data_initial
from data_process.util import correlation_analysis
from config import global_config
import pandas as pd
import numpy as np

MAX_PERIOD = 12


def initial_label_data():
    # 读取属性集数据
    # 返回：
    #       label_array: 标签数据array
    return steel_demand_data_initial.steel_demand_year_on_year_data()


def initial_attr_data():
    # 读取属性集数据
    # 返回：
    #       feature_df: 属性集数据dataFrame
    estate_year_on_year_data = estate_data_initial.estate_year_on_year_data()
    estate_cumulative_year_on_year_data = estate_data_initial.estate_cumulative_year_on_year_data().loc[
                                          12:].reset_index(
        drop=True)

    homeAppAndCar_cumulative_year_on_year_data = homeAppAndCar_data_initial.homeAppAndCar_cumulative_year_on_year_data()[
                                                 12:].reset_index(drop=True)

    infrastructure_cumulative_year_on_year_data = infrastructure_data_initial.infrastructure_cumulative_year_on_year_data()[
                                                  12:].reset_index(drop=True)

    machinery_year_on_year_data = machinery_data_initial.machinery_year_on_year_data()
    machinery_cumulative_year_on_year_data = machinery_data_initial.machinery_cumulative_year_on_year_data()[
                                             12:].reset_index(drop=True)

    BDI_data = macro_data_initial.BDI_data()[12:].reset_index(drop=True)
    PMI_data = macro_data_initial.PMI_data()[12:].reset_index(drop=True)
    macro_year_on_year_data = macro_data_initial.macro_year_on_year_data()[12:].reset_index(drop=True)
    macro_cumulative_year_on_year_data = macro_data_initial.macro_cumulative_year_on_year_data()[12:].reset_index(
        drop=True)

    manufacturing_cumulative_year_on_year_data = manufacturing_data_initial.manufacturing_cumulative_year_on_year_data().loc[
                                                 12:].reset_index(drop=True)

    feature_df = pd.concat([estate_year_on_year_data, estate_cumulative_year_on_year_data,
                            homeAppAndCar_cumulative_year_on_year_data,
                            infrastructure_cumulative_year_on_year_data,
                            machinery_year_on_year_data, machinery_cumulative_year_on_year_data,
                            BDI_data, PMI_data, macro_year_on_year_data, macro_cumulative_year_on_year_data,
                            manufacturing_cumulative_year_on_year_data], axis=1)
    return feature_df


def cal_period_record(basic_data_array, variable_df):
    # 计算领先指标属性集
    # 输入：
    #       basic_data_array: 基数据array
    #       variable_df: 变量集dataFrame
    # 返回：
    #       period_record: list, 属性名-(领先期数，R2)
    period_record = {}
    attribute_list = variable_df.columns
    for attr_name in attribute_list:
        attr_data = variable_df[attr_name].values
        corr_period, r2 = correlation_analysis.best_period(basic_data_array, attr_data, MAX_PERIOD)
        if corr_period > 0:
            period_record[attr_name] = (corr_period, r2)
    return period_record


def selected_attr(feature_df, period_record):
    # 基于领先期筛选数据
    # 输入：
    #       feature_df: 原始属性集数据dataFrame
    #       period_record: 领先期属性list, 属性名-(领先期数，R2)
    # 返回：
    #       train_data_attr：筛选后的属性集数据dataFrame
    leading_attr_list = list(period_record.keys())
    train_data_attr = pd.DataFrame()
    for attr in leading_attr_list:
        cutoff_attr_series = feature_df[attr][MAX_PERIOD - period_record[attr][0]:-period_record[attr][0]].reset_index(
            drop=True)
        train_data_attr = pd.concat(
            [train_data_attr, cutoff_attr_series],
            axis=1)
    return train_data_attr


def selected_label(label_data):
    # 基于领先期筛选数据
    # 输入：
    #       label_data: 原始标签数据array
    # 返回：
    #       train_data_label：筛选后的标签数据array
    return label_data[MAX_PERIOD:]


if __name__ == '__main__':
    label_array = steel_demand_data_initial.steel_demand_year_on_year_data()
    feature_df = initial_attr_data()
    period_record = cal_period_record(label_array, feature_df)
    selected_attr_df = selected_attr(feature_df, period_record)
    selected_label_array = selected_label(label_array)

    selected_attr_df['表观需求同比'] = pd.Series(selected_label_array)
    config = global_config.GlobalConfig()
    data_path = config.model_data
    selected_attr_df.to_csv(data_path, header=True, index=False)
