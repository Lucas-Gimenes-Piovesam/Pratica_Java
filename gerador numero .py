#JOGO PELO TERMINAL
#JOGO PELO TERMINAL
#JOGO PELO TERMINAL
#JOGO PELO TERMINAL
#JOGO PELO TERMINAL
#JOGO PELO TERMINAL

import random

def adivinhar():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto entre 1 e 100.")
    while True: 
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_secreto:
            print("Seu palpite é muito baixo. Tente aumentar.")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto. Tente diminuir.")
        else:
            print(f"Parabéns! Você acertou número secreto {numero_secreto} em {tentativas} tentativas. ")
            break

adivinhar()
