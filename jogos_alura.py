import python_alura_jogo_forca
import python_alura_jogo_adivinhacao

def escolha_jogo():
        print("***************************************")
        print("***********Escolha um jogo!************")
        print("***************************************")

        print("(1) Forca (2) Adivinhação")

        jogo = int(input("QUal o jogo?"))
        if (jogo == 1 ):
                print("Jogando forca")
                python_alura_jogo_forca.jogar()
        elif (jogo == 2):
                print("Jogando Adivinhação")
                python_alura_jogo_adivinhacao.jogar()

if (__name__ == "__main__"):
        escolha_jogo()
