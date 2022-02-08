

def jogar():
    print("###############################")
    print("**O jogo de forca começou!!!**")
    print("###############################")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)
    #Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):

        chute = input("\nQual a letra?")
        chute = chute.strip()


        print("jogando...")
        index = 0
        for letra in palavra_secreta:
            if (chute.upper()==letra.upper()):
                letras_acertadas[index] = letra
            index = index+1
        print(letras_acertadas)
    print("Fim do jogo!!")

jogar()