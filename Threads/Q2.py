#Q2

from threading import *
from time import *
def display():
    print('Value of 1-10 in interval of 1 second')
    for i in range(1,11):
        sleep(1)
        print(i)


t=Thread(target=display)
t.start()



