
from pynput.keyboard import Key, Controller
import time



keyboard = Controller()
time.sleep(2)

f = open("beemovie.txt", "r") # Can be "beemovie.txt" or "neverGonnaGive.txt"


f1 = f.readlines()
for line in f1:
    for char in line:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.12)
    keyboard.press(Key.enter)

f.close()


#keyboard.press(contents)
#keyboard.release(contents)
#time.sleep(.12)
###   time.sleep(1)

