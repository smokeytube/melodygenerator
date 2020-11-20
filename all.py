import time, random
import winsound

while True:
    rand = random.randint(37, 4000)
    winsound.Beep(rand , 100)