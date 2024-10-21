import threading
import urllib.request

import os
import shutil

import time

def clean_directory():
    # remove existing directory
    try:
        shutil.rmtree("images")
    except Exception:
        pass

    # create a directory to store images
    try:
        os.mkdir("images/")
    except Exception:
        pass

def downloadImage(imagePath, fileName):
    print("Downloading image from:", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Completed downloading image")

def executeThread(i):
    imageName = f"images/image-{i}.jpg"
    downloadImage("https://random-image-pepebigotes.vercel.app/api/random-image", imageName)

def main():
    clean_directory()

    t0 = time.time()

    # threads
    threads = []

    # create 10 threads of downloader, append them to array and start them off
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i, ))
        threads.append(thread)
        thread.start()

    # join the threads, i.e. wait untill completion
    for t in threads:
        t.join()
    
    t1 = time.time()

    total_time = t1 - t0

    print("Total Time Taken:", total_time)

if __name__ == "__main__":
    main()
