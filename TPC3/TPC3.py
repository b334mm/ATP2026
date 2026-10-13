import random

alvos = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]


def jogada_computador(total):
    for alvo in alvos:
        dif = alvo - total
        if dif >= 1 and dif <= 10:
            return dif
    return random.randint(1, 10)


def jogada_jogador(total):
    jogada = int(input("A tua jogada (1 a 10): "))
    while jogada < 1 or jogada > 10 or total + jogada > 100:
        print("Jogada inválida.")
        jogada = int(input("A tua jogada (1 a 10): "))
    return jogada


print("Corrida para o 100!")
resp = input("Queres que o computador jogue primeiro? (s/n): ")
if resp == "s":
    vez = "computador"
else:
    vez = "jogador"

total = 0
while total < 100:
    if vez == "computador":
        jogada = jogada_computador(total)
        total = total + jogada
        print("O computador jogou", jogada, "-> total:", total)
        vez = "jogador"
    else:
        jogada = jogada_jogador(total)
        total = total + jogada
        print("Jogaste", jogada, "-> total:", total)
        vez = "computador"


if vez == "jogador":
    print("O computador ganhou!")
else:
    print("Ganhaste!")


