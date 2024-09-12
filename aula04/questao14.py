#Contexto: Cálculo de imposto. 
#Questão: Peça ao usuário para inserir seu salário mensal. 
#Calcule o imposto de renda com base no seguinte: até R$2000, isento; de R$2000,01 até R$3500, 10%; acima de R$3500, 15%.

salario = float(input('Insira seu saláro mensal: '))

if salario<=2000:
    print('Isento')
elif salario>2000 and salario<=3500:
    print(f'Imposto devido: R$ {salario*0.1:.2f}')
else:
    print(f'Imposto devido: R$ {salario*0.15:.2f}')