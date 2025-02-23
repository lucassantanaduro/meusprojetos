class Jogador:
    def __init__(self):
        self.nome = input("Nome do jogador: ")
    
    def alterar_nome_jogador(self):
        self.nome = input('Digite o novo nome: ')
    
    def apresentar_jogador(self):
        return self.nome