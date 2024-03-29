"""
Time: 2019-7-8
Description: 进行房地产数据处理
"""

import pandas as pd
from SteelDemandAnalysis.config import global_config


class Estate:

    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config

    def estate_year_on_year_data(self):
        # 获取房地产同比数据
        # 返回值：dataFrame
        #       属性：  房地产开发投资完成额: 住宅:当月同比
        #               房地产开发投资完成额: 建筑工程:当月同比
        #               房地产开发投资完成额: 安装工程:当月同比
        #               房地产开发投资完成额: 设备工器具购置:当月同比
        #               房地产开发投资完成额: 其他费用:当月同比
        #               商品房销售面积: 住宅:当月同比
        #               房屋新开工面积: 住宅:当月同比
        #               房屋施工面积: 住宅:当月同比
        #               房屋竣工面积: 住宅:当月同比
        data_path = self.path_config.estate_year_on_year_data
        estate_year_on_year_df = pd.read_excel(data_path)
        estate_year_on_year_df.set_index('时间', inplace=True)
        return estate_year_on_year_df[
                   ['房地产开发投资完成额:住宅:当月同比', '房地产开发投资完成额:建筑工程:当月同比',
                    '房地产开发投资完成额:安装工程:当月同比', '房地产开发投资完成额:设备工器具购置:当月同比',
                    '房地产开发投资完成额:其他费用:当月同比', '商品房销售面积:住宅:当月同比',
                    '房屋新开工面积:住宅:当月同比', '房屋施工面积:住宅:当月同比',
                    '房屋竣工面积:住宅:当月同比']].loc[self.param_config.begin_time:self.param_config.end_time]

    def estate_cumulative_year_on_year_data(self):
        # 获取房地产累计同比数据
        # 返回值：dataFrame
        #       属性：  房地产开发投资完成额: 住宅:累计同比
        #               房地产开发投资完成额: 建筑工程:累计同比
        #               房地产开发投资完成额: 安装工程:累计同比
        #               房地产开发投资完成额: 设备工器具购置:累计同比
        #               房地产开发投资完成额: 其他费用:累计同比
        #               商品房销售面积: 住宅:累计同比
        #               房屋新开工面积: 住宅:累计同比
        #               房屋施工面积: 住宅:累计同比
        #               房屋竣工面积: 住宅:累计同比
        data_path = self.path_config.estate_year_on_year_data
        estate_cumulative_year_on_year_df = pd.read_excel(data_path)
        estate_cumulative_year_on_year_df.set_index('时间', inplace=True)
        return estate_cumulative_year_on_year_df[
                   ['房地产开发投资完成额:住宅:累计同比', '房地产开发投资完成额:建筑工程:累计同比',
                    '房地产开发投资完成额:安装工程:累计同比', '房地产开发投资完成额:设备工器具购置:累计同比',
                    '房地产开发投资完成额:其他费用:累计同比', '商品房销售面积:住宅:累计同比',
                    '房屋新开工面积:住宅:累计同比', '房屋施工面积:住宅:累计同比',
                    '房屋竣工面积:住宅:累计同比']].loc[self.param_config.begin_time:self.param_config.end_time]


if __name__ == '__main__':
    pass
