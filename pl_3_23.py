import os, sys
import multiprocessing

"""
def files_w():
    file=open("TMP"+str(os.getpid()),'w')
    file.close()

for i in range(8):
    newp = multiprocessing.Process(target=files_w)
    newp.start()
    newp.join()
"""
for i in range(8):
    os.fork()
    file=open("TMP"+str(os.getpid()),'w')
    file.close()