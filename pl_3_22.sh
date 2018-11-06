import os, sys

n=10
try:
    os.fork()
    n+=1
    print ("hello, n=", n)
except OSError as e:
    print >>sys.stderr, "fork failed ", e.errno, "-", e.strerror
    sys.exit(1)