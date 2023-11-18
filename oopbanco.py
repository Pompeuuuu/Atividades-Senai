import random
continuar = True
valor = random.randint(1,1000)
while continuar:
    deposito=0
    saque=0
    print(f'\nBem vindo ao Banco sua conta báncaria tem: R${valor}!')
    opcao = input('Escolha o método:\n [1] Deposito \n [2] Saque\n')
    class Banco:
        def __init__(self,valor):
            self.valor = valor

        def deposito(self):
            global deposito
            deposito = int(input('Digite um valor para depositar: '))
            self.valor += deposito
            print(f'Transferencia realizada com sucesso!!')

        
        def saque(self):
            global saque
            saque = int(input('Digite um valor para sacar: '))
            if self.valor > saque:
                self.valor -= saque
                print(f'Transferencia realizada com sucesso!!')
            else:
                print('Valor insuficiente!') 
                saque = 0

        def error(self):
            print('Opção Inválida!')

    banco = Banco(valor)
    if opcao == '1':
        banco.deposito()
    elif opcao == '2':
        banco.saque()
    else:
        banco.error()
        if opcao == '1':
            banco.deposito()
        elif opcao == '2':
            banco.saque()

    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        continuar = False
        print('\nObrigado por usar nossos serviços!')
    elif continuar == 'S' and opcao == '1':
        continuar = True
        valor += deposito
    elif continuar == 'S' and opcao == '2':
        continuar = True
        valor -= saque
    else:
        banco.error()
