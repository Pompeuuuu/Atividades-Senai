# 1
# numeros = int(input('Digite um numero:'))
# dobro = lambda x: x * 2
# print('O dobro é', dobro(numeros))

# 2
# numero1 = int(input('Digite o 1 numero:'))
# numero2 = int(input('Digite o 2 numero:'))
# soma = lambda x : x
# print('A soma é', soma(numero1+numero2))

#3
# numero = int(input('Digite o numero:'))
# soma = lambda x : x % 2==0
# if soma(numero) == True:
#     print(f'O {numero} é par')
# else:
#     print(f'O {numero} é impar')

#4
# texto = input('Digite:')
# maiusculo = lambda x:x
# print(maiusculo(texto.upper()))

# 5
from functools import reduce
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite mais um numero:'))
numeros = [n1, n2, n3]
prod = reduce(lambda x, y : x * y, numeros)
print(prod)
