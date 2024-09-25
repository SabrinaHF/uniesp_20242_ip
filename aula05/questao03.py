#Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
#Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for
#mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir
#que é uma tartaruga.

def advinha_animais():
    
    animal = input('Seu animal favorito é um mamífero ou réptil? ')

    if animal == 'mamífero':
        print('Acho que seu animal favorito é um cachorro!')
    else:
        print('Acho que seu animal favorito é uma tartaruga!')
        
if __name__ == '__main__':
      
    print('...Iniciando programa...') 
   
    advinha_animais()
   
    print('...Fim do programa...') 