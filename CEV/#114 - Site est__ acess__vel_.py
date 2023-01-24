import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except:
	print('Sem conexao')
else:
	print('conectando normalmente')


# conteudo inteiro do site: site.read()
