#!/usr/bin/env python3

def noise_walk():

    '''
    noise_walk applies noise_verify to all files within a given directory

    @input:
    None

    @output:
    noise_walk prints basic data to console (SEE:  noise_verify).
    noise_walk writes this data to countSummary.txt.
    '''

    import os
    from noiseVerify import noise_verify
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    constant_pressure_directory = input('Directory to walk:  ')

    for root, dirs, files in os.walk(constant_pressure_directory):
        for filename in files:
            result = noise_verify(constant_pressure_directory, filename)

            summary_file = open('countSummary.txt', 'a')
            summary_file.write(result)

    return
