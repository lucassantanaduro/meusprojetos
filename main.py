import random
import jogador

def jogar_dado():
    return random.randint(1,6)

def escolher_qtd_jogadores():
    numero_de_jogadores = 0
    while numero_de_jogadores < 1 or numero_de_jogadores > 4:
        numero_de_jogadores = int(input("\nDigite o numero de jogadores. Minimo 1, maximo 4: "))
    return numero_de_jogadores

def adicionar_jogadores(quantidade):
    jogadores = []
    for j in range(0,quantidade):
        print(f'Jogador {j+1}')
        jogadores.append(jogador.Jogador())
    return jogadores

def jogar():
    while True:
        for vez in range(len(jogadores)):
            print(f'\n{jogadores[vez].apresentar_jogador()} jogou o dado.')
            print(f'Resultado: {jogar_dado()}')
        decisao = input("\nContinuar jogando?")
        if decisao == 'Sim' or decisao == 'S' or decisao == 's':
            continue
        else:
            print("Até a proxima. Aperte ENTER para fechar.")
            input()
            break

qtd_jogadores = escolher_qtd_jogadores()
jogadores = adicionar_jogadores(qtd_jogadores)
jogar()