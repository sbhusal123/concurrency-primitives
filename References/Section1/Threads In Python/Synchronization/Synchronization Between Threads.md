# Deadlocks And Race Conditions

**Scope:**
- Deadlock example with Dining Philosophers Problem

- Race Condition and Shared Resources

- Data race including:

    - Conditions, Semaphores, Event and Barriers

    - Fundamenal issues to protect multithreaded applications



## Dining Philosophers And Race Condition:

- Famous illustration of synchronization problem that occurs in concurrent systems.

![Dining Philosopher](../../../../images/Dining%20Philosopher.png)

In the illustration above, consider five philosophers sitting on a dining table with four forks to eat the dinner. They have a fork place on their left and right side. Philosophers either think or pick up a fork and eat.

While four of the fork are used by the two of philosopher, other philosopher had to wait till one of the fork is available. In this case, dinner table reaches a deadlock state.

This kind of resonates with the synchronization issue, where the resource aviability is lesser than the threads / processes.

**Illustrates:**
- Problem may occur while designing concurrent system.
- Fork - system resource
- Philosophers - competing process

## Pythonic Implementation For Dining Philosopher Problem

- Implementation using RLocks
- Rlocks - forks


```python
import threading
import time
import random

class Philosopher(threading.Thread):

    def __init__(self, name, leftFork, rightFork):
        print(f"{name} Has Sat Down On a Table")
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print(f"{threading.current_thread().name} has started thinking.")

        while True:
            # Acquire left fork
            time.sleep(random.randint(1, 5))
            print(f"{threading.current_thread().name} has finished thinking.")
            self.leftFork.acquire()
            time.sleep(random.randint(1, 5))

            try:
                print(f"{threading.current_thread().name} has accquired left fork.")
                self.rightFork.acquire()

                try:
                    print(f"{threading.current_thread().name} has acquired both forks, and is currently eating.")
                finally:
                    self.rightFork.release()
                    print(f"{threading.current_thread().name} has released right fork.")
            finally:
                self.leftFork.release()
                print(f"{threading.current_thread().name} has released left fork.")

fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = Philosopher("Philosopher1", fork1, fork2)
philosopher2 = Philosopher("Philosopher2", fork2, fork3)
philosopher3 = Philosopher("Philosopher3", fork3, fork4)
philosopher4 = Philosopher("Philosopher4", fork4, fork5)
philosopher5 = Philosopher("Philosopher5", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()

```

Here we have 5 philosopher, and 5 forks as RLock, in the run method we have:

- first acquire left fork
- Then try to acquire right fork

Above code suffers from deadlock when all the philosopher acquire left fork and program halts its execution. That's why always checking for the deadlock is always necessary.

```sh
# Output
Philosopher1 Has Sat Down On a Table
Philosopher2 Has Sat Down On a Table
Philosopher3 Has Sat Down On a Table
Philosopher4 Has Sat Down On a Table
Philosopher5 Has Sat Down On a Table

Philosopher1 has started thinking.
Philosopher2 has started thinking.
Philosopher3 has started thinking.
Philosopher5 has started thinking.
Philosopher4 has started thinking.

Philosopher2 has finished thinking.
Philosopher1 has finished thinking.
Philosopher3 has finished thinking.
Philosopher4 has finished thinking.
Philosopher5 has finished thinking.

Philosopher2 has accquired left fork.
Philosopher3 has accquired left fork.
Philosopher1 has accquired left fork.
Philosopher5 has accquired left fork.
Philosopher4 has accquired left fork.
```

>  Race Condition:  A race condition occurs when multiple processes or threads access shared resources concurrently, leading to unpredictable outcomes due to timing, potentially causing data corruption or unexpected behavior. Above example of Dining philosopher is also an example of race condition.

> Race condition is a significant problem in concurrent programming. The condition occurs when one thread tries to modify a shared resource at the same time that another thread is modifying that resource – t​his leads to garbled output, which is why threads need to be synchronized.

