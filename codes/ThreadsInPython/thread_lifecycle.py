import threading

import time

def threadWorker():
    # it is the only at the point where the thread starts
    # here it goes from runnable to runing state

    print("Thread has entered the runing state")

    # if we perform some waiting, goes into not-runnable state.
    time.sleep(5)

    # Entered into the runing state again
    print("Thread ws paused and again entered the runing state")

    # nothing further to procede with, dead now

# at this point, thread has no state,hasn't been allocated any resources
myThread = threading.Thread(target=threadWorker)

# call to .start() method allocates the necessary resources in order
# for threads to run
# Note that Here, it goes from Starting to Runnable state but not runing
# only goes into runing state when target function is invoked
myThread.start()

# here we join the thread to our main process,
myThread.join()
