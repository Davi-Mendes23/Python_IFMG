from random import random, choice

class Tabuleiro:
    def __init__(self):
        self._posicoes = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]

    def imprime(self):
        print('\n |A|B|C|')
        for cont, linha in enumerate(self._posicoes):
            print('--------')
            print(cont + 1, '|' + '|'.join(linha), sep='')

    def jogada(self, posicao, simbolo):
        try:
            linha = int(posicao[0]) - 1
            letra = posicao[1].upper()
            coluna = ord(letra) - ord('A')
            if self._posicoes[linha][coluna] == ' ':
                self._posicoes[linha][coluna] = simbolo
                return True
        except:
            pass
        return False

    def posicoes_vazias(self):
        # Retorna lista com coordenadas de todas as casas vazias
        vazias = []
        for i in range(3):
            for j in range(3):
                if self._posicoes[i][j] == ' ':
                    vazias.append((i, j))
        return vazias

    def tem_jogada(self):
        return any(' ' in linha for linha in self._posicoes)

    def todas_linhas(self):
        todas = []
        # Linhas
        for linha in self._posicoes:
            todas.append(tuple(linha))
        # Colunas
        for cont in range(3):
            coluna = (self._posicoes[0][cont],
                      self._posicoes[1][cont],
                      self._posicoes[2][cont])
            todas.append(coluna)
        # Diagonais
        diagonal = []
        transversal = []
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            transversal.append(self._posicoes[2 - cont][cont])
        todas.append(tuple(diagonal))
        todas.append(tuple(transversal))
        return todas

class Velha:
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        self._jogador = 'X'  # Humano sempre X
        self._ia = 'O'       # IA sempre O

    def imprime(self):
        print('\n' * 50)
        print('Jogo da Velha\n')
        self._tabuleiro.imprime()

    def troca_jogador(self):
        self._jogador, self._ia = self._ia, self._jogador

    def eh_vencedor(self, jogador):
        linhas = self._tabuleiro.todas_linhas()
        return tuple([jogador] * 3) in linhas

    def jogada_humana(self):
        while True:
            self.imprime()
            print('\nJogador', self._jogador)
            posicao = input('Informe a jogada (ex: 1A, 2B): ')
            if self._tabuleiro.jogada(posicao, self._jogador):
                break

    def jogada_ia(self):
        # 1 - Se IA puder ganhar agora
        for (i, j) in self._tabuleiro.posicoes_vazias():
            self._tabuleiro._posicoes[i][j] = self._ia
            if self.eh_vencedor(self._ia):
                return  # faz jogada vencedora
            self._tabuleiro._posicoes[i][j] = ' '

        # 2 - Se humano puder ganhar, bloquear
        for (i, j) in self._tabuleiro.posicoes_vazias():
            self._tabuleiro._posicoes[i][j] = self._jogador
            if self.eh_vencedor(self._jogador):
                self._tabuleiro._posicoes[i][j] = self._ia
                return
            self._tabuleiro._posicoes[i][j] = ' '

        # 3 - Jogada aleatória
        i, j = choice(self._tabuleiro.posicoes_vazias())
        self._tabuleiro._posicoes[i][j] = self._ia

    def jogar(self):
        while self._tabuleiro.tem_jogada():
            # Jogador humano (X)
            self.jogada_humana()
            if self.eh_vencedor(self._jogador):
                self.imprime()
                print('\nFim de Jogo!')
                print('Vitória do jogador', self._jogador)
                return

            if not self._tabuleiro.tem_jogada():
                break

            # Jogada da IA (O)
            self.jogada_ia()
            if self.eh_vencedor(self._ia):
                self.imprime()
                print('\nFim de Jogo!')
                print('Vitória da IA (O)')
                return

        self.imprime()
        print('Jogo empatado!')

if __name__ == '__main__':
    jogo = Velha()
    jogo.jogar()
