import csv
# with the opening of this file as a variable called file
with open('csvtest.csv', 'a') as file:
	team = input('Team: ')
	score = input('Number: ')

	writer = csv.DictWriter(file, fieldnames=['team', 'score'])
	writer.writerow({'team': team, 'score': score})

# file.close() would be here, but with keyword maked is redundant
