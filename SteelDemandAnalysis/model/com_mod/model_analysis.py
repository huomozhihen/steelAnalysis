"""
Time： 2019-7-16
Description： 模型分析
"""
from model.com_mod import data_partitioning, model_method
from model.LinearRegression import LinearRegression_model
from model.DecisionTreeRegression import DecisionTreeRegressor_model
from model.SVMRegression import SVMRegression_model
from model.RandomForestRegression import RandomForestRegression_model
from model.AdaBoostRegression import AdaBoostRegression_model
from model.GBRTRegression import GBRTRegression_model
from model.XGBoostRegression import XGBoostRegression_model
from model.LightGBMRegression import LightGBMRegression_model
from data_process.feature import feature_correlation_analysis, data_coversion
from config import global_config
import datetime
from dateutil.relativedelta import relativedelta
import logging
from config import log

max_pre_months = 120
min_pre_months = 36


def initial_data():
    path_config = global_config.PathConfig()
    param_config = global_config.ParamConfig()
    param_config.data_type = 1  # 同比数据
    param_config.predict_period = 1  # 预测期为1个月
    feature_correlation_analysis.FeatureCorrelationAnalysis(path_config, param_config).feature_correlation_analysis()
    data_coversion.DataCoversion(path_config, param_config).data_coversion()


def pre_months_select(train_model):
    data_partition = data_partitioning.DataPartition()
    all_data_df = data_partition.all_data()
    min_month = datetime.datetime(2007, 1, 1)
    min_mse = 10000
    prev_pre_months = min_pre_months
    for pre_months in range(min_pre_months, max_pre_months + 1):
        max_month = datetime.datetime(2019, 5, 1) - relativedelta(months=pre_months)
        cur_month = min_month
        ground_truth = []
        predict = []
        while cur_month <= max_month:
            x_s = cur_month
            x_e = cur_month + relativedelta(months=pre_months - 1)
            y_s = cur_month + relativedelta(months=pre_months)
            y_e = y_s
            train_df, test_df = data_partition.divide_data(all_data_df, x_s, x_e, y_s, y_e)
            train_attr, train_label, test_attr, test_label = model_method.load_data(train_df, test_df)
            model = train_model(train_attr, train_label)
            predict_label = model.predict(test_attr)
            ground_truth.append(test_label[0])
            predict.append(predict_label[0])
            cur_month += relativedelta(months=+1)
        mse = model_method.mse(ground_truth, predict)
        if mse < min_mse:
            min_mse = mse
            prev_pre_months = pre_months
    print(min_mse, prev_pre_months)
    return min_mse, prev_pre_months


if __name__ == '__main__':
    train_model_dict = [LinearRegression_model.MyLinearRegression().linear_regression,
                        DecisionTreeRegressor_model.MyDecisionTreeRegression().decision_tree_regression,
                        SVMRegression_model.MySVMRegression().svm_regression,
                        RandomForestRegression_model.MyRandomForestRegression().random_forest_regression,
                        AdaBoostRegression_model.MyAdaBoostRegression().AdaBoost_regression,
                        GBRTRegression_model.MyGBRTRegression().GBRT_regression,
                        XGBoostRegression_model.MyXGBoost().XGBoost_regression,
                        LightGBMRegression_model.MyLightGBM().lightGBM_regression
                        ]
    train_model = train_model_dict[1]
    begin_time = datetime.datetime.now()
    pre_months_select(train_model)
    end_time = datetime.datetime.now()
    print((end_time - begin_time).seconds)
    initial_data()
