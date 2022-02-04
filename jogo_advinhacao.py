import random

def jogar():
    print("###############################")
    print("O jogo de advinhação começou!!!")
    print("###############################")



    numero_secreto = int(random.random() * 100)
    pontos = 1000
    print("Qual o nível de dificuldade? ")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input("\nDigite o nível de dificuldade:"))

    if (nivel == 1):
        total_de_tentativas=20
    elif (nivel == 2):
        total_de_tentativas=10
    else:
        total_de_tentativas=5





    numero_jogada = total_de_tentativas
    rodada = 1
    for rodada in range (1, total_de_tentativas+1):
        print(("Tentativa {} de {}").format(rodada,numero_jogada))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        print("Você digitou", chute_str)

        acertou = numero_secreto==chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        type(acertou)
        if (acertou):
            print("\nVocê acertou, e fez {} pontos!!!".format(pontos))
            break
        else:
            if (maior):
                print("\nVocê errou!!!  O seu chute foi maior que o número secreto")
            elif(menor):
                print("\nVocê errou!!!  O seu chute foi menor que o número secreto")
        pontos_perdidos= abs(numero_secreto-chute)
        pontos= pontos-pontos_perdidos
        total_de_tentativas= total_de_tentativas - 1


    print("Fim do jogo !")

