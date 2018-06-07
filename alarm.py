import random, os, wave, pygame, time

def sound(alarm_type):
    audio_file = random.choice(os.listdir("recordings/converted/%s" % (alarm_type))) #chooses random audio file from directory

    #matches bitrate to audio file - fixes pitch
    pygame.mixer.quit
    file_path = 'recordings/converted/%s/%s' % (alarm_type, audio_file)
    print(file_path)
    file_wav = wave.open(file_path)
    frequency = file_wav.getframerate()
    pygame.mixer.init(frequency=frequency)
    pygame.mixer.music.load(file_path)
    # #pygame.mixer.pre_init(16000, -16, 2, 2048) #manually change the pitch

    pygame.init()

    pomodoro_display = pygame.display.set_mode((400, 300))
    my_sound = pygame.mixer.Sound(file_path) 

    my_sound.play()
    time.sleep(4)
    my_sound.stop() 
    pygame.display.quit()
    