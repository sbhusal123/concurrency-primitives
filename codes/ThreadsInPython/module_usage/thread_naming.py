import threading
import time

def threadTarget():
    print(f"Thread {threading.current_thread().name} starting")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} ended")

for i in range(4):
    threadName = "Thread-" + str(i)
    thread = threading.Thread(target=threadTarget, name=threadName)
    thread.start()
