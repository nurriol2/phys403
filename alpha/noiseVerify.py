#!/usr/bin/env python3

def noise_verify(dir_name, data_name):

    '''
    noise_verify analyzes multichannel analyzer (MCA) raw data and returns basic information

    @input:
    dir_name:  The parent directory containing the file to verify.
    data_name:  The file to verify.

    @output
    Filepath: (String) The full filepath of the file noise_verify acts on

    File SHORT:  (String) The analyzed file name

    Threshold:  (Integer) A number chosen arbitrarily. Counts below this number are considered noise. This noise is removed before calculating the total number of counts in the data set.

    Maximum count:  (Integer) The largest data point in the data setself.

    Total count:  (Integer) The grand sum of counts in the data set, after noise has been removed.
    '''

    import os
    import numpy as np
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    #open file
    cwd = os.getcwd()

    #UN/Comment to toggle logging ON/OFF
    logging.disable(logging.DEBUG)

    file_path = cwd + '/' + dir_name + '/' + data_name
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


    #formatted console output
    print('RESULTS:\nFilepath:  %s\nFile SHORT:  %s\nThreshold = %i\nData Maximum = %i\nTotal Count (Signal only) = %i' %(file_path, threshold, maximum_count, total_count))

    return (file_path, data_name threshold, maximum_count, total_count)
