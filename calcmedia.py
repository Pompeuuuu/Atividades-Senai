n1=float(input("Digite a nota 1:"))
n2=float(input("Digite a nota 2:"))
n3=float(input("Digite a nota 3:"))
media=(n1+n2+n3)/3
if  media >=7:
    print(f"Aluno aprovado \n Nota:{media}")
elif  media >=5:
    print(f"Aluno esta de recuperação \n Nota:{media}")
else:
    print(f"Aluno reprovado \n Nota:{media}")