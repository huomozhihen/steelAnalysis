"""
Time: 2019-7-5
Description: 进行宏观数据处理
"""

import pandas as pd
from config import global_config


def BDI_data():
    # 获取波罗的海干散货运价指数数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  BDI
    config = global_config.GlobalConfig()
    data_path = config.BDI_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['BDI']].loc[0:86].reset_index(drop=True)


def PMI_data():
    # 获取采购经理指数数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  PMI（月）
    #               PMI:新订单（月）
    config = global_config.GlobalConfig()
    data_path = config.macro_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['PMI（月）', 'PMI:新订单（月）']].loc[0:86].reset_index(drop=True)


def macro_year_on_year_data():
    # 获取宏观同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  社会消费品零售总额:当月同比（月）
    #               M1:同比（月）
    #               M2:同比（月）
    #               CPI:当月同比（月）
    #               PPI:全部工业品:当月同比（月）
    config = global_config.GlobalConfig()
    data_path = config.macro_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['社会消费品零售总额:当月同比（月）', 'M1:同比（月）',
                'M2:同比（月）', 'CPI:当月同比（月）',
                'PPI:全部工业品:当月同比（月）']].loc[0:86].reset_index(drop=True)


def macro_cumulative_year_on_year_data():
    # 获取宏观累计同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  社会消费品零售总额:累计同比（月）(整理）
    config = global_config.GlobalConfig()
    data_path = config.macro_year_on_year_data
    estate_year_on_year_df = pd.read_excel(data_path)
    return estate_year_on_year_df[
               ['社会消费品零售总额:累计同比（月）(整理）']].loc[0:86].reset_index(drop=True)


if __name__ == "__main__":
    pass
