
'''from string import digits
# giving access to all ascii characters, decimal digits and punctuation marks
from itertools import product
# habillity to cross product of all numbers

passwd = int(input('Enter the 4 digit password: '))


for passcode in product(digits, repeat=4):

	print(*passcode)
'''
import itertools


'''
map() converts our input into integers to match the type of the contents of 'a' 
and tuple() makes it a tuple to match the type of combinations.
'''

password = tuple(map(int, input('Enter 4 digit password: ')))

digits = list(range(0, 9))

for passcode in itertools.product(digits, repeat=4):
    if passcode == password:
        print("The password is: " + ''.join(str(i) for i in password))
