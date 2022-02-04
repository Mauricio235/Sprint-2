import forca
import jogo_advinhacao

print("###############################")
print("******Bem Vindo aos jogos******")
print("###############################")

print("(1) Forca  (2) Advinhação")

jogo = int(input("Digite o número do jogo escolhido:"))

if (jogo == 1):
    print('Jogando forca!!!')
    forca.jogar()
elif(jogo == 2):
    print("Jogando advinhação")
    jogo_advinhacao.jogar()