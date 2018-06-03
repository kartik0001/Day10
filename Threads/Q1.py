# Q1

from threading import *
import time
def display():
    print('Starting Process And Waiting for 5 seconds\n')
    time.sleep(5)
    print('5 seconds up.Process End')

print('Starting Main Thread\n')
t=Thread(target=display)
t.start()
t.join()
print('Back in Main thread')

