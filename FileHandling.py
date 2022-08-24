import os

filepath = os.path.abspath('Documents/emailvagas.txt')

file = open(filepath, 'r')
print(file.read())

