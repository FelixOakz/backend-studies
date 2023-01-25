# accept text as string from user
text = str(input('Text: ')).upper()
letters = sentences = 0
words = 1

#counting leters, using isalpha function from cs50 manuals
for i in range(len(text)):
	if text[i] >= 'A' and text[i] <= 'Z':
		letters += 1
	elif text[i] == ' ':
		words += 1
	elif text[i] == '.' or text[i] == '?' or text[i] == '!':
		sentences += 1

# using given formula to calculate score
S = float(sentences) / words * 100
L = float(letters) / words * 100

g = (0.0588 * float(L)) - (0.296 * float(S)) - 15.8
grade = round(g)

# printing result according to computed score
if grade < 1:
	print('Before grade 1.')
elif grade > 16:
	print('Grade 16+.')
else:
	print(f'Grade {grade}.')
