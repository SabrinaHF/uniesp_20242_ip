#Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
#de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
#escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.

def desafio_caverna():
    
    porta = int(input('Digite o nº da porta: '))
    
    match porta:
        case 1:
            print('O aventureiro irá enfrentar o desafio 1!')
        case 2:
            print('O aventureiro irá enfrentar o desafio 2!')
        case 3:
            print('O aventureiro irá enfrentar o desafio 3!')
        case 4:
            print('O aventureiro irá enfrentar o desafio 4!')
        case 5:
            print('O aventureiro irá enfrentar o desafio 5!')
    
    
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    desafio_caverna()
   
    print('...Fim do programa...') 