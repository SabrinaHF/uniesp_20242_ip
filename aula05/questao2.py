
def funcao_processamento():
    
    qtd_ferro = float(input('Digite a quantidade de ferro: '))
    qtd_ouro = float(input('Digite a quantidade de ouro: '))

    total = qtd_ferro + qtd_ouro

    if (qtd_ferro/total) >= 0.7:
        print('Porcentagem de ferro na liga é suficiente')
    else:
        print('Porcentagem de ferro na liga é insuficiente')

if __name__ == '__main__':
    
 
    print('--- --- Iniciando o programa --- ---')
    
    
    funcao_processamento()
    
    
    print('--- --- Fim do programa --- ---')