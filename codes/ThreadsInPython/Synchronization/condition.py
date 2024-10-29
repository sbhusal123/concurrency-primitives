import threading
import random
import time


class Publisher(threading.Thread):

    def __init__(self, integers, condition):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)
    
    def run(self):
        """
        Publisher acquires a condition, appends integer, notifies and releases
        """
        while True:
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

    def __init__(self, integers, condition):
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self)
    
    def run(self):
        """
        Subscriber 
        """
        while True:
            self.condition.acquire()
            print(f"Condition acquired by Consumer: {self.name}")
            while True:
                if self.integers:
                    integers = self.integers.pop()
                    print(f"{self.integers} Popped from list by consumer: {self.name}")
                    break

                print(f"Condition wait by: {self.name}")
                self.condition.wait()
            print(f"Consumer {self.name} Releasing condition.")
            self.condition.release()

def main():
    pass
