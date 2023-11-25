# n1= 10
# n2= 0
# try:
#     total = n1/n2
#     print(total)
# except ZeroDivisionError:
#     print('Não pode dividir por zero!!!!')


# def divisao(a,b)
#     try: 
#         total = a/b
#         return total
#     except ZeroDivisionError
#         return None
# resultado = divisao (10,0)
# if resultado is not None:
#     print(f'Resultado é {resultado}')
# else:
#     print('Não pode dividir por zero!!!!')


# def divisao(a,b)
#     if(b == 0):
#         raise ZeroDivisionError ('Não pode dividir por zero')
#     else 
#         total = a/b
#         print (total)
# try:
#     divisao(4,2)
# except ZeroDivisionError as e:
#     print(f'Calculo não permitido:{e}')


def validaIdade(idade):
    if (idade>=18):
        print('Maior de idade')
    elif (idade > 0 and idade < 18):
        print('Menor de idade')
    elif (idade<0):
        raise ValueError('Idade nao pode ser negativa')
    else:
        raise ValueError('Idade não pode ser zero!!')
try:
    idade = ('Digite sua idade:')
    if idade.is_integer():
        validaIdade(idade)
    elif idade == str:
        raise ValueError('Idade nao pode ser letra!')
    else:
        raise ValueError('Idade tem que ser inteira!')
except ValueError as e:
    print(f'Error:{e}')