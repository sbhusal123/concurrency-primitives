import multiprocessing
import time

def processWorker():
    t1 = time.time()
    print(f"Process started at: {t1}")
    time.sleep(20)

process = multiprocessing.Process(target=processWorker)
print(f"Process: {process}")

# process started
process.start()

print("Terminating process..")
process.terminate()

process.join()

print(f"Process terminated: {process}")
