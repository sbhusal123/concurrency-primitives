import urllib.request
import time

import os
import shutil

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
    print("Downloading image from :", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)


def main():
    clean_directory()

    t0 = time.time()
    for i in range(10):
        imageName = "images/image-" + str(i) + ".jpg"
        downloadImage("https://random-image-pepebigotes.vercel.app/api/random-image", imageName)

    t1 = time.time()

    total_time = t1 - t0

    print("Total Execution Time {}".format(total_time))

if __name__ == '__main__':
    main()
