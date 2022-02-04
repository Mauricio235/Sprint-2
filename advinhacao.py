print("###############################")
print("O jogo de advinhação começou!!!")
print("###############################")

numero_secreto = 54
total_de_tentativas = 3

while (total_de_tentativas>0):
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    print("Você digitou", chute_str)
    print("O numero secreto é: ", numero_secreto)

    acertou = numero_secreto==chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    type(acertou)


    if (acertou):
        print("\nVocê acertou!!!")
    else:
        if (maior):
            print("\nVocê errou!!!  O seu chute foi maior que o número secreto")
        elif(menor):
            print("\nVocê errou!!!  O seu chute foi menor que o número secreto")

    print("Fim do jogo !")
    total_de_tentativas= total_de_tentativas - 1


