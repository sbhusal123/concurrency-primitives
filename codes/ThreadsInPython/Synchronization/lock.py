import threading
import time
import random

# global resource
counter = 1

# lock
lock = threading.Lock()

def increament_counter():
    global counter
    lock.acquire()
    try:
        while counter < 1000:
            counter += 1
            print(f"Worker A increamented counter to: {counter}")
    finally:
        lock.release()

def decreament_counter():
    global counter
    lock.acquire()
    try:
        while counter > -1000:
            counter -= 1
            print(f"Worker A decreamented counter to: {counter}")
    finally:
        lock.release()


def main():
    t0 = time.time()

    thread2 = threading.Thread(target=decreament_counter)
    thread1 = threading.Thread(target=increament_counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
