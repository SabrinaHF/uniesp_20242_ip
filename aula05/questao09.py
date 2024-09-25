#Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a
#escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para
#exibir o feitiço escolhido.

def escolha_feitiço():
    
    num_feitico = int(input('Informe o nº do feitiço: '))
    
    match num_feitico:
        case 1:
            print('O feitiço é de fogo!')
        case 2:
            print('O feitiço é de água!')
        case 3:
            print('O feitiço é de terra!')


if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    escolha_feitiço()
   
    print('...Fim do programa...') 