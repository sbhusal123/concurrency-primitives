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
        time.sleep(random.randint(0,4))
    
    def run(self):
        global ticketsAvailable
        runing = True
        thread_name = threading.current_thread().name
        while runing:
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
    
    print(semaphore)

if __name__ == "__main__":
    main()
