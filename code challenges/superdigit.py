n = str(input('enter n: '))
k = int(input('enter k: '))
p = n * k
p = int(p)
while p > 9:
	p = sum(map(int, str(p)))
print(p)