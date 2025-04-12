
from pysine import sine
import time

C=260
Csharp=275
D=292
Dsharp=309
E=328
F=347
G=390
Gsharp=413
A=437
B=491
C2=520




def Twinkle():
    sine(frequency=C2, duration=0.05)
    time.sleep(0.05)
    sine(frequency=B, duration=0.05)
    time.sleep(0.05)
    sine(frequency=Asharp, duration=0.05)
    time.sleep(0.05)   
    sine(frequency=A, duration=0.05)
    time.sleep(0.05)
    sine(frequency=Gsharp, duration=0.05)
    time.sleep(0.05)
    sine(frequency=G, duration=0.05)
    time.sleep(0.05)
    sine(frequency=Fsharp, duration=0.1)
    time.sleep(0.05)

    sine(frequency=F, duration=0.05)
    time.sleep(0.05)
    sine(frequency=E, duration=0.05)
    time.sleep(0.05)
    sine(frequency=Dsharp, duration=0.05)
    time.sleep(0.05)   
    sine(frequency=D, duration=0.1)
    time.sleep(0.05)
    sine(frequency=Csharp, duration=0.05)
    time.sleep(0.05)
    sine(frequency=C, duration=0.05)
    time.sleep(0.05)
    sine(frequency=C, duration=0.1)
    time.sleep(0.05)

    sine(frequency=G, duration=0.05)
    time.sleep(0.05)
    sine(frequency=G, duration=0.05)
    time.sleep(0.05)
    sine(frequency=F, duration=0.05)
    time.sleep(0.05)   
    sine(frequency=F, duration=0.05)
    time.sleep(0.05)
    sine(frequency=E, duration=0.05)
    time.sleep(0.05)
    sine(frequency=E, duration=0.05)
    time.sleep(0.05)
    sine(frequency=D, duration=0.1)
    time.sleep(0.05)

    sine(frequency=C, duration=0.05)
    time.sleep(0.05)
    sine(frequency=C, duration=0.05)
    time.sleep(0.05)
    sine(frequency=G, duration=0.05)
    time.sleep(0.05)   
    sine(frequency=G, duration=0.05)
    time.sleep(0.05)
    sine(frequency=A, duration=0.05)
    time.sleep(0.05)
    sine(frequency=A, duration=0.25)
    time.sleep(0.05)
    sine(frequency=G, duration=0.5)
    time.sleep(0.05)

Twinkle()

