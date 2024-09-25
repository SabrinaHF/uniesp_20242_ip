#Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de
#25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o
#valor total que o colecionador tem.

def contagem_moedas():

    qtd_um = int(input('Qual a quantidade de moedas de 1 real? '))
    qtd_cinquenta = int(input('Qual a quantidade de moedas de 50 centavos? '))
    qtd_vintecinco = int(input('Qual a quantidade de moedas de 25 centavos? '))

    print(f'O valor total das moedas é de R$ {qtd_um + qtd_cinquenta*0.5 + qtd_vintecinco*0.25:.2f}!')
    
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    contagem_moedas()
   
    print('...Fim do programa...') 