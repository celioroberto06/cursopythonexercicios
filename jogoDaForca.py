import random
from random import randint

def msg_abertura():
    print('\033[31m==' * 13)
    print('BEM VINDO AO JOGO DA FORCA')
    print('==' * 13, '\033[m')


def diversas_palavras():
    palavras = ['BANANA', 'MAÇA', 'MORANGO', 'MELANCIA']
    for c in range(1, 4):
        palavras.append(str(input(f'Digite a {c}ª palavra: ')))
    sorteio = random.choice(palavras)
    palavra_secreta = sorteio.upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    lista = ['_' for letra in palavra]
    return lista


def pede_chute():
    chute = input('Qual o seu chute? ').upper().strip()[0]
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def msg_perdeu(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def msg_ganhou():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\      /-.      ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \::.    /       ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def  jogar():
    msg_abertura()
    palavra_secreta = diversas_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print(f'Ainda esta faltando {letras_faltando} letras')
    if(acertou):
        msg_ganhou()
    else:
        msg_perdeu(palavra_secreta)

    print('FIM DO JOGO')


if (__name__== "__main__"):
    jogar()




