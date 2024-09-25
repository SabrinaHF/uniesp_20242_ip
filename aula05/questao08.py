#Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se
#um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se
#completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe
#10 moedas de ouro. Crie um programa que receba o número de missões completadas e
#informe o valor do bônus.

def calculadora_bonus():
    
    qtd_missao = int(input('Número de missões do cavaleiro: '))
    
    if qtd_missao>10:
        print('O valor do bônus é de 100 moedas de ouro!')
    elif qtd_missao>=5 and qtd_missao<=10:
        print('O valor do bônus é de 50 moedas de ouro!')
    else:
        print('O valor do bônus é de 10 moedas de ouro!')

if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    calculadora_bonus()
   
    print('...Fim do programa...') 