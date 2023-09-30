#1-----------------------------
num1=45
num2=18
if num1>num2:
    print(f'O numero {num1} é maior e o {num2} é menor')
#2-----------------------------
idade=int(input("Digite sua idade para poder entrar no show:"))
if idade>=18:
    print('Liberado')
else:
    print('Bloqueado')

#3-----------------------------
n1= float(input("Digite a nota 1: "))
n2= float(input("Digite a nota 2: "))
n3= float(input("Digite a nota 3: "))
media=(n1+n2+n3)/3
if media>=5:
    print(f'A nota do aluno foi {media}, Aluno aprovado!!')
else:
    print(f'A nota do aluno foi {media}, Aluno reprovado!!')