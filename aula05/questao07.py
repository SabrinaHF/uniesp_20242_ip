#Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se
#uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3
#metros). Crie um programa que receba a altura da planta e informe a sua classificação.

def plantas_magicas():
    
    altura_planta = float(input('Digite a altura da planta ~mágica~: '))
    
    if altura_planta < 1:
        print('A planta ~mágica~ é da pequena!')
    elif altura_planta > 3:
        print('A planta ~mágica~ é da grande!')
    else:
        print('A planta ~mágica~ é da média!')

if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    plantas_magicas()
   
    print('...Fim do programa...') 