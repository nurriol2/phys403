#!/usr/bin/env python3

def noise_walk():

    import os
    from noiseVerify import noise_verify
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    cwd = os.getcwd()

    constant_pressure_directory = input('Directory to walk:  ')

    for root, dirs, files in os.walk(constant_pressure_directory):
        #print('root:  %s' %root)
        #print('dirs:  %s' %dirs)
        #print('files:  %s' %files)

        for filename in files:
            noise_verify(constant_pressure_directory, filename)

    return
