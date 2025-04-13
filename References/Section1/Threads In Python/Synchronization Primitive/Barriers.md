# Barriers

Barriers are synchronization primitives that allows multiple threads or processes to all reach a certain point in the program,
and none of them can proceed past that point until all others have also reached it.

- Initialized with a count (the number of threads/processes that need to wait at the barrier).
- Each thread calls a wait() method when it reaches the barrier.
- When the number of waiting threads equals the initial count, all threads are released to continue their execution.

```python
import threading

# barriers for 3 threads
barrier = threading.Barrier(3)

# each thread should call wait for 3 times to pass barrier
barrier.wait()
barrier.wait()
barrier.wait()
```

So the basic idea behind the barrier is, to have a variable that represents the strength of barrier, each thread waits at a barrier
calling wait. So call to `wait` is a blocking call. 

## Example:

Example below implements shows a three workers:
- Executing some task.
- Tasks are task1, task2, task3
- Constraint is we want to have task3 be executed after all threads finish executing task3.


```python
import threading
import time

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
```
