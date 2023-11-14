import random
continuar = True
while continuar:
    valor = random.randint(1,1000)
    print(f'\nBem vindo ao Banco sua conta báncaria tem: R${valor}!')
    opcao = input('Escolha o método:\n [1] Deposito \n [2] Saque\n')
   
    class Banco:
        def __init__(self,valor):
            self.valor = valor
        def deposito(self):
            deposito = int(input('Digite um valor para depositar: '))
            print(f'Sua conta possui agora R${valor+deposito}!')
        
        def saque(self):
            saque = int(input('Digite um valor para sacar: '))
            if self.valor > saque:
                print(f'Sua conta possui agora R${valor-saque}')
            else:
                print('Valor insuficiente!') 
        def error(self):
            print('Opção Inválida!')

    if opcao == '1':
        banco = Banco(valor)
        banco.deposito()
    elif opcao == '2':
        banco = Banco(valor)
        banco.saque()
    else:
        banco = Banco(valor)
        banco.error()
        if opcao == '1':
            banco = Banco(valor)
            banco.deposito()
        elif opcao == '2':
            banco = Banco(valor)
            banco.saque()

    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        continuar = False
        print('\nObrigado por usar nossos serviços!')
    elif continuar == 'S':
        continuar = True
    else:
        banco = Banco(valor)
        banco.error()
