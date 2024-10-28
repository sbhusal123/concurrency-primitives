import threading
import time
import random

def threadTarget(i):
    print(f"Thread {i} started..")
    time.sleep(random.randint(1, 3))
    print(f"Thread {i} finished.")

def main():
    for i in range(4):
        thread = threading.Thread(target=threadTarget, args=(i, ))
        thread.start()
    
    # this doesnt mean all runing, but actively in progress or paused
    print("\nList of all active threads:")
    for t in threading.enumerate():
        print(t)
    print("\n")

if __name__ == "__main__":
    main()

