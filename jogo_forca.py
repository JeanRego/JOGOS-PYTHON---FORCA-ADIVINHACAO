import random

def jogar():

    imprime_bemVindo()

    palavraSecreta = palavra_secreta()

    letras = letras_acertadas(palavraSecreta)
    print(letras)


    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        print("Jogando...")

        chute = pede_chute()

        if (chute in palavraSecreta):

            marca_chute_correto(chute,palavraSecreta,letras)

        else:
            erros += 1
        enforcou = erros == 7
        acertou = "_" not in letras
        desenha_forca(erros)
        print(letras)

    if (acertou):
        imprime_mensagem_ganhou()

    else:
        imprime_mensagem_perdeu(palavraSecreta)


def imprime_bemVindo():
    print("***************************************")
    print("   Bem vindo(a) ao meu jogo da forca   ")
    print("***************************************")


def palavra_secreta():
    arquivo = open('txt/nomes.txt', 'r')
    palavras = []

    for x in arquivo:
        x = x.strip()
        palavras.append(x)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    secreto = palavras[numero].upper()
    return secreto

def letras_acertadas (x):
    return ["_" for letra in x]

def pede_chute():
    chute = input("Qual a letra?: ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute,palavraSecreta,letras):
        index = 0
        for letra in palavraSecreta:
            if (chute == letra):
                print(f"Encrontrei a letra {letra} na posicao {index}")
                letras[index] = letra
            index = index + 1


def imprime_mensagem_ganhou():
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


def imprime_mensagem_perdeu(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
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

if (__name__ == "__main__"):
    jogar()
