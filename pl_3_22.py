import os, sys

n=10
try:
    pid = os.fork()
    if pid==0:
        n/=2
    else:
        n*=2
    
    print ("hello, n=", n)

except OSError as e:
    print >>sys.stderr, "fork failed ", e.errno, "-", e.strerror
    sys.exit(1)