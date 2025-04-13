import threading
import time

"""
Barriers used when:
- group of threads had to wait on each others
"""

class Worker(threading.Thread):

    def __init__(self, name, barrier, *args, **kwargs):
        self.barrier = barrier
        threading.Thread.__init__(self, name=name, *args, **kwargs)

    def task_1(self):
        print(f"Thread {self.name} Executing task1....")
        time.sleep(1)
        print(f"Thread {self.name} Finished executing task1....")

    def task_2(self):
        print(f"Thread {self.name} Executing task2....")
        time.sleep(1)
        print(f"Thread {self.name} Finished executing task2....")

    def task_3(self):
        print(f"Thread {self.name} Executing task3....")
        time.sleep(1)
        print(f"Thread {self.name} Finished executing task3....")

    
    def run(self):
        self.task_1()
        self.task_2()

        # wait untill all threads finishes executing task 1 and 2
        self.barrier.wait()
        print("Finished executing task1 and task2")
        print("Now executing task 3")
        self.task_3()



num_threads = 3

workers = [ ]

barrier = threading.Barrier(num_threads)
for i in range(0, 3):
    worker = Worker(name=f"{i}", barrier=barrier)
    workers.append(worker)

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()
