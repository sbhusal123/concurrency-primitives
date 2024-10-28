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
