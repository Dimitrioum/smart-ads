"""
Module contains methods for video/audio basic processing
"""
from constants.constants import WORKING_DIRECTORY
import subprocess


def extract_audio_from_video(video_input_name, audio_output_name: str, audio_sample_rate: int = 44100,
                             audio_channels_number: int = 2, audio_bitrate: int = 192, audio_output_format: str = 'mp3',
                             working_directory: str = WORKING_DIRECTORY):
    """ Extracts audio file from video file and saves it at the same directory

    Args:
        video_input_name (str): location of source video file
        audio_output_name (str): name of the output audio file
        audio_sample_rate (int): sampling rate of audio
        audio_channels_number (int): number of audio channels
        audio_bitrate (int): bitrate of audio (Kbits per second)
        audio_output_format (str): format of output audio file
        working_directory (str): path of the working directory within the application
    """
    command = 'ffmpeg -i ' + working_directory + video_input_name + '-vn -ar ' + str(audio_sample_rate) + '-ac ' \
              + str(audio_channels_number) + '-ab ' + str(audio_bitrate) + 'K' + '-f ' \
              + audio_output_format + working_directory + audio_output_name + '.' + audio_output_format

    subprocess.call(command, shell=True)






if __name__ == '__main__':
    print(help(extract_audio_from_video))