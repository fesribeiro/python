print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1


for rodada in range(1,total_tentativas + 1):

    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")

    chute = int(chute_str)


    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue


    print("Voce digitou", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou o numero !!")
        break
    else:
        if (maior):
            print("Você errou ! seu numero maior que o numero secreto")
        elif (menor):
            print("Você errou ! seu numero menor que o numero secreto")


print("\n")
print("**********************************")
print("Fim de jogo")
print("**********************************")