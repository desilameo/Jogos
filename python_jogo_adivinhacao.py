'''
print("***************************************")
print("Bem vindo ao jogo de adivinhação")
print("***************************************")

numero_secreto = 42
chute_str = input("Digite seu número")

print("Você digitou", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")


#adicionar tentativas
print("***************************************")
print("Bem vindo ao jogo de adivinhação")
print("***************************************")

numero_secreto = 42
tentativas = 3
rodada = 1

while rodada <= tentativas:

    print("Tentativa {} de {} rodada".format(rodada,tentativas))
    chute_str = input("Digite seu número")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim de jogo")




#utilizando FOR

print("***************************************")
print("Bem vindo ao jogo de adivinhação")
print("***************************************")

numero_secreto = 42
tentativas = 3

for rodada in range(1,tentativas +1):

    print("Tentativa {} de {} rodadas: ".format(rodada,tentativas))
    chute_str = input("Digite seu número de 1 a 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 101):
        print("Você deve digitar  um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim de jogo")



#interpolação de string

#fixando casas decimais em float

print("R$ {}".format(1.59))

print("R$ {:f}".format(1.59))

print("R$ {:.2f}".format(1.59))

#alinhando o ponto nos valores
print("R$ {:7.2f}".format(1.59))
print("R$ {:7.2f}".format(1236.59))
print("R$ {:07.2f}".format(1.59))

# definindo para valores inteiros
print("R$ {:7d}".format(46))
print("Data {:02d}/{:02d}/{:04d}".format(8,10,2021))

'''

#  usando random
def jogar():

    print("***************************************")
    print("Bem vindo ao jogo de adivinhação")
    print("***************************************")

    import random


    #Outras opcoes de random
    #numero_secreto = round(random.random()*100)
    #numero_secreto = random.randrange(1,101)

    numero_secreto = random.randint(1,100)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina seu nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas +1):

        print("Tentativa {} de {} rodadas: ".format(rodada,tentativas))
        chute_str = input("Digite seu número de 1 a 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 101):
            print("Você deve digitar  um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos, parabéns!!!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim de jogo, o número secreto era:", numero_secreto)

if(__name__ == "__main__"):
    jogar()