# num = 11
# while num > 1:
#     num -= 1
#     print(num)
# print("Fogo!!!!")


insert_number = int(input("Insira um numero par:"))
cont=0
while cont < insert_number:
     if cont < insert_number:
       for cont in range(0,insert_number,2):
           print(cont)
           soma=sum(cont)
       else:      
           print(f'A soma do numéro é {soma}')
           break