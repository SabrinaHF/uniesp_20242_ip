#Contexto: Pesquisa eleitoral. 
#Questão: Solicite ao usuário que insira um número: 
#1 para o candidato A, 2 para o candidato B, 3 para o candidato C e qualquer outro número para voto nulo. 
#Em seguida, informe a qual candidato o voto foi destinado ou se foi nulo.

num = int(input('Insira um número: '))

match num:
    case 1: 
        print('O voto foi para o Candidato A')
    case 2: 
        print('O voto foi para o Candidato B')
    case 3: 
        print('O voto foi para o Candidato C')
    case _:
        print('O voto foi nulo')