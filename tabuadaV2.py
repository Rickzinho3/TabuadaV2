#tabuada - v2.0

import time
import os

#cores
class colors:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'
    
#definindo função    
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
while True:
    devo_comecar = input(colors.white + 'Pressione ENTER para começar \nou digite [s] para sair: ' + colors.end)
    if devo_comecar == '':
        print(' ')
        break
    elif devo_comecar == 's':
        print('')
        print('saindo')
        time.sleep(1)
        print('limpando terminal...')
        time.sleep(1)
        limpar()
        time.sleep(1)
        exit()
    else:
        print('Opção Inválida.')
    
while True:
	n = int(input(colors.white + 'Um número de 1 a 10 [ou 14 para sair]: ' + colors.end))
	print(' ')
	print(colors.yellow + 'processando...' + colors.end)
	time.sleep(1)
	print(' ')
	
	if n == 14:
	    print('saindo')
	    time.sleep(1)
	    print('limpando terminal...')
	    time.sleep(1)
	    limpar()
	    exit()
	elif n < 1:
		print(colors.red + 'Número mínimo permitido: 1' + colors.end)
		print('')
		continue 
	elif n > 10:
	    print(colors.red + 'Número máximo permitido: 10.' + colors.end)
	    print(' ')
	    continue
	
	for c in range(1, 11):
		time.sleep(0.1)
		print(colors.white + f'{n} x {c} = {n*c}' + colors.end)
	
	print(' ')
