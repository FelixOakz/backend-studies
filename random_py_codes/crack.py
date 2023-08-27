'''from string import digits
# giving access to all ascii characters, decimal digits and punctuation marks
from itertools import product
# habillity to cross product of all numbers

passwd = int(input('Enter the 4 digit password: '))


for passcode in product(digits, repeat=4):

	print(*passcode)
'''
import itertools
import time

'''
map() converts our input into integers to match the type of the contents of 'a' 
and tuple() makes it a tuple to match the type of combinations.
'''

password = tuple(map(int, input('Enter 4 digit password: ')))

digits = list(range(0, 10))
start_time = time.time()

for passcode in itertools.product(digits, repeat=6):
    print(f"-> {passcode} ")
    if passcode == password:
        print("\n\n-----> The password is: " + ''.join(str(i) for i in password))
        break

execution_time = time.time() - start_time

formatted_seconds = "{:.5f}".format(execution_time)

print(f'\nThe execution time in seconds is: {formatted_seconds} seconds')