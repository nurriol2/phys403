#!/usr/bin/env python3

def fit_to_data():


    import os
    import numpy as np
    import matplotlib.pyplot as plt
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    #ask user for filename
    user_file = input('Enter filename:  ')

    #format user_file for file_path
    file_name = '/' + user_file

    #calibration data is located in testPulseData directory
    test_pulse_dir = os.path.abspath('testPulseData')

    #create full path to file
    file_path = test_pulse_dir + file_name

    logging.debug('file_path = %s' %file_path)

    file = open(file_path)
    raw_data = file.readlines()
    file.close()

    count_data = raw_data[12:len(raw_data) - 1]

    #y data of histogram
    count_array = np.array(count_data, dtype = int)
    logging.debug('count_data_array:  %s' %count_data_array)

    #x data of histogram
    bins_array = np.linspace(1, 1024, 1024)
    logging.debug(len(bins))

    




    return
