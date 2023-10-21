operador = input('Digite o operador:(+,-,*,/)')
number1 = float(input('Digite o primeiro numero:'))
number2 = float(input('Digite o segundo numero:'))
def calc(calculo):
    if operador == "+":
        calculo = (number1 + number2)
        return calculo
    elif operador == "-":
        calculo =(number1 - number2)
        return calculo
    elif operador == '*':
        calculo =(number1 * number2)
        return calculo
    elif operador == '/' and number2 != 0:
        calculo = (number1 / number2)
        return calculo
    else:
        print('Numero ou operador invalido!')
print(calc(3))
