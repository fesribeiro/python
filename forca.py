import random

def jogar():
    print("************************************")
    print("************************************")
    print("*******    Jogo da forca       *****")
    print("************************************")
    print("************************************")


    arquivo = open("palavras.txt", "r")
    palavras = []


    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    erros = 0

    print("\n", letras_acertadas, "\n")

    #enquato(true)
    while(not enforcou and not acertou):

        chute = input("Qual a letra ? ")

        chute = chute.strip().upper()

        

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros += 1

        enforcou = erros == 6 
        acertou = "_" not in letras_acertadas

        print("\n", letras_acertadas, "\n")

    if (acertou):
        print("Você ganhou !!")
    else:
        print("Você perdeu !!")


    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()