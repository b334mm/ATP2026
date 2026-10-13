"""Jogo Corrida para o 100."""


def obter_jogada(total):
	"""Pede uma jogada válida, sem ultrapassar 100."""
	while True:
		try:
			jogada = int(input("Escolhe um número de 1 a 10: "))
		except ValueError:
			print("Introduz um número inteiro.")
			continue

		if 1 <= jogada <= 10 and total + jogada <= 100:
			return jogada
		print("Jogada inválida. Escolhe entre 1 e 10 sem ultrapassar 100.")


def jogar(computador_primeiro):
	total = 0
	vez_computador = computador_primeiro

	while total < 100:
		if vez_computador:
			if computador_primeiro and total == 0:
				jogada = 1
			else:
				# Deixa o adversário num total congruente com 1 módulo 11.
				jogada = (1 - total % 11) % 11
				# Se já estiver nessa posição, não há jogada que a mantenha;
				# escolher 1 permite continuar a partida.
				if jogada == 0:
					jogada = 1
			print(f"O computador soma {jogada}.")
		else:
			jogada = obter_jogada(total)

		total += jogada
		print(f"Total: {total}")

		if total == 100:
			vencedor = "Computador" if vez_computador else "Jogador"
			print(f"{vencedor} venceu!")
			return

		vez_computador = not vez_computador


def main():
	print("Corrida para o 100")
	print("1 - O computador joga primeiro")
	print("2 - O jogador joga primeiro")
	while True:
		escolha = input("Escolhe uma opção (1 ou 2): ").strip()
		if escolha in ("1", "2"):
			jogar(computador_primeiro=(escolha == "1"))
			break
		print("Opção inválida.")


if __name__ == "__main__":
	main()


