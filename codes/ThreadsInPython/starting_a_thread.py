from threading import Thread

class WorkerThread(Thread):

    def __init__(self):
        print("Created worker thread object")
        Thread.__init__(self)
    
    def run(self):
        print("Thread is now running.")
    
thread = WorkerThread()

thread.start()
print("Started worked thread")

thread.join()
print("Worker thread finished execution")
