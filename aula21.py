# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    num1 = int(input("Digite um número: "))
except ValueError:
    print("Erro: Digite números inteiros.")
else:
    print("O seu numero é",num1)


# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação.

try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Digite números válidos.")
else:
    print("O resultado é:", resultado)


# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido.


# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.