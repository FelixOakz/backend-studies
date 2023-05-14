import re as regularexpressions

s = input('Do you agree?: ').lower()
if regularexpressions.search("^y(es)?$", s):
	print('Agreed.')
elif regularexpressions.search("^no?$", s):
	print("Not agreed.")

# take a look at the cs50 doc