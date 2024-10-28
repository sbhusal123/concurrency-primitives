import threading
import random

def executeThread(i):
    print(f"Thread {i} started.")
    sleep = random.randint(1, 10)
    print(f"Thread {i} finished execution.")

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i, ))
    thread.start()

    # returns a list of alive threads
    print("Active Therads:", threading.enumerate())
