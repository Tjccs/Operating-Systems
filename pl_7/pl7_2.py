import signal
import time
import sys

list_inp = list()
start_time = time.time()



bol = True
count = 0 


def handler(sig, NULL):
    global count
    count += 5
    print("Passaram: " + str(count) + "segundos.")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 5, 5)

while bol:
    final_time = time.time()
    inp = input("Insira um numero: \n")
    list_inp.append(inp)
    
    if len(list_inp) == 20:
        result = final_time - start_time
        print(result)
        bol = False
        sys.exit(1)
    else:
        final_time += time.time()
    
