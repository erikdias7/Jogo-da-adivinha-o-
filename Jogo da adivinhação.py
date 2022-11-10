import random
#jogo com for 
import time

def jogar_adivinhacao():

    print("★ ★ ★ BEM VINDO AO JOGO DA ADIVINHAÇÃO ★ ★ ★")
    numero_secreto = random.randrange(1, 100 + 1)

    tentativas = 0

    rodada = 1
    
    pontos = 500

    print ("Qual o nível de dificuldade?")
    print ("(1) fácil, (2) médio (3) difícil")
    nivel = int(input("Defina o nível de dificuldade:"))
    if (nivel == 1):
        tentativas = 20
        print ("CHUTE UM NÚMERO DE 1 A 100")
        print ("VOCÊ TERÁ 20 TENTATIVAS! BOA SORTE")
    elif(nivel == 2):
        tentativas = 15
        print ("CHUTE UM NÚMERO DE 1 A 100")
        print ("VOCÊ TERÁ 15 TENTATIVAS! BOA SORTE")
    elif(nivel == 3):
        tentativas = 10
        print ("CHUTE UM NÚMERO DE 1 A 100")
        print ("VOCÊ TERÁ 10 TENTATIVAS! BOA SORTE")
    else:
        print("OPÇÃO NÃO EXISTENTE, VOLTANDO AO MENU")
        jogar_adivinhacao()
    for rodada in range(1,tentativas + 1):
        print("Tentativa {} de {}".format (rodada, tentativas))
        chute = int(input("Digite o seu número: "))


        if (numero_secreto == chute):
            print("Você acertou e fez {} pontos".format(pontos))
            print("Meus parabéns, você passou, voltando para o menu inicial")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou, valor acima do correto")
            elif(chute < numero_secreto):
                print("Você errou, valor abaixo do correto")
            pontosperdidos = abs(chute - numero_secreto)
            pontos = pontos + pontosperdidos

if(__name__ == "__main__"):        
    jogar_adivinhacao()