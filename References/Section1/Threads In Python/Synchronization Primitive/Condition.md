# Conditions

## Condition
- Waits on a signal from another thread.

- Example:
    - Another thread has finished execution.
    - Curret thread can procede to perform.

`threading.Condition` in Python is a powerful synchronization primitive that helps manage access to shared resources, particularly when one or more threads need to wait for certain conditions to be met before proceeding.

**Example Illustration: In C**

```txt
    int is_done;
    mutex_t done_lock;
    cond_t dont_cond;

        Thread A                                        Thread B
    // do the work here..                       //stop here untill work done..
    mutex_lock(&done_lock)                      mutex_lock(&done_lock)
    is_done=1                                   if(!is_done)
    cond_signal(&done_cond, &done_lock)           cond_wait(&done_cond, &done_lock)
    mutex_unlock(&done_lock)                    mutex_unlock(&done_lock)
```

Here, we have a two threads, ThreadA and ThreadB:
- ThreadB waits ThreadA is done with its work.
- We need three things to work with:
    - is_done flag indicating, some thread is done with working.
    - Lock that can be applied to the variable to protect the other thread reaching to critical section of code.
    - And a conditional wait variable.
- When A is done with doing some work:
    - A acquires a lock
    - Inticates that it is done with doing some work on its side.
    - Sends a signal to anyone waiting on the condition.
    - Then unlock the lock
- For the ThreadB part
    - B first acquires a lock
    - Checks to see if the work is done, if is isnt it keeps waiting, here its important that ``cond_wait`` not only makes 
      threadB wait but it also unlocks the mutex. This will allow threadA to acquire the lock and send the signal. 
      The call blocks untill the signal is recieved and threadB acquires a lock again. Hence its needed to unlock at the end.


**Key Concept With Pythonic Implementation:**

- **1. Condition variable:**
    - A condition variable allows threads to wait until a certain condition becomes true.

    - It is associated with a lock, so only one thread can access the shared resource at any given time.

- **2. Locking Mechanism:**
    - When creating a Condition object, a lock (either a Lock or RLock) is implicitly created if not provided.

    - This lock ensures that only one thread can enter the critical section protected by the condition at a time.

- **3. Wait and Notify:**
    - Wait: A thread can wait for a condition to be met. While waiting, it releases the lock associated with the condition and enters a suspended state until another thread notifies it.

    - Notify: Another thread, after making the condition true, can call notify() to wake one of the waiting threads or notify_all() to wake all waiting threads.





A condition object has acquire() and release() methods that call the corresponding methods of the associated lock. It also has a wait() method, and notify() and notifyAll() methods. These three must only be called after the calling thread has acquired the lock.

**Condition Class Method:**

- ``acquire(*args)`` This method is used to acquire the lock. This method calls the corresponding acquire() method on the underlying lock present in the condition object; The return value is whatever that method returns.

- ``release()`` this method is used to release the lock. This method calls the corresponding release() method on the underlying lock present in the condition object.

- ``notify()`` It wakes up any thread waiting on the corresponding condition. This must only be called when the calling thread has acquired the lock. Also, calling this method will wake only one waiting thread. The threads are moved from a waiting to a runnable state but can only proceed once they reacquire the lock.

- ``notifyAll()`` It wakes up all the threads waiting on this condition. This method acts like notify() method, but wakes up all the waiting threads instead of one.

- ``wait([timeout])`` This method is used to block the thread and make it wait until some other thread notifies it by calling the ``notify()`` or ``notifyAll()`` method on the same condition object or until the timeout occurs. This must only be called when the calling thread has acquired the lock. When called, this method releases the lock and then blocks the thread until it is awakened by a ``notify()`` or ``notifyAll()`` call for the same condition variable from some other thread, or until the timeout occurs. This method returns True if it is released because of ``notify()`` or ``notifyAll()`` method else if timeout occurs this method will return False boolean value.

**Example:**

- Create two different classes - inherit from thread class.

- Publisher class:
    - Publish new integers to integer array
    - Notify to subscriber

- Subscriber class:
    - New integer to be consumed from array

```python
import threading
import random
import time


class Publisher(threading.Thread):

    def __init__(self, integers, condition, name):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self, name=name)
    
    def run(self):
        """
        Publisher acquires a condition, appends integer, notifies and releases
        """
        for i in range(1, 3):
            integer = random.randint(0, 1000)
            self.condition.acquire()
            print(f"Condition Acquired by Publisher: {self.name}")
            self.integers.append(integer)
            print(f"Publisher {self.name} appending {integer} to array.")
            self.condition.notify()
            print(f"Condition released by publisher: {self.name}")
            self.condition.release()
            time.sleep(1)


class Subscriber(threading.Thread):

    def __init__(self, integers, condition, name):
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self, name=name)
    
    def run(self):
        """
        Subscriber 
        """
        while True:
            self.condition.acquire()
            print(f"Condition acquired by Consumer: {self.name}")
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print(f"{integer} Popped from list by consumer: {self.name}")
                    break

                print(f"Condition wait by: {self.name}")
                self.condition.wait()
            print(f"Consumer {self.name} Releasing condition.")
            self.condition.release()

def main():
    integers = []
    condition = threading.Condition()

    pub1 = Publisher(integers=integers, condition=condition, name="Publisher1")
    pub1.start()

    sub1 = Subscriber(integers=integers, condition=condition, name="Subscriber1")
    sub2 = Subscriber(integers=integers, condition=condition, name="Subscriber2")
    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()

if __name__ == "__main__":
    main()
```

In the above code, we've a producer generating a three random numbers, which are to be consumer by the subscriber.

**Producer:**
- Acquires a condition.

- Appends a random integer.

- Notifies a thread waiting on corresponding condition. calling this method will wake only one waiting thread.

- Releases the condition.

**Subscriber:**
- Infinitely is listening, to get notified by the producer.
- Acquires a lock
- If new integer is seen.
- Gets the new integer value pushed by producer.
- Waits on a condition
- Reelease the condition


**Output:**

```sh
# Output
Condition Acquired by Publisher: Publisher1
Publisher Publisher1 appending 477 to array.
Condition released by publisher: Publisher1
Condition acquired by Consumer: Subscriber1
477 Popped from list by consumer: Subscriber1
Consumer Subscriber1 Releasing condition.
Condition acquired by Consumer: Subscriber1
Condition wait by: Subscriber1
Condition acquired by Consumer: Subscriber2
Condition wait by: Subscriber2
Condition Acquired by Publisher: Publisher1
Publisher Publisher1 appending 710 to array.
Condition released by publisher: Publisher1
710 Popped from list by consumer: Subscriber1
Consumer Subscriber1 Releasing condition.
Condition acquired by Consumer: Subscriber1
Condition wait by: Subscriber1
```
