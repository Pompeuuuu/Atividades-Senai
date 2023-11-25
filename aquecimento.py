# 1
# def quadrado(number): 
#         total = number*number
#         print(f'O resultado do quadrado é : {total}')
# try:
#     number = float(input('Digite um numero:'))
#     if number == 0:
#         raise ValueError('O numero nnão pode ser zero!')
#     elif number < 0:
#         raise ValueError('O numero não pode ser negativo!')   
#     elif number.is_integer():
#         quadrado(number)
#     else:
#         raise ValueError('O número não é inteiro')  
# except ValueError as e:
#      print(f'Error:{e}')

# #2
# def soma(number1,number2): 
#         total = number1+number2
#         print(f'O resultado da soma é : {total}')
# try:
#     number1 = float(input('Digite um numero:'))
#     number2 = float(input('Digite outro numero:')) 
#     if number1.is_integer() and number2.is_integer():
#         soma(number1,number2)
#     else:
#         raise ValueError('O número não é inteiro')  
# except ValueError as e:
#      print(f'Error:{e}')

#3
# import math
# def fatorial(number):
#         print(f'O fatorial é: {math.factorial(number)}')
# try:
#     try:
#         number = int(input('Digite um numero:'))
#         if number < 0:
#             raise ValueError('O numero não pode ser negativo')
#         elif number == 0:
#             raise ValueError('O numero não poder ser 0')
#         else:
#           fatorial(number)
#     except BaseException:
#         print('O numero tem que ser inteiro!')
# except ValueError as e:
#      print(f'Error:{e}')


#4
def primo(number):
    for i in range (2, int(number**0.5)+1):
        if number % i ==0:
            return False
    return True

def proximo_primo(number):
    prox_primo = number + 1
    while True:
        if primo(prox_primo):
            return prox_primo
        prox_primo += 1
try:
    entrada = int(input('Digite um numero:'))
except BaseException:
    print('Digite um numero inteiro!') 
    exit()
try:
    if entrada < 2:
         raise ValueError('O numero não pode ser menor que 2')
    else:
        res =  proximo_primo(entrada)
        print(f'O proximo numero primo é {res}')
except ValueError as e:
     print(f'Error:{e}')

#5
# def texto(fala): 
#         tamanho = len(fala)
#         print(f'O tamanho da palavra é: {tamanho}')
# try:
#     fala = input('Digite uma palavra:')
#     if fala =="":
#         raise ValueError('Digite uma frase!')
#     else:
#         texto(fala)
# except ValueError as e:
#      print(f'Error:{e}')