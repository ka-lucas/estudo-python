#Desenvolva um jogo simples de adivinhação onde o computador sorteie um número entre 1 e 100 e o usuário deve adivinhar.

from random import choice 

def adivinhacao():
    number1 = int(input("Digite o numero:\n"))
    numero_aleatorio = choice(range(1,100))
    if number1 == numero_aleatorio:
        return(numero_aleatorio)
    else: 
        return (numero_aleatorio)

if __name__ == '__main__' :
    resultado = adivinhacao()
    if resultado == 1 :
        print(f"Resultado:\nVoce acertou o resultado é {resultado}")
    else:
        print(f"Resultado:\nVoce errou o resultado é {resultado}")

