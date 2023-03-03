scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

min = max = scores[0]
cmax = cmin = 0
for i in scores:
	if i > max:
		max = i
		cmax += 1
	elif i < min:
		min = i
		cmin += 1
scores.clear()
scores.append(cmax)
scores.append(cmin)
print(scores)
