import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
pontos = 1000


print("Qual o nivel de dificuldade ? ")
print("(1) Facil (2) Médio (3) Dificil")

nivel = int(input("Defina o nivel: "))

if (nivel == 1):
    total_tentativas = 20
elif (nivel==2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1,total_tentativas + 1):

    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")

    chute = int(chute_str)


    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou o numero e fez {} pontos!!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou ! seu numero maior que o numero secreto")
        elif (menor):
            print("Você errou ! seu numero menor que o numero secreto")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("\n")
print("**********************************")
print("Fim de jogo")
print("**********************************")