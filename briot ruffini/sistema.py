
from time import sleep

coeficientes = []
resultado = []

grau = int(input('Digite qual é o grau da sua equação: '))

print('Digite agora os coeficientes numéricos da sua F(x): \n')

for c in range(grau, -1, -1):
    coeficientes.append(int(input(f'coeficiente de x no grau {c}: ')))

raiz = float(input('\nDigite o valor de x que você deseja dividir o polinômio: '))

print('Fazendo os cálculos...')
sleep(2)

resu = coeficientes[0]

for i, v in enumerate(coeficientes):
    if i == 0:
        resultado.append(resu)
    else:
        resu = resu * raiz + v
        resultado.append(resu)

print('\nOs coeficientes do polinômio que resultou da divisão foram: \n')
c = len(resultado) - 1
for i, v in enumerate(resultado):
    if i == len(resultado) - 1:
        print(f'E \033[31mresto\033[m da divisão foi: {v}')
    else:
        
        print(f'Coeficiente de grau {c}: {v}')
        c = c - 1

print('\n')
