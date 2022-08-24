from threading import *

class Example(Thread):
    def run(self):
        for i in range(1000):
            print("Hello from Example")


class ExampleTwo(Thread):
    def run(self):
        for i in range(1000):
            print("Hello from ExampleTwo")


example = Example()
exampleTwo = ExampleTwo()
example.run()
exampleTwo.run()
