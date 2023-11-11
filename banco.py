import math
import random
saldo = random.randint(1000,10000)
print('\nBem vindo ao aplicativo do banco!\n')
print(f'Você possui R${saldo}!\n')
choise = int(input('[1] Depositar\n[2] Retirar saldo\n'))
if choise == 1:
    deposito =float(input('Digite o valor:'))
    saldo += deposito
    print(f'Você possui R${saldo}!')
elif choise == 2:
    saque = float(input('Digite o valor:'))
    saldo -= saque
    print(f'Você possui R${saldo}!')
else:
    print('Opção inválida!')
loop()