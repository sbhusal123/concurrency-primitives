import threading
import time

def threadTarget():
    print("Child thread starting\n")
    time.sleep(2)
    print(f"Currrent Thread: {threading.current_thread()} \n")
    print(f"Main Thread: {threading.main_thread()}\n")
    print("Child thread ended.")

thread = threading.Thread(target=threadTarget)
thread.start()
thread.join()

