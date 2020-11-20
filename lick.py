import winsound


#notelengths
sixteenth = 100 #1
eighth = 200 #2
dottedeight = 300 #3
quarter = 400 #4
dottedquarter = 600 #6
half = 800 #8
dottedhalf = 1200 #12
whole = 1600 #16

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

winsound.Beep(d4, eighth)
winsound.Beep(e4, eighth)
winsound.Beep(f4, eighth)
winsound.Beep(g4, eighth)
winsound.Beep(e4, quarter)
winsound.Beep(c4, eighth)
winsound.Beep(d4, whole)