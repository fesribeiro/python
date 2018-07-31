def jogar():
    print("************************************")
    print("************************************")
    print("*******    Jogo da forca       *****")
    print("************************************")
    print("************************************")


    palavra_secreta = "banana".upper()


    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

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