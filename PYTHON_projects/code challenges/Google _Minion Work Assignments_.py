def solution(data, n):
	ndata = []
	for i in data:
		if data.count(i) <= n:
			ndata.append(i)
	return ndata
