import os
import time
import logging

version = 0.1
description = 'demo'

"""
This file is intended to record simulation results and make a comparison.  
"""


def log():
    # Logging configure
    save_dir = 'E:\\workspace\\logs'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_file = os.path.join(save_dir,
                             'version_{0}_{1}_'.format(version, description) + time.strftime("%y%m%d_%H_%M") + '.txt')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename=save_file,
                        filemode='a')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
