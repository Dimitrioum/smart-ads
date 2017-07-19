"""
Module contains methods for video/audio basic processing
"""
import os
import subprocess
from constants.constants import WORKING_DIRECTORY, SPEECH_DATA_PATH, SPEECH_MODEL_PATH
from pocketsphinx import AudioFile, get_data_path, get_model_path, Decoder


def extract_audio_from_video(video_input_name: str, audio_output_name: str, audio_sample_rate: int = 44100,
                             audio_channels_number: int = 2, audio_bitrate: int = 192, audio_output_format: str = 'mp3',
                             working_directory: str = WORKING_DIRECTORY):
    """ Extracts audio file from video file and saves it into the same directory

    Args:
        video_input_name (str): location of source video file
        audio_output_name (str): name of the output audio file
        audio_sample_rate (int): sampling rate of audio
        audio_channels_number (int): number of audio channels
        audio_bitrate (int): bitrate of audio (Kbits per second)
        audio_output_format (str): format of output audio file
        working_directory (str): location of the working directory within the application
    """
    command = 'ffmpeg -i ' + os.path.join(working_directory, video_input_name) + ' -vn -ar ' + str(audio_sample_rate) \
              + '-ac ' + str(audio_channels_number) + ' -ab ' + str(audio_bitrate) + 'K' + ' -f ' \
              + audio_output_format + os.path.join(working_directory, audio_output_name) + '.' + audio_output_format

    subprocess.call(command, shell=True)


def convert_audio_to_raw(audio_input_name: str, audio_output_name: str, working_directory: str = WORKING_DIRECTORY):
    """ Converts audio file to .raw format and saves it into the same directory

    Args:
        audio_input_name (str): name of the input audio file
        audio_output_name (str): name of the output raw audio file
        working_directory (str): location of the working directory within the application
    """

    command = 'ffmpeg -i ' + os.path.join(working_directory, audio_input_name) + ' -f s16le -acodec pcm_s16le ' \
              + os.path.join(working_directory, audio_output_name) + '.raw'

    subprocess.call(command, shell=True)


def get_text_from_audio(audio_input_name: str, working_directory: str = WORKING_DIRECTORY):
    """ Gets text from audio file (using pocketsphinx-python library)

    Args:

    Return:
        list: text from audio file

    """

    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', os.path.join(SPEECH_MODEL_PATH, 'en-us'))
    config.set_string('-lm', os.path.join(SPEECH_MODEL_PATH, 'en-us.lm.bin'))
    config.set_string('-dict', os.path.join(SPEECH_MODEL_PATH, 'cmudict-en-us.dict'))
    decoder = Decoder(config)

    # Decode streaming data.
    decoder.start_utt()
    with open(os.path.join(working_directory, audio_input_name), 'rb') as stream:
        while True:
            buf = stream.read(1024)
            if buf:
                decoder.process_raw(buf, False, False)
            else:
                break

    decoder.end_utt()
    text_from_audio = [seg.word for seg in decoder.seg()]

    return text_from_audio if text_from_audio else 'Audio file doesn\'t contain words'

def find_texts_similarities():
    pass


if __name__ == '__main__':
    text_audio = get_text_from_audio(audio_input_name='test_raw.raw')
    print(list(text_audio))