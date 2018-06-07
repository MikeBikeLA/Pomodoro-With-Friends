import audio, alarm, time
from threading import Event

audio.convert()
time_work = 0.1
time_break = 0.1
time_break_long = 0.1
count = 0
while True: 
    alarm.sound('work')
    print("Time to work (%i mins)" % (time_work))
    time.sleep(time_work*60.0)
    count += 1
    if count < 4: #fewer than 4 sessions
        alarm.sound('break')
        print("Time to take a break (%i mins)" % (time_break))
        time.sleep(time_break*60.0)
    else: #4th session, longer break
        count = 0
        alarm.sound('break')
        print("Time to take a long break (%i mins)" % (time_break_long))
        time.sleep(time_break_long*60.0)
