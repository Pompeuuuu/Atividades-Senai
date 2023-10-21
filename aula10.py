# def somalist():
#     numero=int(input('numero:'))
#     soma = 0
#     for lista in range(1,numero+1):
#         soma += lista
#     print(soma)
# somalist()

# def contar_letra(palavra,letra):    
#     contador = 0
#     for char in palavra:
#            if char == letra:
#                 contador += 1
#     print("Tem essa quantidade na palavra", contador)
# achados = contar_letra('abracadaba','a'),

n = int(input('fat: '))
res=1
count=1
while count<=n:
    res*=count
    count+=1
print(res)