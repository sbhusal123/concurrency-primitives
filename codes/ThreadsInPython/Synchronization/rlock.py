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