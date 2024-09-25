#Em um campeonato de corrida de dragões, cada dragão corre uma determinada
#distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois
#dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma
#velocidade.

def corrida_dragao():
    
    dragao_um_dist = float(input('Distância - Dragão 01: '))
    dragao_um_tempo = float(input('Tempo - Dragão 01: '))
    dragao_dois_dist = float(input('Distância - Dragão 02: '))
    dragao_dois_tempo = float(input('Tempo - Dragão 02: '))
    
    velocidade_um = dragao_um_dist/dragao_um_tempo
    velocidade_dois = dragao_dois_dist/dragao_dois_tempo
    
    if velocidade_um > velocidade_dois:
        print('O Dragão 01 é o mais rápido!')
    elif velocidade_dois > velocidade_um:
        print('O Dragão 02 é o mais rápido!')
    else:
        print('Os dragões são igualmente rápidos!')
    
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    corrida_dragao()
   
    print('...Fim do programa...') 