#Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
#espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
#escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
#70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
#determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
#busque uma nova arma.

def batalha_final():
    
    espada_ataque = int(input('Poder de ataque da espada: '))
    espada_durab = int(input('Durabilidade da espada: '))
    arco_ataque = int(input('Poder de ataque do arco: '))
    arco_durab = int(input('Durabilidade do arco: '))
    lanca_ataque = int(input('Poder de ataque da lança: '))
    lanca_durab = int(input('Durabilidade da lança: '))
    
    if espada_ataque > 50 and espada_durab > 70:
        print('Escolha a espada!')
    elif arco_ataque > 50 and arco_durab > 70:
        print('Escolha o arco!')
    elif lanca_ataque > 50 and lanca_durab > 70:
        print('Escolha a lança!')
    else:
        print('Busque uma nova arma!')
    
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    batalha_final()
   
    print('...Fim do programa...') 