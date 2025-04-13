# Events

- Object that:
    - Features two internal flag that is either true or false.

- In threads:
    - Continously poll event object - to check its state
    - Choose the action according to state.

**Methods of Event**

- **set():** Sets the internal flag to true. All threads waiting for the flag to be set are notified.

- **clear():** Clears the internal flag to false. Threads that call wait() will block until the flag is set again.

- **wait(timeout=None):** Blocks until the internal flag is true. If the flag is already true, it returns immediately. If a timeout is specified, it will wait at most timeout seconds for the flag to be set.

- **is_set():** Returns the current state of the internal flag.


```python
import threading
import time

def worker(event, timeout):
    print("Worker started, waiting for event...")
    event_occurred = event.wait(timeout)
    if event_occurred:
        print("Event occurred, proceeding...")
    else:
        print("Timeout reached, proceeding without event...")

event = threading.Event()

# Create and start a worker thread
worker_thread = threading.Thread(target=worker, args=(event, 5))
worker_thread.start()

# Simulate some work in the main thread
time.sleep(2)

# Set the event to notify the worker thread
print("Main thread setting the event...")
event.set()

# Wait for the worker thread to complete
worker_thread.join()

print("Worker thread has finished.")
```

**Example2: Cars waiting for Traffic Light To Turn Blue:**

```python
import threading
import time

class Car(threading.Thread):

    def __init__(self, name, event, *args, **kwargs):
        self.event = event
        threading.Thread.__init__(self, name=name, *args, **kwargs)
        print(f"Car-{self.name} waiting for light to turn blue...")
    
    def is_light_blue(self):
        return self.event.wait()
    
    def run(self):
        if self.is_light_blue():
            print(f"Car-{self.name} moving..")


event = threading.Event()
cars = [ ]

def countdown(seconds):
    """Performs countdown to seconds and sets event"""
    print(f"Waiting {seconds} seconds to turn light blue.")
    for s in range(0, seconds):
        print(f"{seconds-s}...")
        time.sleep(1)
    event.set()

for i in range(0,5):
    car = Car(name=f"{i}", event=event)
    cars.append(car)

for car in cars:
    car.start()

countdown(5)

for car in cars:
    car.join()
```

