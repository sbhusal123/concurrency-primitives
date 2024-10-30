# Semaphore and BoundedSemaphore

## Semaphore:

- Have an internal counter (representing the number of resource), that is increased when it's acquired and decreanted when released.

- Multiple threads can acquire a semaphore.

- If semaphore value falls to negative, cannot acquire a semaphore further.


> Suppose, we protected a block of code with semaphore, and set it's value to 2. Then a threadA acquring it, sets it value to 1. If threadB tries to access it, sets it value to 0. So, with semaphore initialized with 2, the section of code or resource can only be accessed by 2 of the threads at a time. At this point if, threadC further tries to acquire it, semaphore would deny the request untill any of  threads acquiring releases it or semaphore counter increaments to more than 0.

## Semaphore in Python

```python
class Semaphore:
    """This class implements semaphore objects.

    Semaphores manage a counter representing the number of release() calls minus
    the number of acquire() calls, plus an initial value. The acquire() method
    blocks if necessary until it can return without making the counter
    negative. If not given, value defaults to 1.

    """

    # After Tim Peters' semaphore class, but not quite the same (no maximum)

    def __init__(self, value=1):
        if value < 0:
            raise ValueError("semaphore initial value must be >= 0")
        self._cond = Condition(Lock())
        self._value = value
```

- Accepts initial value, by default set to 1.

**Semaphore Methods:**

- Two methods:
    - ``<semaphore>.acquire()`` to acquire a semaphore.
    - ``<semaphore>.release()`` to release a semaphore.

- If the initial value of semaphore is 2.
    - Threads can acquire a semaphore for 2 times.
    - While they can release it multiple.

i.e. Following piece of code is valid:

```python
semaphore = threading.Semaphore(value=1)
# once acquired, cannot be required
semaphore.acquire() # value = 0

# semaphore.acquire() would be a blocking call here

semaphore.release() # value=1 
semaphore.release() # value=2
semaphore.release() # value=3
```

> **Caveats:** Here, while releasing the lock, the semaphore value can exceed the initial value. But that's not the case in BoundedSemaphore.
> Only to be used in case where, acquring a resource is a major concern and releasing is not a major concern.


## Example: Ticket Selling Program:

- Four threads as a seller.

- Each try to sell as many tickets as possible.

```python
import threading
import time
import random

class TicketSeller(threading.Thread):

    ticketSold = 0

    def __init__(self, semaphore, name):
        threading.Thread.__init__(self, name=name)
        self.semaphore = semaphore
        print(f"Ticket Seller:{name} Started Working")
    
    def randomDelay(self):
        """For some delay"""
        time.sleep(random.randint(0,4))
    
    def run(self):
        global ticketsAvailable
        runing = True
        thread_name = threading.current_thread().name
        while runing:
            # if removed, possibly all tickets will be sold by single thread.
            self.randomDelay()

            self.semaphore.acquire()
            if ticketsAvailable <= 0:
                runing = False
            else:
                self.ticketSold = self.ticketSold + 1
                ticketsAvailable =  ticketsAvailable - 1
                print(f"{thread_name} sold 1 ticket ({ticketsAvailable} left)")
            self.semaphore.release()
        
        print(f"Ticket seller {thread_name} sold {self.ticketSold} in total")

ticketsAvailable = 20
def main():
    semaphore = threading.Semaphore()

    sellers = []
    for i in range(0, 4):
        ticket_seller = TicketSeller(semaphore=semaphore, name=f"Seller{i}")
        ticket_seller.start()
        sellers.append(ticket_seller)
    
    for seller in sellers:
        seller.join()

if __name__ == "__main__":
    main()
```

```sh
# Output
Ticket Seller:Seller0 Started Working
Ticket Seller:Seller1 Started Working
Ticket Seller:Seller2 Started Working
Seller1 sold 1 ticket (19 left)
Ticket Seller:Seller3 Started Working
Seller2 sold 1 ticket (18 left)
Seller1 sold 1 ticket (17 left)
Seller0 sold 1 ticket (16 left)
Seller1 sold 1 ticket (15 left)
Seller0 sold 1 ticket (14 left)
Seller3 sold 1 ticket (13 left)
Seller1 sold 1 ticket (12 left)
Seller1 sold 1 ticket (11 left)
Seller1 sold 1 ticket (10 left)
Seller0 sold 1 ticket (9 left)
Seller2 sold 1 ticket (8 left)
Seller1 sold 1 ticket (7 left)
Seller3 sold 1 ticket (6 left)
Seller3 sold 1 ticket (5 left)
Seller3 sold 1 ticket (4 left)
Seller3 sold 1 ticket (3 left)
Seller2 sold 1 ticket (2 left)
Seller3 sold 1 ticket (1 left)
Seller0 sold 1 ticket (0 left)
Ticket seller Seller1 sold 7 in total
Ticket seller Seller3 sold 6 in total
Ticket seller Seller2 sold 3 in total
Ticket seller Seller0 sold 4 in total
```

Here we have:
- 4 threads acting as a tcket seller.
- Semaphore is initialized to 1 by default.
- Global variable ticketsAvailable as a placeholder for storing no of tickets.
- 20 tickets available in stock.
- Each seller when decreasing a number of tickets, they first acquire a semaphore, after selling (or decreasing) release it.
- Note that we have a randomSleep to simulate some reallife delay.
