# Shared Resource And Data Race:

**Scope:**
- Synchronization Primitives
- Examples to use primitives within Program





## Locks (threading.Lock())

The threading module of Python includes locks as a synchronization tool. A lock has two states:

- Locked acquired using: ``lock.acquire()``

- Unlocked using: ``lock.release()``

**First Thread Access:** If lock.acquire() is called by a thread, and the lock is currently free, it will immediately acquire the lock and continue execution.

**Second Thread Access:** If another thread tries to call lock.acquire() while the lock is already held, it will be blocked (paused) and will wait until the lock is released by the first thread.

**Release:** Once the lock is released by the thread that currently holds it (via lock.release()), the next thread in line will acquire it and continue.

**Example:**

```python
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

    thread1 = threading.Thread(target=increament_counter)
    thread2 = threading.Thread(target=decreament_counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()

```

Here, we have used a lock from python threading module to increament and decreament a global resource i.e. counter. We have a two threads updating the values of our global resource, i.e. either increamenting or decreamenting the value of resource. If there were no locks, two threads would try to update the same value causing the **dirty write** leading inconsistent value of global counter. 

Here lock ensures that, only one who acquires is able to update the global value without causing a dirty write.


## RLock:

An RLock (short for Reentrant Lock) in Python is a type of lock that allows a thread to acquire the same lock multiple times without causing a deadlock. This is especially useful when a thread needs to enter a critical section multiple times in nested functions or recursive calls.

**Features**

- **Reentrant:** A thread that has already acquired the lock can acquire it again without getting blocked.

- **Reference Count:** Every time the lock is acquired by the same thread, a counter is incremented. Each release() call by that thread decrements the counter. Only when the counter reaches zero is the lock fully released and available for other threads.

- **Avoiding Deadlock:** If a function that acquires a lock calls another function that also tries to acquire the same lock, a regular Lock would cause a deadlock. However, an RLock allows the same thread to continue execution.

**Example1 With Preventing: Dirty Read + Dirty Write:**

```python
import threading

class BankAccount:

    def __init__(self):
        self.balance = 0
        self.lock = threading.RLock()

    def deposit(self, amount):
        with self.lock:  # Acquiring the lock
            print(f"Depositing {amount}")
            self.balance += amount
            self.show_balance()  # Calling another function that also needs the lock

    def withdraw(self, amount):
        with self.lock:  # Acquiring the lock
            print(f"Withdrawing {amount}")
            if self.balance >= amount:
                self.balance -= amount
                self.show_balance()
            else:
                print("Insufficient funds!")

    def show_balance(self):
        with self.lock:  # Reacquiring the lock in a nested method
            print(f"Current balance: {self.balance}")

# Instantiate the bank account
account = BankAccount()

# Create threads to deposit and withdraw
thread1 = threading.Thread(target=account.deposit, args=(100,))
thread2 = threading.Thread(target=account.withdraw, args=(50,))


# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
```

Here, we prevent the **dirty write as well as a dirty read**, i.e.:

Consider the case where hundreds of people doing a transaction on a same bank account, then the problem would be if, three of the actor are depositing balance, other two are reading a balance then there might be a case where the read and write might get inconsistent.

So, we acquire a lock once when depositing or withdrawing (lock counter = 1) and again when balance is to be shown (lock counter = 2)

> Note that, if a single therad has acquire a lock for two times, it should release the lock for two times.
> If A has acquire a lock for two times, then the other thread B cannot acquire a same lock unless A release all the lock or lock counter reaches 0.


**Example2: Multiple Locks Modifying Multiple Global Values**

Consider a case where we have a two global resources which can be only be accessed by a single entity at a time. 