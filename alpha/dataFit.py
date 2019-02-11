#!/usr/bin/env python3

def fit_to_data():


    import os
    import numpy as np
    import matplotlib.pyplot as plt
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')


    cwd = os.getcwd()
    #test pulse data is collected specifically for channel calibration
    dir_name = '/testPulseData/'

    file_path = cwd + dir_name

    file = open(file_path)
    raw_data = file.readlines()
    file.close()

    count_data = raw_data[12:len(raw_data) - 1]

    for dataPoint in count_data:
        dataPoint = int(dataPoint)
    logging.debug(count_data)





    return
