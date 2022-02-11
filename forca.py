import random


def jogar():

    imprime_introdução()

    palavra_secreta = carrega_palavra_acertada()

    letras_acertadas = inicializa_palavra_secreta(palavra_secreta)
    erros = 0

    enforcou = False
    acertou = False

    print(letras_acertadas)
    #Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):


        chute = pede_chute()

        if (chute in palavra_secreta):
            marc_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            erros = erros + 1
            desenha_forca(erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros ==6

        if (acertou):
            imprime_mensagem_succeso()
        elif(enforcou):
            imprime_mensagem_fracasso(palavra_secreta)


    print("Fim do jogo!!")


def imprime_introdução():
    print("###############################")
    print("**O jogo de forca começou!!!**")
    print("###############################")


def carrega_palavra_acertada():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return (palavra_secreta)


def inicializa_palavra_secreta(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("\nQual a letra?")
    chute = chute.strip().upper()
    return (chute)


def marc_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1
    print(letras_acertadas)


def imprime_mensagem_fracasso(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def imprime_mensagem_succeso():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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


jogar()

