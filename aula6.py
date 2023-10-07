num= [7,2,3,5,1]
print(num)
print(num[2])
num.append(6)
num.remove(5)
print(num)

frutas = ['masa','morajo','marajuca']
print(frutas+num)

for i in frutas:
    print(i)
for verifica in num:
 if verifica == 5:
    print('O 5 É REAL!!!')
 else:
    print('O 5 É OS AMIGOS QUE FIZEMOS PELO CAMINHO')