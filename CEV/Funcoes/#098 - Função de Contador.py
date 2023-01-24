from time import sleep

def counter(start, end, step):
	print(f'Couting from {start} til {end} stepping {step}.')
	sleep(1)
	if start < end:
		count = start
		while count <= end:
			print(f'{count} ', end='- ')
			sleep(.5)
			count += step
		print('end.')
	else:
		count = start
		while count >= end:
			print(f'{count} ', end='- ')
			sleep(.5)
			count -= step
		print('end.')

counter(1, 10, 1)
counter(10, 0, 2)
print('now choose how the counter will work:')
st = int(input('Starting number:'))
en = int(input('Ending number: '))
ste = int(input('Steping number: '))
counter(st, en, ste)
