#Contexto: Um programa de descontos em uma loja. 
#Questão: Escreva um programa que dê descontos de acordo com o valor da compra: 
#acima de R$100, desconto de 10%; entre R$50 e R$100, desconto de 5%; abaixo de R$50, sem desconto. 
#Calcule e mostre o valor do desconto e o valor total a pagar.

valor_compra = float(input('Informe o valor da compra: '))

if valor_compra>100:
    print(f'Desconto de 10%. Valor total a pagar: R$ {(valor_compra-valor_compra*0.1):.2f}')
elif valor_compra>=50 and valor_compra<=100:
    print(f'Desconto de 5%. Valor total a pagar: R$ {(valor_compra-valor_compra*0.05):.2f}')
else:
    print(f'Sem desconto. Valor total a pagar: R$ {valor_compra:.2f}')