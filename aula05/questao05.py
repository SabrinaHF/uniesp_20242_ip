#Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de
#água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de
#água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a
#distância até o oásis, e informe se a água é suficiente.

def jornada_deserto():
    
    qtd_agua = float(input('Informe a quantidade de água em litros: '))
    distancia = float(input('Informe a distância até o oásis em quilômetros: '))
    
    if qtd_agua == distancia*2:
        print('A quantidade de água é suficiente para chegar no próximo oásis.')
    else:
        print('A quantidade de água é insuficiente para chegar no próximo oásis.')
        
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    jornada_deserto()
   
    print('...Fim do programa...') 