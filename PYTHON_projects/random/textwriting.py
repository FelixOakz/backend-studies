import os

filepath = os.path.abspath('/Py-SQL-studies/random/TextDatabase.txt')

for i in range(1, 1001):
	file = open(filepath, 'a')
	file.write(f'teste numero {i}\n')
	file.close()

print('process finished')
