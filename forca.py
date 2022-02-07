

def jogar():
    print("###############################")
    print("**O jogo de forca começou!!!**")
    print("###############################")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):

        chute = input("\nQual a letra?")
        chute = chute.strip()


        print("jogando...")
        index = 0
        for letra in palavra_secreta:
            if (chute.upper()==letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index = index+1
    print("Fim do jogo!!")

jogar()