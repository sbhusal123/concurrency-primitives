import threading
import time

def standardTime():
    print("Starting standard thread")
    time.sleep(10)
    print("Ending standard thread")

def heartBeatHandler():
    while True:
        print("Sending out heartbeat signal")
        time.sleep(2)

if __name__ == "__main__":
    standardThread = threading.Thread(target=standardTime)

    deamonThread = threading.Thread(target=heartBeatHandler, daemon=True)
    deamonThread.start()

    standardThread.start()
