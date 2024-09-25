#Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X
#número de passos para o norte, e a segunda no Y número de passos para o leste. Crie um
#programa que receba os valores de X e Y e calcule a distância total que o pirata precisa
#percorrer para chegar ao tesouro (soma de X e Y).

def tesouro_escondido():

    valor_x = int(input('Digite os números de passos para o norte: '))
    valor_y = int(input('Digite os números de passos para o leste: '))

    print(f'Distância para chegar ao tesouro é de {valor_x+valor_y} passos.')   

if __name__ == '__main__':
    
   print('...Iniciando programa...') 
   
   tesouro_escondido()
   
   print('...Fim do programa...') 