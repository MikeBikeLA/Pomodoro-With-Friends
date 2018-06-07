import pygame, time, os, glob, wave, random, shutil, audio, alarm
from pydub import AudioSegment

def main():
    convert_audio()
    count = 0
    while True: 
        alarm('work')
        time.sleep(1500)
        count += 1
        if count < 4:
            alarm('break')
            time.sleep(300)
        else:
            count = 0
            alarm('break')
            time.sleep(900)
    

def convert_audio():
    base_dir = os.getcwd()
    source_dir_break = base_dir + '/recordings/original/break'  # Path where the audio files are located
    source_dir_work = base_dir + '/recordings/original/work' # Path where the audio files are located
    output_dir_break = base_dir + '/recordings/waves/break/'
    output_dir_work = base_dir + '/recordings/waves/work/'
    extension_list = ('*.mp3', '*.aac') #must have at least two #m4a not working

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

def alarm(alarm_type):
    audio_file = random.choice(os.listdir("recordings/waves/%s" % (alarm_type))) #chooses random audio file from directory

    #matches bitrate to audio file - fixes pitch
    pygame.mixer.quit
    file_path = 'recordings/waves/work/%s' % (audio_file)
    print(file_path)
    file_wav = wave.open(file_path)
    frequency = file_wav.getframerate()
    pygame.mixer.init(frequency=frequency)
    pygame.mixer.music.load(file_path)
    # #pygame.mixer.pre_init(16000, -16, 2, 2048) #manually change the pitch

    pygame.init()

    pomodoro_display = pygame.display.set_mode((400, 300))
    sound_work = pygame.mixer.Sound(file_path) 

    sound_work.play()
    time.sleep(3)
    sound_work.stop() 

if __name__ == '__main__':
    main()