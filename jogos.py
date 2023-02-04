
import jogo_adivinha
import jogo_forca

print("****************************************")
print("********** ESCOLHA O JOGO **************")
print("****************************************")

print("Adivinhação(1)  Forca(2)")

escolha_jogo = int(input("Qual o jogo?: "))

if (escolha_jogo == 1):
    print("Jogando Adivinhação")
    jogo_adivinha.adivinhacao()

elif (escolha_jogo == 2):
    print("forca")
    jogo_forca.jogar()