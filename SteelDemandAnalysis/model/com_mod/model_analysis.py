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
from model.BaggingRegression import BaggingRegression_model
from data_process.feature import feature_correlation_analysis, data_coversion
from config import global_config
import datetime
from dateutil.relativedelta import relativedelta
import logging
from config import log

max_pre_months = 120
min_pre_months = 36


def initial_data(data_type=1):
    # 用于初始化数据集
    path_config = global_config.PathConfig()
    param_config = global_config.ParamConfig()
    param_config.data_type = data_type  # 数据类型
    param_config.predict_period = 1  # 预测期为
    feature_correlation_analysis.FeatureCorrelationAnalysis(path_config, param_config).feature_correlation_analysis()
    data_coversion.DataCoversion(path_config, param_config).data_coversion()


def pre_months_select(train_model):
    # 用于不同模型选择数据时间窗
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
    return min_mse, prev_pre_months


def model_with_pre_months(train_model, pre_months):
    # 确定时间窗大小后模型输出
    data_partition = data_partitioning.DataPartition()
    all_data_df = data_partition.all_data()
    min_month = datetime.datetime(2007, 1, 1)
    max_month = datetime.datetime(2019, 5, 1) - relativedelta(months=pre_months)
    print(min_month + relativedelta(months=pre_months))
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
    # model_method.draw_picture(ground_truth, predict)
    return predict


if __name__ == '__main__':
    initial_data(2)
    train_model_list = [LinearRegression_model.MyLinearRegression().linear_regression,
                        DecisionTreeRegressor_model.MyDecisionTreeRegression().decision_tree_regression,
                        SVMRegression_model.MySVMRegression().svm_regression,
                        RandomForestRegression_model.MyRandomForestRegression().random_forest_regression,
                        BaggingRegression_model.MyBaggingRegression().Bagging_regression,
                        AdaBoostRegression_model.MyAdaBoostRegression().AdaBoost_regression,
                        GBRTRegression_model.MyGBRTRegression().GBRT_regression,
                        XGBoostRegression_model.MyXGBoost().XGBoost_regression
                        ]
    train_model = train_model_list[4]
    mse, pre_months = pre_months_select(train_model)
    print(mse, pre_months)
    y_predict = model_with_pre_months(train_model, pre_months)
    for i in y_predict:
        print(i)
