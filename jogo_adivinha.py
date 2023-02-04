
def adivinhacao ():
    print("***************************************")
    print("Bem vindo(a) ao meu jogo de adivinhação")
    print("***************************************")
    print("Tente adivinhar o valor que eu estou pensando!")
    print("")

    import random

    numero_secreto = random.randrange(1,11) #GERA NUMEROS DE 1 A 10. OU PODE USAR O RANDOM.RANDOM() * 10
    tentativas = 3
    rodadas = 1

    print("Escolha um nivel de dificuldade")
    print("Facil(1) Medio(2)  Dificil(3)  ")

    nivel_dif = int(input("Qual o nivel?: "))
    if (nivel_dif == 1):
        tentativas = 10
    if (nivel_dif == 2):
        tentativas = 5
    if (nivel_dif == 3):
        tentativas = 3

    print("Voce tem ", tentativas, " tentativas")
    print("")

    while (rodadas <= tentativas):
        print("Rodada {} de {}".format(rodadas,tentativas))
        numero_digitado = int(input("Digite um numero entre 1 e 10: "))

        if (numero_digitado < 1 or numero_digitado > 10): #VERIFICA SE O NUMERO DIGITADO É MENOR QUE 1 ou MAIOR QUE 10
            print("Numero invalido")
            continue #CONTINUE RETORNA A LEITURA DO CODIGO LA PRA CIMA

        acertou = numero_digitado == numero_secreto
        numero_alto = numero_digitado > numero_secreto
        numero_pequeno = numero_digitado < numero_secreto

        if(acertou):
            print("Voce acertou")
            break
        else:
            rodadas = rodadas + 1
            if(numero_alto):
                print("vc chutou um numero muito alto")
            elif(numero_pequeno):
                print("vc chutou um numero muito pequeno")



    print(f"O numero digitado era {numero_secreto} Game Over")


if (__name__ == "__main__"): #PARA CONSEGUIR ABRIR O ARQUIVO PELO TERMINAL
    adivinhacao()