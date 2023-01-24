import pywhatkit as zap
from time import sleep

ent = str(input('Numero: '))
num = '+5584'+ent

msg = str(input('Msg a ser enviada: '))

hr = int(input('Hora: '))
min = int(input('Min: '))

for i in range(5):
    zap.sendwhatmsg(num, msg, hr, min)
    sleep(1)
    min = min + 2
    sleep(1)
