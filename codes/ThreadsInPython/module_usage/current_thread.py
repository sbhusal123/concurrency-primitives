import threading


def threadTarget():
    print(f"Current thread: {threading.current_thread()}")

threads = []

for i in range(10):
    thread = threading.Thread(target=threadTarget)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
