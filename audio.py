import os, shutil, glob
from pydub import AudioSegment

def convert():
    base_dir = os.getcwd()
    source_dir_break = base_dir + '/recordings/audio/break'  # Path where the audio files are located
    source_dir_work = base_dir + '/recordings/audio/work' # Path where the audio files are located
    output_dir_break = base_dir + '/recordings/converted/break/'
    output_dir_work = base_dir + '/recordings/converted/work/'
    extension_list = ['*.mp3', '*.aac'] #must have at least two #m4a not working

    if os.path.exists(output_dir_break):
        shutil.rmtree(output_dir_break)
    os.makedirs(output_dir_break)

    if os.path.exists(output_dir_work):
        shutil.rmtree(output_dir_work)
    os.makedirs(output_dir_work)

    os.chdir(source_dir_break)
    for extension in extension_list:
        for audio in glob.glob(extension):
            audio_filename = os.path.splitext(os.path.basename(audio))[0] + '.wav' #just a string of the file name
            my_audio = AudioSegment.from_file(audio)
            my_audio.export(output_dir_break + audio_filename, format='wav')
    #-----------------------------------------
    os.chdir(source_dir_work)
    for extension in extension_list:
        for audio in glob.glob(extension):
            audio_filename = os.path.splitext(os.path.basename(audio))[0] + '.wav' #just a string of the file name
            my_audio = AudioSegment.from_file(audio)
            my_audio.export(output_dir_work + audio_filename, format='wav')
    os.chdir(base_dir)
