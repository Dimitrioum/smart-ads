""" Constants, used by the app

Attributes:
    _PACKAGE_LOCATION (str): location of the application
    WORKING_DIRECTORY (str): location of the working directory within the application
    SPEECH_MODEL_PATH (str): location of the speech recognition model
    SPEECH_DATA_PATH (str): location of the speech recognition data, used by the pocketsphinx library
"""
import os
from pocketsphinx import get_data_path, get_model_path


_PACKAGE_LOCATION = '/'.join(os.path.realpath(__file__).split('/')[:-2])
WORKING_DIRECTORY = _PACKAGE_LOCATION

SPEECH_MODEL_PATH = get_model_path()
SPEECH_DATA_PATH  = get_data_path()

if __name__ == '__main__':
    print(WORKING_DIRECTORY)