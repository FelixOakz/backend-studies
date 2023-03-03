def voto(nasc):
	from datetime import date
	age = date.today().year - nasc
	if age < 16:
		return f'Com {age} anos: NAO VOTA.'
	elif 16 <= age < 18 or age > 65:
		return f'Com {age} anos: VOTO OPCIONAL.'
	else:
		return f'Com {age} anos: VOTO OBRIGATORIO.'

r = int(input('Que ano vc nasceu?: '))
print(voto(r))
