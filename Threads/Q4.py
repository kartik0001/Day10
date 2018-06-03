#Q4

from threading import *
from time import *
from math import *

def displayFactorial(l1):
    print('Displaying factorial using thread: ')

    for i in range(len(l1)):
        print("The factorial of {} = {}".format(l1[i], factorial(l1[i])))
        sleep(3)


l1 = [1, 2, 3, 4]
print('The complete list is:\n{}'.format(l1))
t = Thread(target=displayFactorial, args=(l1,))
t.start()
t.join()
print('Thank You')
