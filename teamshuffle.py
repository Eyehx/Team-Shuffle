import random
# Questionario para o modelo de montagem
def sorteador_de_equipes():
    num_times = int(input("Quantos times são? "))
    num_jogadores = int(input("Quantos jogadores por time? "))
    
    jogadores_por_posicao = {
        'mid': [],
        'top': [],
        'jungle': [],
        'sup': [],
        'adc': []
    }
    # Inserção dos dados para o sorteio
    for _ in range(num_jogadores * num_times):
        nome = input("Digite o nome do jogador: ")
        posicao = input("Digite a posição do jogador (mid, top, jungle, sup, adc): ").lower()
        while posicao not in jogadores_por_posicao.keys() or len(jogadores_por_posicao[posicao]) >= num_times:
            print("Posição inválida ou já preenchida. Tente novamente.")
            posicao = input("Digite a posição do jogador (mid, top, jungle, sup, adc): ").lower()
        jogadores_por_posicao[posicao].append(nome)
    
    times = [[] for _ in range(num_times)]
    
    for posicao, lista_jogadores in jogadores_por_posicao.items():
        random.shuffle(lista_jogadores)
        for i, jogador in enumerate(lista_jogadores):
            times[i % num_times].append((jogador, posicao))
    
    return times
# Retorno dos dados
def imprimir_times(times):
    for i, time in enumerate(times, start=1):
        print(f"Time {i}:")
        for jogador, posicao in time:
            print(f"{jogador} - {posicao}")
        print()

times = sorteador_de_equipes()
imprimir_times(times)