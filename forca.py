

def jogar():
    print("###############################")
    print("**O jogo de forca começou!!!**")
    print("###############################")

    palavra_secreta = "maçã".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    erros = 0

    enforcou = False
    acertou = False

    print(letras_acertadas)
    #Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):


        chute = input("\nQual a letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute==letra):
                    letras_acertadas[index] = letra
                index = index+1
            print(letras_acertadas)
        else:
            erros = erros + 1
        acertou = "_" not in letras_acertadas
        enforcou = erros ==6

        if (acertou):
            print("Você ganhou!!!")
        elif(enforcou):
            print("Você perdeu :(")


    print("Fim do jogo!!")

jogar()