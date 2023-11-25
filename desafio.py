import random 
continuar = True
while continuar:
    numEasy = random.randint(0,10)
    numMedium = random.randint(0,50)
    numHard = random.randint(0,100)
    try:
        def facil():
            tentativas = 5
            while tentativas > 0:
                print(f'-------------------------------------------------------------------------\nDificuldade EASY, Escolha um numero de 0/10 \n BOA SORTE! Tentativas ={tentativas}')
                try:
                    choise = int(input('Digite o número:'))
                except BaseException:
                    print('Digite um numero valido')           
                if choise == numEasy:
                    print(f'\n{nome} Parabéns você ganhou! o numero era: {numEasy}')
                    break
                elif choise > 10:
                    print('Digite um numero menor do que 10!')
                elif choise < 0:
                    print('Digite um numero maior que zero!')
                elif choise != numEasy and tentativas ==1:
                    print(f'\n{nome} Você perdeu! o numero era {numEasy}')
                    break
                elif choise != numEasy:
                    print(f'\n{nome} Você errou! tente novamente!')
                    tentativas = tentativas - 1
                else:
                    raise BaseException('Digite um numero inteiro')
            return choise

        def medio():
            tentativas = 10
            while tentativas > 0:
                print(f'-------------------------------------------------------------------------\nDificuldade MEDIUM, Escolha um numero de 0/50 \n BOA SORTE! Tentativas ={tentativas}')
                try:
                    choise = int(input('Digite o número:'))
                except BaseException:
                    print('Digite um numero valido')           
                if choise == numMedium:
                    print(f'\n{nome} Parabéns você ganhou! o numero era: {numMedium}')
                    break
                elif choise > 50:
                    print('Digite um numero menor do que 50!')
                elif choise < 0:
                    print('Digite um numero maior que zero!')
                elif choise != numMedium and tentativas ==1:
                    print(f'\n{nome} Você perdeu! o numero era {numEasy}')
                    break
                elif choise != numMedium:
                    print(f'\n{nome} Você errou! tente novamente!')
                    tentativas = tentativas - 1
                else:
                    raise BaseException('Digite um numero inteiro')
            return choise

        def dificil():
            tentativas = 15
            while tentativas > 0:
                print(f'-------------------------------------------------------------------------\nDificuldade HARD, Escolha um numero de 0/100 \n BOA SORTE! Tentativas ={tentativas}')
                try:
                    choise = int(input('Digite o número:'))
                except BaseException:
                    print('Digite um numero valido')           
                if choise == numHard:
                    print(f'\n{nome} Parabéns você ganhou! o numero era: {numHard}')
                    break
                elif choise > 100:
                    print('Digite um numero menor do que 100!')
                elif choise < 0:
                    print('Digite um numero maior que zero!')
                elif choise != numHard and tentativas ==1:
                    print(f'\n{nome} Você perdeu! o numero era {numHard}')
                    break
                elif choise != numHard:
                    print(f'\n{nome} Você errou! tente novamente!')
                    tentativas = tentativas - 1
                else:
                    raise BaseException('Digite um numero inteiro')
            return choise
    except BaseException as e:
        print(f'Error: {e}')

    print('-------------------------------------------------------------------------\nBem vindo ao jogo do Milhão!')
    nome = input('Digite seu nome:')

    try:
        idade = int(input('\nDigite sua idade para escolher a dificuldade: '))
    except BaseException:
        print(f'Digite um numero inteiro')
        exit()
    try:
        if idade <= 10:
            facil()
        elif idade >10 and idade <= 18:
            medio()
        elif idade > 18:
            dificil()
        elif idade == 0:
            print('Digite uma idade diferente de 0!')
        elif idade < 0:
            print('Digite uma idade valída!')
        else:
            raise BaseException('Digite um numero inteiro!')
  
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            continuar = False
            print('\nObrigado por usar nossos serviços!')
            break
        elif continuar =='S':
            continuar = True
        else:
            raise BaseException('Digite S ou N!')
            exit()
         
    except BaseException as e:
        print(f'Erro:{e}')
