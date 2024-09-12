#Contexto: Controle de velocidade. 
#Questão: Peça ao usuário para inserir a velocidade atual de um carro.
#Informe se ele está abaixo do limite (80 km/h), ou se ele deverá ser multado (acima de 80 km/h). 
#Se ele for multado, informe que a multa será de R$5,00 por km acima do limite.

velocidade = int(input('Insira velocidade atual do carro: '))

if velocidade<=80:
    print('Velocidade abaixo do limite')
else:
    print(f'Velocidade acima do limite. Multa de R$ {(velocidade-80)*5:.2f}')
