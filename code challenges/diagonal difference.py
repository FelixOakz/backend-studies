#      [0] [1] [2]
arr = [[11, 2, 4],		# [0]
		[4, 5, 6],		# [1]
		[10, 8, -12]]	#[2]

n = 3
primd = secd = 0
for i in range(n):
	primd += arr[i][i]
	secd += arr[n - i - 1][i]
print(abs(primd - secd))