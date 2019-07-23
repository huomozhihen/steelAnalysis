from data_process.feature import feature_correlation_analysis
from data_process.feature import data_coversion
from model.com_mod import data_partitioning
from config import global_config
import datetime
import dateutil.relativedelta
from model.BaggingRegression import BaggingRegression_model
import numpy as np


def model_predict():
    path_config = global_config.PathConfig()
    param_config = global_config.ParamConfig()
    param_config.set_begin_time('2012-01')
    param_config.set_end_time('2019-5')
    param_config.set_predict_period(1)
    fca = feature_correlation_analysis.FeatureCorrelationAnalysis(path_config, param_config)
    fca.feature_correlation_analysis()
    data_coversion.DataCoversion(path_config, param_config).data_coversion()
    data_partitioning.DataPartition(path_config, param_config).data_partitioning()
    feature_df = fca.initial_attr_data()

    predict_time = datetime.datetime.strptime('2019-6', '%Y-%m')
    data_attr = []
    with open(path_config.attr_intro, mode='r') as f:
        for line in f:
            attr, period = line.split()
            data_attr.append(feature_df[attr][
                                 predict_time - dateutil.relativedelta.relativedelta(
                                     months=int(period))])
    data_array = np.array(data_attr)
    data_array = data_array[np.newaxis, :]
    model = BaggingRegression_model.final_Bagging_regression()
    data_value = model.predict(data_array)
    print(data_value)


if __name__ == '__main__':
    model_predict()
