from openpyxl import Workbook

# Função para adicionar dados à planilha

def adicionar_dados(planilha, dados):
			for linha in dados:
			      planilha.append(linha)

# Dados a serem inseridos na planilha

dados = [
["Nome", "Idade", "Cidade"],
["Alice", 25, "São Paulo"],
["Bob", 30, "Rio de Janeiro"],
["Charlie", 22, "Belo Horizonte"],
]

# Cria uma nova planilha

wb = Workbook()
planilha = wb.active

# Adiciona os dados à planilha

adicionar_dados(planilha, dados)

# Salva a planilha em um arquivo

wb.save('dados.xlsx')

print("Dados inseridos na planilha 'dados.xlsx'.")