print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

chute = int(chute_str)

print("Voce digitou", chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto


if (acertou):
    print("Voce acertou o numero !!")
else:
    if (maior):
        print("Você errou ! seu numero maior que o numero secreto")
    elif (menor):
        print("Você errou ! seu numero menor que o numero secreto")

print("**********************************")
print("Fim de jogo")