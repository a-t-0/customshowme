import time
import customshowme
@customshowme.time
def some_example():
    for i in range(0,100000):
        something="new"
        if i == 100:
            print("Something inbetween that should be down.")
some_example()