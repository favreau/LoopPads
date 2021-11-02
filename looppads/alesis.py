import mido
from playsound import playsound 


import glob
import os

kits = dict()

loops_folder = '/Users/favreau/Music/Loops/'
folders = glob.glob(loops_folder + '*')
# print(folders)
for folder in folders:
    files = glob.glob(folder + '/*')
    base_name = os.path.basename(folder)
    sounds = list()
    for file in files:
        sounds.append(os.path.basename(file))
    kits[base_name] = sounds

    import threading
from multiprocessing import Process

active_threads = dict()

class SoundThread (threading.Thread):
    
    MODE_ONE_SHOT = 0
    MODE_LOOP = 1
    
    def __init__(self, kit, sound_id, mode):      
        threading.Thread.__init__(self)
        self._kit = kit
        self._sound_id = sound_id
        self._mode = mode
        
    def play_sound(self):
        if self._sound_id < len(kits[self._kit]):
            if self._sound_id < len(kits[self._kit]):
                # print('Play %s: %s' % (self._kit, kits[self._kit][self._sound_id]))
                playsound(loops_folder + '/' + self._kit + '/' + kits[self._kit][self._sound_id], block=True)
            else:
                print('Wrong sound')
        else:
            print('Wrong kit')
        
    def run(self):
        if self._mode == self.MODE_ONE_SHOT:
            ''' One shot '''
            print('One shot')
            self.play_sound()
        elif self._mode == self.MODE_LOOP:
            ''' Loop '''
            while True:
                self.play_sound()

# Alesis Pads
# 44 45 46
# 40 41 42
# 36 37 38

alesis_pads = dict()
alesis_pads[44] = 0
alesis_pads[45] = 1
alesis_pads[46] = 2
alesis_pads[40] = 3
alesis_pads[41] = 4
alesis_pads[42] = 5
alesis_pads[36] = 6
alesis_pads[37] = 7
alesis_pads[38] = 8


def play_sound():
    filename = loops_folder + '/Pacman/' + kits['Pacman'][0]
    print(filename)
    playsound(filename, block=True)
    

if __name__ == '__main__':
    freeze_support()
    import random
    i = 3
    while i> 0:
        note = 44 # + random.randint(0, 2) # alesis.receive().note
        if active_threads.get(note):
            print('Stop thread %d' % note)
            active_threads[note].terminate()
            active_threads[note] = None

        print('Start thread %d' % note)
    #     t = SoundThread('Pacman', alesis_pads[note], SoundThread.MODE_ONE_SHOT)
        t = Process(target=play_sound)
        t.start()
    #     t.join()
        active_threads[note] = t
        import time
        time.sleep(1)
        i -= 1
