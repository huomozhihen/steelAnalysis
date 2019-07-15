"""
Time: 2019-7-10
Description: 进行制造业数据处理
"""

import pandas as pd
from config import global_config

path_config = global_config.PathConfig()
param_config = global_config.ParamConfig()


def manufacturing_cumulative_year_on_year_data():
    # 获取制造业累计同比数据
    # 返回值：dataFrame
    #       属性：  固定资产投资完成额:制造业:累计同比
    #               固定资产投资完成额:黑色金属矿采选业:累计同比
    #               固定资产投资完成额:制造业:金属制品业:累计同比
    #               固定资产投资完成额:制造业:黑色金属冶炼及压延加工业:累计同比
    #               固定资产投资完成额:制造业:通用设备制造业:累计同比
    #               固定资产投资完成额:制造业:专用设备制造业:累计同比
    #               固定资产投资完成额:制造业:电气机械及器材制造业:累计同比
    #               固定资产投资完成额:制造业:仪器仪表制造业:累计同比
    #               PPI:全部工业品:累计同比
    data_path = path_config.manufacturing_year_on_year_data
    manufacturing_cumulative_year_on_year_df = pd.read_excel(data_path)
    manufacturing_cumulative_year_on_year_df.set_index('时间',inplace=True)
    return manufacturing_cumulative_year_on_year_df[
               ['固定资产投资完成额:制造业:累计同比', '固定资产投资完成额:黑色金属矿采选业:累计同比',
                '固定资产投资完成额:制造业:金属制品业:累计同比', '固定资产投资完成额:制造业:黑色金属冶炼及压延加工业:累计同比',
                '固定资产投资完成额:制造业:通用设备制造业:累计同比', '固定资产投资完成额:制造业:专用设备制造业:累计同比',
                '固定资产投资完成额:制造业:电气机械及器材制造业:累计同比', '固定资产投资完成额:制造业:仪器仪表制造业:累计同比',
                'PPI:全部工业品:累计同比']].loc[param_config.begin_time:param_config.end_time]


if __name__ == '__main__':
    print(manufacturing_cumulative_year_on_year_data())
    pass
