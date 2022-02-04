print("###############################")
print("O jogo de advinhação começou!!!")
print("###############################")

numero_secreto = int(random.random() * 100)
total_de_tentativas = 3

numero_jogada = total_de_tentativas
rodada = 1
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, numero_jogada))
    chute_str = input("Digite o seu número entre 1 e 100: ")
    chute = int(chute_str)
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    print("Você digitou", chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    type(acertou)

    if acertou:
        print("\nVocê acertou!!!")
        break
    else:
        if maior:
            print("\nVocê errou!!!  O seu chute foi maior que o número secreto")
        elif menor:
            print("\nVocê errou!!!  O seu chute foi menor que o número secreto")

    total_de_tentativas = total_de_tentativas - 1

print("Fim do jogo !")
