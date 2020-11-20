import winsound
import random
import time

#notelengths
sixteenth = 100 #1
eighth = 200 #2
dottedeight = 300 #3
quarter = 400 #4
dottedquarter = 600 #6
half = 800 #8
dottedhalf = 1200 #12
whole = 1600 #16

#notepitchnes
c4 = 262
cs4 = 277
d4 = 294
ds4 = 311
e4 = 330
f4 = 349
fs4 = 370
g4 = 392
gs4 = 415
a4 = 440
as4 = 466
b4 = 494
c5 = 523

randpitchn = 0
notelength = 0
pitchn = c4

def boop():
    randlen = random.randint(1, 8)
    randpitch = random.randint(1, 13)
    if randlen == 1:
        lengthn = sixteenth
    elif randlen == 2:
        lengthn = eighth
    elif randlen == 3:
        lengthn = dottedeight
    elif randlen == 4:
        lengthn = quarter
    elif randlen == 5:
        lengthn = dottedquarter
    elif randlen == 6:
        lengthn = half
    elif randlen == 7:
        lengthn = dottedhalf
    elif randlen == 8:
        lengthn = whole
    else:
        lengthn = whole

    if randpitch == 1:
        pitchn = c4
    elif randpitch == 2:
        pitchn = cs4
    elif randpitch == 3:
        pitchn = d4
    elif randpitch == 4:
        pitchn = ds4
    elif randpitch == 5:
        pitchn = e4
    elif randpitch == 6:
        pitchn = f4
    elif randpitch == 7:
        pitchn = fs4
    elif randpitch == 8:
        pitchn = g4
    elif randpitch == 9:
        pitchn = gs4
    elif randpitch == 10:
        pitchn = a4
    elif randpitch == 11:
        pitchn = as4
    elif randpitch == 12:
        pitchn = b4
    elif randpitch == 13:
        pitchn = c5
    else:
        pitchn = c5
    winsound.Beep(pitchn, lengthn)

while True:
    boop()






















    
    randlen = random.randint(1, 8)
    randpitch = random.randint(1, 13)
    if randpitch == 2 and randlen == 2:
        boop()
        randlen = random.randint(1, 8)
        randpitch = random.randint(1, 13)
        if randpitch == 3 and randlen == 2:
            boop()
            randlen = random.randint(1, 8)
            randpitch = random.randint(1, 13)
            if randpitch == 4 and randlen == 2:
                boop()
                randlen = random.randint(1, 8)
                randpitch = random.randint(1, 13)
                if randpitch == 5 and randlen == 2:
                    boop()
                    randlen = random.randint(1, 8)
                    randpitch = random.randint(1, 13)
                    if randpitch == 3 and randlen == 4:
                        boop()
                        randlen = random.randint(1, 8)
                        randpitch = random.randint(1, 13)
                        if randpitch == 1 and randlen == 2:
                            boop()
                            randlen = random.randint(1, 8)
                            randpitch = random.randint(1, 13)
                            if randpitch == 2 and randlen == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                                print ("lick")
                                time.sleep(100000)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

        