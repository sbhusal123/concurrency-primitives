import threading
import random

def executeThread(i):
    sleep = random.randint(1, 10)

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i, ))
    thread.start()

    # returns a list of alive threads
    print("Active Therads:", threading.enumerate())
