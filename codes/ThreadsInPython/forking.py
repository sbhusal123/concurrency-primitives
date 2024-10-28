import os

"""
Note that this implementation is only available in unix based os.
"""

def child():
    print(f"We are in the child process with PID={os.getpid()}")

def parent():
    newRef = os.fork()
    if newRef == 0:
        child()
    else:
        child()

parent()
