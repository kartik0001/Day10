# Q3

from threading import *
from time import *


def displayListElements(l1):
    print('Displaying all elements of the list with delay: ')
    j = 0
    for i in range(2, 11, 2):
        print(l1[j])
        print('Going to sleep for {} seconds'.format(i))
        sleep(i)
        j += 1


l1 = ['Microsoft Buys','World\'s', 'Largest Coding','Platform','Github']
print('The complete list is as follows:\n{}'.format(l1))
t = Thread(target=displayListElements, args=(l1,))
t.start()
t.join()
print('Thank You')

