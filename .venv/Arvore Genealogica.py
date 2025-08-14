import json
from os.path import isfile

# Constantes para as chaves do dicionário
PAI = 'Pai'
MAE = 'Mãe'


def linha():
    """Imprime uma linha separadora no console para organização."""
    print('-' * 50)


class Arvore:
    """
    Classe que gerencia uma árvore genealógica, permitindo incluir,
    excluir, listar pessoas e seus parentescos.
    """

    def __init__(self, nome_arquivo):
        """
        Inicializa a árvore genealógica.
        Carrega os dados de um arquivo JSON se ele existir.
        """
        self._nome_arquivo = nome_arquivo
        self._arvore = {}
        # Checa se o arquivo de dados já existe
        if isfile(self._nome_arquivo):
            # Abre o arquivo para leitura com codificação UTF-8
            with open(self._nome_arquivo, 'r', encoding='utf-8') as arq:
                self._arvore = json.load(arq)

    def incluir(self, nome):
        """Inclui uma nova pessoa na árvore."""
        # Verifica se o nome é uma string vazia
        if not nome:
            print('Erro: Nome inválido!')
        # Verifica se a pessoa já está cadastrada
        elif nome in self._arvore:
            print(f'Erro: "{nome}" já está cadastrado(a)!')
        else:
            # Adiciona a nova pessoa ao dicionário da árvore
            self._arvore[nome] = {PAI: '', MAE: ''}
            print(f'"{nome}" foi incluído(a) com sucesso.')
        input("Pressione Enter para continuar...")

    def listar(self):
        """Lista todas as pessoas cadastradas na árvore."""
        if not self._arvore:
            print('Nenhuma pessoa cadastrada!')
            linha()
        else:
            # Ordena os nomes em ordem alfabética para exibição
            lista_nomes = sorted(list(self._arvore.keys()))
            for nome in lista_nomes:
                dados = self._arvore[nome]
                lista_dados = []
                # Adiciona pai e mãe à lista de dados se existirem
                if dados[PAI]:
                    lista_dados.append(f'Pai: {dados[PAI]}')
                if dados[MAE]:
                    lista_dados.append(f'Mãe: {dados[MAE]}')

                dados_str = f"({', '.join(lista_dados)})" if lista_dados else ""
                print(nome, dados_str)
                linha()

    def buscar(self, nome):
        """
        Busca uma pessoa na árvore.
        Retorna os dados da pessoa se encontrada, caso contrário, retorna None.
        """
        return self._arvore.get(nome)

    def alterar_pais(self, nome):
        """Define ou altera os pais de uma pessoa."""
        pessoa = self.buscar(nome)
        if pessoa is not None:
            nome_pai = input(f'Informe o pai de {nome} (deixe em branco para remover): ').strip()
            nome_mae = input(f'Informe a mãe de {nome} (deixe em branco para remover): ').strip()

            # Verifica se o pai existe na árvore (a menos que o campo esteja vazio)
            if nome_pai and nome_pai not in self._arvore:
                print(f'Erro: O pai "{nome_pai}" não está cadastrado.')
            else:
                pessoa[PAI] = nome_pai

            # Verifica se a mãe existe na árvore (a menos que o campo esteja vazio)
            if nome_mae and nome_mae not in self._arvore:
                print(f'Erro: A mãe "{nome_mae}" não está cadastrada.')
            else:
                pessoa[MAE] = nome_mae

            print(f'Pais de "{nome}" atualizados.')
        else:
            print(f'Erro: Pessoa "{nome}" não encontrada!')
        input("Pressione Enter para continuar...")

    def excluir(self, nome):
        """Exclui uma pessoa, apenas se não for pai ou mãe de ninguém."""
        if self.buscar(nome) is None:
            print(f'Erro: Pessoa "{nome}" não encontrada!')
            input("Pressione Enter para continuar...")
            return

        # Verifica se a pessoa a ser excluída é pai ou mãe de alguém
        for outro, dados in self._arvore.items():
            if dados[PAI] == nome:
                print(f'Erro: "{nome}" é pai de "{outro}" e não pode ser excluído.')
                input("Pressione Enter para continuar...")
                return
            if dados[MAE] == nome:
                print(f'Erro: "{nome}" é mãe de "{outro}" e não pode ser excluída.')
                input("Pressione Enter para continuar...")
                return

        # Se não for parente, remove a pessoa
        self._arvore.pop(nome)
        print(f'"{nome}" foi excluído(a) com sucesso.')
        input("Pressione Enter para continuar...")

    def salvar(self):
        """Salva o estado atual da árvore no arquivo JSON."""
        # Abre o arquivo para escrita com codificação UTF-8
        with open(self._nome_arquivo, 'w', encoding='utf-8') as arq:
            json.dump(self._arvore, arq, indent=2, ensure_ascii=False)
        print('Árvore salva com sucesso!')
        input("Pressione Enter para continuar...")

    def ancestrais(self, nome, nivel=0):
        """Exibe os ancestrais de uma pessoa de forma recursiva."""
        pessoa = self.buscar(nome)
        if pessoa is not None:
            # Imprime o nome com indentação para criar a estrutura de árvore
            print('  ' * nivel + nome)
            # Chama a função para o pai e a mãe, se existirem
            if pessoa[PAI]:
                self.ancestrais(pessoa[PAI], nivel + 1)
            if pessoa[MAE]:
                self.ancestrais(pessoa[MAE], nivel + 1)

    def descendentes(self, nome, nivel=0):
        """Exibe os descendentes de uma pessoa de forma recursiva."""
        # Imprime o nome do ancestral com indentação
        print('  ' * nivel + nome)

        # Encontra todos os filhos diretos da pessoa atual
        filhos = []
        for pessoa, dados in self._arvore.items():
            if dados[PAI] == nome or dados[MAE] == nome:
                filhos.append(pessoa)

        # Para cada filho encontrado, chama a função recursivamente
        for filho in sorted(filhos):
            self.descendentes(filho, nivel + 1)

    def menu(self):
        """Exibe o menu de opções e retorna a escolha do usuário."""
        print('\n' * 3)
        linha()
        print('ÁRVORE GENEALÓGICA'.center(50))
        linha()
        self.listar()
        print('(+) Incluir   (-) Excluir    (P)ais')
        print('(A)ncestrais  (D)escendentes (S)alvar')
        print('sai(R)')
        linha()
        return input('Escolha uma opção: ').strip().lower()

    def executar(self):
        """Loop principal que executa o programa."""
        while True:
            opcao = self.menu()

            if opcao in ['+', '-', 'p', 'a', 'd']:
                nome = input('Informe o nome da pessoa: ').strip()
                if not nome:
                    print("O nome não pode ser vazio.")
                    input("Pressione Enter para continuar...")
                    continue

                if self.buscar(nome) is None and opcao not in ['+']:
                    print(f'Erro: Pessoa "{nome}" não encontrada!')
                    input("Pressione Enter para continuar...")
                    continue

                if opcao == '+':
                    self.incluir(nome)
                elif opcao == '-':
                    self.excluir(nome)
                elif opcao == 'p':
                    self.alterar_pais(nome)
                elif opcao == 'a':
                    linha();
                    print('Árvore de Ancestrais:');
                    linha()
                    self.ancestrais(nome)
                    linha();
                    input("Pressione Enter para continuar...")
                elif opcao == 'd':
                    linha();
                    print('Árvore de Descendentes:');
                    linha()
                    self.descendentes(nome)
                    linha();
                    input("Pressione Enter para continuar...")

            elif opcao == 's':
                self.salvar()
            elif opcao == 'r':
                print("Salvando e saindo...")
                self.salvar()
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")


if __name__ == '__main__':
    # Cria uma instância da classe Arvore, usando 'arvore.json' para salvar os dados
    arvore_genealogica = Arvore('arvore.json')
    arvore_genealogica.executar()
