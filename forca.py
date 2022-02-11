import random


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


def imprime_mensagem_fracasso():
    print("Você perdeu!!!")


def imprime_mensagem_suceso():
    print("Você Ganhou!!!")


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

        acertou = "_" not in letras_acertadas
        enforcou = erros ==6

        if (acertou):
            imprime_mensagem_suceso()
        elif(enforcou):
            imprime_mensagem_fracasso()


    print("Fim do jogo!!")

jogar()

