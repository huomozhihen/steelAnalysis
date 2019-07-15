"""
Time: 2019-7-10
Description: 进行家电汽车数据处理
"""

import pandas as pd
from config import path_config


def homeAppAndCar_cumulative_year_on_year_data():
    # 获取家电汽车累计同比数据
    # 返回值：dataFrame
    #       时间：2012-01至2019-03
    #       属性：  产量:家用电冰箱:累计同比（月）
    #               产量:家用洗衣机:累计同比（月）
    #               产量:空调:累计同比（月）
    #               产量:汽车:累计同比（月）
    #               销量:汽车:累计同比（月）
    config = path_config.GlobalConfig()
    data_path = config.homeAppAndCar_year_on_year_data
    homeAppAndCar_cumulative_year_on_year_df = pd.read_excel(data_path)
    homeAppAndCar_cumulative_year_on_year_df.set_index('时间', inplace=True)
    return homeAppAndCar_cumulative_year_on_year_df[
               ['产量:家用电冰箱:累计同比（月）', '产量:家用洗衣机:累计同比（月）',
                '产量:空调:累计同比（月）', '产量:汽车:累计同比（月）',
                '销量:汽车:累计同比（月）']].loc['2013-01':'2019-03']


if __name__ == '__main__':
    pass
