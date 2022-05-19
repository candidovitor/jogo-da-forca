import random
from palavras import palavras
from forma_forca import formato_das_vidas
import string

    
def valida_palavra(palavras):
    palavra = random.choice(palavras)  
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()


def hangman():
    palavra = valida_palavra(palavras)
    letra_palavra = set(palavra) 
    alfabeto = set(string.ascii_uppercase)
    letras_usuario = set()  

    vidas = 7

    while len(letra_palavra) > 0 and vidas > 0:

        print('Você tem', vidas, 'vidas restantes e já usou as seguintes letras: ', ' '.join(letras_usuario))

        lista_palavra = [letra if letra in letras_usuario else '-' for letra in palavra]
        print(formato_das_vidas[vidas])
        print('A palavra é...: ', ' '.join(lista_palavra))

        adivinha_letra = input('Tente adivinhar a letra: ').upper()
        if adivinha_letra in alfabeto - letras_usuario:
            letras_usuario.add(adivinha_letra)
            if adivinha_letra in letra_palavra:
                letra_palavra.remove(adivinha_letra)
                print('')

            else:
                vidas = vidas - 1 
                print('\nA letra escolhida foi:', adivinha_letra, 'porém não está na palavra.')

        elif adivinha_letra in letras_usuario:
            print('\nVocê já usou essa letra, tente outra.')

        else:
            print('\nEssa não é uma letra válida.')

    if vidas == 0:
        print(formato_das_vidas[vidas])
        print('Você perdeu!! A palavra era: ', palavra)
    else:
        print('Uhuuul,  VOCÊ GANHOU!!', palavra, '!!')



hangman()