n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
socks = []
pair = 0

for i in ar:
	if i not in socks:
		socks.append(i)
	else:
		socks.remove(i)
		pair += 1
	print(socks)
print(pair)
