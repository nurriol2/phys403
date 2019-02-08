#! /usr/bin/env python3

import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

def indexer(filename):

    #open test data
    import os

    cwd = os.getcwd()
    testPulseDir = cwd + '/testPulseData/'

    file = open(testPulseDir + filename)
    mcaOutput = file.readlines()
    file.close()

    #strip the header and tail
    countData = mcaOutput[12:1036]

    #index data by channel number
    channelToCount = {}

    i = 1
    for count in countData:

        count = count.strip('\n')
        count = int(count)

        channelToCount[i] = count
        i += 1

    logging.debug(channelToCount)

    return channelToCount


#search for maximum counts
#return channel number of maximum count
#associate pulse energy with channel
