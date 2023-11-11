#1
# class Cachorro:
#     def __init__(self,raca,tamanho):
#         self.raca = raca
#         self.tamanho = tamanho
#     def latir(self):
#         print('AUUUUUUUUUUUUUUUUUU!!!!!!!!')
# cachorro1 = Cachorro('Pitbul','Grande')
# cachorro1.latir()

#2
# class Triangulo:
#     def __init__(self, largura,altura):
#         self.largura = largura
#         self.altura = altura
#     def calcular_area(self):
#         print(f'A area do triangulo é: {(self.altura*self.largura)/2}')
# triangulo1 = Triangulo(10,5)
# triangulo1.calcular_area()

#3
import random
class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def corrida(self):
        for self.aceleracao in range(1,6):
            kmh = random.randint(1,20)
            print(f"Correndo a velocidade atual é de {self.velocidade}Km/h")
            self.velocidade += kmh
        print(f'\nA velocidade do carro final é de {self.velocidade}Km/h!!!') 
carro1=Carro(0)
carro1.corrida()
