def jogar():
    print("************************************")
    print("************************************")
    print("*******    Jogo da forca       *****")
    print("************************************")
    print("************************************")


    palavra_secreta = "banana"

    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print("\n", letras_acertadas, "\n")

    #enquato(true)
    while(not enforcou and not acertou):

        chute = input("Qual a letra ? ")

        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

            index = index + 1


        print("\n", letras_acertadas, "\n")


    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()