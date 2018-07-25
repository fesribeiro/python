def jogar():
    print("************************************")
    print("************************************")
    print("*******    Jogo da forca       *****")
    print("************************************")
    print("************************************")
    print("************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #enquato(true)
    while(not enforcou and not acertou):

        chute = input("Qual a letra ? ")

        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))

            index = index + 1


        print("Jogando...")


    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()