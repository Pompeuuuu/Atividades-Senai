import random
valor = random.randint(1,1000)
print ('Bem vindo ao Banco sua conta báncaria tem: R$', valor,'!')
opcao = input('Escolha o método:\n [1] Deposito \n [2] Saque\n')
class Banco:
    def __init__(self,valor):
        self.valor = valor
    def deposito(self):
        deposito = int(input('Digite um valor para depositar'))
        valor += deposito
        return valor
    
    def saque(self):
        saque = int(input('Digite um valor para sacar'))
        if valor > saque:
            valor -= saque 
            return valor
        else:
            print('Valor insuficiente!') 
if opcao == '1':
    banco = Banco(valor)
    banco.deposito()
    print(f'Sua conta possui agora {valor}')
elif opcao == '2':
    banco = Banco(valor)
    banco.saque()
    print(f'Sua conta possui agora {valor}')
else:
    print('Opção Inválida!')
