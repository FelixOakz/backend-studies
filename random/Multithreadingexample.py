from threading import *
import threading
from time import sleep

lock = threading.Lock()

class Example(Thread):
   def run(self):
       for i in range(5):
           lock.acquire()
           print('Lock 1 acquired')
           print("Hello from Example")
           sleep(1)
           lock.release()


class ExampleTwo(Thread):
   def run(self):
       for i in range(5):
           lock.acquire()
           print("Hello from ExampleTwo")
           print('Lock 2 acquired')
           sleep(1)
           lock.release()


example = Example()
exampleTwo = ExampleTwo()
example.start()
sleep(.1)
exampleTwo.start()