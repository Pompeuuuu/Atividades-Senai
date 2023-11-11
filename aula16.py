#1
from datetime import datetime

# data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
# nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
# data_agora = datetime.now()

# idade = data_agora.year - nascimento.year - ((data_agora.month, data_agora.day)<(nascimento.month, nascimento.day))
# print(idade)


#2
data_agora = datetime.now()
print(f'{data_agora.year}:{data_agora.month}:{data_agora.day+7} às {data_agora.hour}:{data_agora.minute}:{data_agora.second}')