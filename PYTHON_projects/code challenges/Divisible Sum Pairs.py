k = 3
n = 6
ar = [1, 3, 2, 6, 1, 2]

pair = 0
for i in range(n):
	for j in range(n):
		if i < j and (ar[i] + ar[j]) % k == 0:
			pair += 1

print(pair)
