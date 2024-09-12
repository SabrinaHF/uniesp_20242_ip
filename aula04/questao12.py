#Contexto: Condições climáticas.
#Questão: Peça ao usuário para inserir a temperatura atual e informe se está frio (< 15°C), ameno (entre 15°C e 25°C) ou quente (> 25°C).

temperatura = int(input('Informe a temperatura atual: '))

if(temperatura<15):
    print('Está frio.')
elif(temperatura>25):
    print('Está quente.')
else:
    print('Está ameno.')