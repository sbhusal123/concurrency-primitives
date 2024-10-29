import threading
import time


class Worker:

    def __init__(self) -> None:
        self.a = 1
        self.b = 1
        self.rlock = threading.RLock()

    def increament_a(self):
        self.rlock.acquire()
        print(f"Modifying A: RLock Acquired: {self.rlock}")
        self.a = self.a + 1
        time.sleep(1)
        self.rlock.release()
        print(f"Modifying A: RLock Released: {self.rlock}")

    def increament_b(self):
        self.rlock.acquire()
        print(f"Modifying A: RLock Acquired: {self.rlock}")
        self.b = self.b + 1
        time.sleep(1)
        self.rlock.release()
        print(f"Modifying A: RLock Released: {self.rlock}")

    def increament_both(self):
        self.rlock.acquire()
        print(f"RLock acquired, modifying A and B: {self.rlock}")
        self.increament_a()
        self.increament_b()
        self.rlock.release()
        print(f"RLock released, modifying A and B: {self.rlock}")

worker = Worker()
worker.increament_both()
