#Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a
#armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga
#precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e
#ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.

def armadura_guerreiro():
    
    qtd_ferro = float(input('Digite a quantidade de ferro: '))
    qtd_ouro = float(input('Digite a quantidade de ouro: '))

    liga = qtd_ferro + qtd_ouro

    if qtd_ferro/liga >= 0.7:
        print('Quantidade de ferro na liga é suficiente!')
    else:
        print('Quantidade de ferro na liga é insuficiente!')

if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    armadura_guerreiro()
   
    print('...Fim do programa...') 