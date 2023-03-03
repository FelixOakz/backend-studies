def notas(*n, sit=False):
	"""
	-> funcao para analisar notas e situacoes de varios alunos
	:param not: uma ou mais notas dos alunos
	:param sit: valor opcional para indicar situacao
	:return: dicionario com varias infos
	"""
	r = {}
	r['Total'] = len(n)
	r['Maior'] = max(n)
	r['Menor'] = min(n)
	r['Media'] = sum(n)/len(n)
	if sit:
		if r['Media'] >= 7:
			r['situação'] = 'BOA'
		elif r['Media'] >= 5:
				r['situacao'] = 'RAZOÁVEL'
		else:
			r['situação'] = 'RUIM'
	return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)