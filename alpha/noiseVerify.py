#!/usr/bin/env python3

def noise_verify(dir_name = '/testPulseData/'):

    import os
    import numpy as np
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    data_name = input('data name:  ')

    #open (constant pressure) file
    cwd = os.getcwd()

    #UN/Comment to toggle logging ON/OFF
    logging.disable(logging.DEBUG)

    file_path = cwd + dir_name + data_name
    logging.debug('file_path:  %s' %file_path)

    file = open(file_path)
    raw_data = file.readlines()
    file.close()


    #strip header and tail
    count_data = raw_data[12:len(raw_data)-1]
    logging.debug('count_data = %s' %count_data)

    #convert the dtype from string to integers
    for dataPoint in count_data:
        numeric_dataPoint = dataPoint.strip('\n')
        numeric_dataPoint = int(numeric_dataPoint)

        count_data.insert(count_data.index(dataPoint), numeric_dataPoint)
        del count_data[count_data.index(dataPoint)]

    logging.debug(count_data)
    logging.debug(type(count_data[282]))

    #convert the list to an np.array
    signal_noise_array = np.array(count_data)
    logging.debug(type(signal_noise_array))

    #calculate maximum from the data
    maximum_count = np.amax(signal_noise_array)
    logging.debug('maximum of count:  %i' %maximum_count)

    #arbitrarily choose a threshold
    threshold = 10

    #assume anything below the threshold is noise
    #select data above threshold
    signal_array = signal_noise_array[signal_noise_array > threshold]
    assert len(signal_noise_array) > len(signal_array)
    logging.debug(signal_array)

    #sum the total number of counts above threshold
    total_count = np.sum(signal_array)
    logging.debug('total count = %i' %total_count)

    #basic statistics
    #threshold
    #maximum of data
    #total count

    print('RESULTS:\nThreshold = %i\nData Maximum = %i\nTotal Count (Signal only) = %i' %(threshold, maximum_count, total_count))

    return (threshold, maximum_count, total_count)
