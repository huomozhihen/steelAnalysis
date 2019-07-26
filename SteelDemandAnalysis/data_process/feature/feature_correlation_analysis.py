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


class FeatureCorrelationAnalysis:

    def __init__(self, path_config=global_config.PathConfig(), param_config=global_config.ParamConfig()):
        self.path_config = path_config
        self.param_config = param_config
        self.MAX_PERIOD = self.param_config.corr_max_period
        self.PREDICT_PERIOD = self.param_config.predict_period

    def initial_label_data(self):
        # 读取属性集数据
        # 返回：
        #       label_df: 标签数据dataFrame
        steel_demand = steel_demand_data_initial.SteelDemand(self.path_config, self.param_config)
        if self.param_config.data_type == 1:
            label_df = steel_demand.steel_demand_year_on_year_data()
        elif self.param_config.data_type == 2:
            label_df = steel_demand.steel_demand_cumulative_year_on_year_data()
        elif self.param_config.data_type == 3:
            label_df = steel_demand.steel_demand_data()
        else:
            label_df = steel_demand.steel_demand_cumulative_data()
        return label_df

    def initial_attr_data(self):
        # 读取属性集数据
        # 返回：
        #       feature_df: 属性集数据dataFrame
        estate = estate_data_initial.Estate(self.path_config, self.param_config)
        estate_year_on_year_data = estate.estate_year_on_year_data()
        estate_cumulative_year_on_year_data = estate.estate_cumulative_year_on_year_data()

        homeAppAndCar = homeAppAndCar_data_initial.HomeAppAndCar(self.path_config, self.param_config)
        homeAppAndCar_cumulative_year_on_year_data = homeAppAndCar.homeAppAndCar_cumulative_year_on_year_data()

        infrastructure = infrastructure_data_initial.Infrastruture(self.path_config, self.param_config)
        infrastructure_cumulative_year_on_year_data = infrastructure.infrastructure_cumulative_year_on_year_data()

        machinery = machinery_data_initial.Machinery(self.path_config, self.param_config)
        machinery_cumulative_year_on_year_data = machinery.machinery_cumulative_year_on_year_data()

        macro = macro_data_initial.Macro(self.path_config, self.param_config)
        BDI_data = macro.BDI_data()
        PMI_data = macro.PMI_data()
        macro_year_on_year_data = macro.macro_year_on_year_data()
        macro_cumulative_year_on_year_data = macro.macro_cumulative_year_on_year_data()

        manufacturing = manufacturing_data_initial.Manufacturing(self.path_config, self.param_config)
        manufacturing_cumulative_year_on_year_data = manufacturing.manufacturing_cumulative_year_on_year_data()

        feature_df = pd.concat([estate_year_on_year_data, estate_cumulative_year_on_year_data,
                                homeAppAndCar_cumulative_year_on_year_data,
                                infrastructure_cumulative_year_on_year_data,
                                machinery_cumulative_year_on_year_data,
                                BDI_data, PMI_data, macro_year_on_year_data, macro_cumulative_year_on_year_data,
                                manufacturing_cumulative_year_on_year_data], axis=1)
        return feature_df

    def cal_period_record(self, basic_df, variable_df):
        # 计算领先指标属性集
        # 输入：
        #       basic_df: 基数据dataFrame
        #       variable_df: 变量集dataFrame
        # 返回：
        #       period_record: list, 属性名-(领先期数，R2)
        basic_data_array = basic_df[basic_df.columns[0]].values
        period_record = {}
        attribute_list = variable_df.columns
        for attr_name in attribute_list:
            attr_data = variable_df[attr_name].values
            corr_period, r2 = correlation_analysis.best_period(basic_data_array, attr_data, self.MAX_PERIOD)
            if corr_period >= self.PREDICT_PERIOD:
                period_record[attr_name] = (corr_period, r2)
        with open(self.path_config.attr_intro, 'w') as f:
            for k, v in period_record.items():
                f.write(k + ' ' + str(v[0]) + '\n')
        return period_record

    def selected_attr(self, feature_df, period_record):
        # 基于领先期筛选数据
        # 输入：
        #       feature_df: 原始属性集数据dataFrame
        #       period_record: 领先期属性list, 属性名-(领先期数，R2)
        # 返回：
        #       train_data_attr：筛选后的属性集数据dataFrame
        leading_attr_list = list(period_record.keys())
        train_data_attr = pd.DataFrame()
        for attr in leading_attr_list:
            cutoff_attr_series = feature_df[attr][
                                 self.MAX_PERIOD - period_record[attr][0]:-period_record[attr][0]].reset_index(
                drop=True)
            train_data_attr = pd.concat(
                [train_data_attr, cutoff_attr_series],
                axis=1)
        return train_data_attr

    def selected_label(self, label_df):
        # 基于领先期筛选数据
        # 输入：
        #       label_df: 原始标签数据dataFrame
        # 返回：
        #       train_data_label_df：筛选后的标签数据dataFrame
        return label_df[self.MAX_PERIOD:]

    def feature_correlation_analysis(self):
        # 数据初始化
        label_df = self.initial_label_data()
        feature_df = self.initial_attr_data()

        # 基于领先期数据调整
        period_record = self.cal_period_record(label_df, feature_df)
        selected_attr_df = self.selected_attr(feature_df, period_record)
        selected_label_df = self.selected_label(label_df)

        # 存储数据
        selected_label_df.reset_index(inplace=True)
        model_data = pd.concat([selected_attr_df, selected_label_df], axis=1).set_index('时间')
        model_data.to_csv(self.path_config.initial_model_data, sep=',', header=True, index=True)


if __name__ == '__main__':
    FeatureCorrelationAnalysis().feature_correlation_analysis()
