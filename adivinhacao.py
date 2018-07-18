print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

chute = int(chute_str)

print("Voce difitou", chute)

if (numero_secreto == chute):
    print("Voce acertou o numero !!")
else:
    if (chute < numero_secreto):
        print("Numero menor que o resultado")
    else:
        print("Numero maior que o resultado")

print("\n")
print("**********************************")
print("Fim de jogo")