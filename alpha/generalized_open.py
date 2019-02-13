def my_open(user_dir, user_file):

    """
    extract signal + noise count data from any data set given directory and filename

    my_open assumes alpha is the parent directory

    @input:
    user_dir:  (string) directory name
    user_file:  (string) file name

    @output:

    raw_data:  (list) a list containing signal + noise data from a data set 
    """

    import os
    import logging
    logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

    #format user_file for file_path
    file_name = '/' + user_file

    #access testPulseData directory
    test_pulse_dir = os.path.abspath(user_dir)

    #create full path to file
    file_path = test_pulse_dir + file_name
    logging.debug('file_path = %s' %file_path)

    file = open(file_path)
    raw_data = file.readlines()
    file.close()

    return raw_data
