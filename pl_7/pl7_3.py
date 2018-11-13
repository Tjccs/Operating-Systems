import signal
import time
import sys
import random

bol = True




def controlC(sig, NULL):
    inp = print("Quer mesmo sair? Faça Ctrl+Z")

    signal.signal(signal.SIGINT, controlZ)


def controlZ(sig, NULL):
    print("ctrl+z")
    signal.signal(signal.SIGTSTP)
    bol = False


signal.signal(signal.SIGINT, controlC)


while bol:
    numb = random.randint(0, 1000)
    print(numb)
    time.sleep(0.5)
    if numb == 1:
        sys.exit()
