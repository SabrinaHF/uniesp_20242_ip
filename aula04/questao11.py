#Contexto: Cinema. 
#Questão: Escreva um programa que pergunta ao usuário sua idade e informa o valor do ingresso do cinema: 
#abaixo de 12 anos e acima de 60, R$ 15.00; entre 12 e 60 anos, R$ 25.00.

idade = int(input('Qual a sua idade: '))

if idade<12 or idade>60:
    print('Valor do ingresso: R$ 15.00.')
else:
    print('Valor do ingresso: R$ 25.00.')