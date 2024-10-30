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
