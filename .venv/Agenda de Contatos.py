import csv
from os.path import isfile

#Escreve uma linha na tela
def linha():
    print('-'*50)

class Contato:
    #Campos dos contatos
    campos =  ['Nome', 'Telefone', 'Aniversário']
    def __init__(self, valores):
        #Inicializa dicionario para os campos
        self._dic = {}
        #Percorre a lista de campos
        for cont, camp in enumerate (self.campos):
            #Atribui o valor correspondente ao campo
            self._dic[campo] = valores[cont]

    def alterar(self):
        linha()
        print('Alteração de contato')
        linha()
        #Percorre campos
        for campo, valor in sef._dic.items():
            #Mostra o campo como valor atual
            print(campo + ' ('+valor+')', sep='')
            #Pega novo valor
            novo_valor = input('Novo valor: ').strip()
            #Verifica se o valor é diferente de ''
            if novo_valor != '':
                #Atribui novo valor ao campo
                self._dic[campo] = novo_valor
    @property
    def valores(self):
        #Retorna lista com valores dos campos
        lista_valores = []
        for campo in self.campos:
            lista_valores.append(self.di)
        return lista_valores

    def __str__(self):
        #Str com campo e valores
        lista_cv = [campo + ': ' + self._dic[campo]
                    for campo in self._dic]
        return '\n' .join(lista_cv)

    def __lt__(self, other):
        #Comparação < (Necessário para ordenar a lista de contatos)
        return tuple(self.valores) < tuple(other.valores)

    @classmethod
    def novo(cls):
        linha()
        print('Novo contato')
        linha()
        #Lista de valores
        lista_valores = []
        for campo in cls.campos:
            #Obtém o valor de cada campo
            valor = input(campo + ': ').strip()
            #Adiciona à lista de valores
            lista_valores.append(valor)
        #Verifica se o nome ficou vazio
        if len(lista_valores[0]) == 0:
            print('Contato inválido, o nome é obrigatório ')
            #Não cria contato com nome vazio
            return None
        else:
            #Cria o contato
            return Contato(lista_valores)

class Arquivo:
    def __init__(self, nome_arquivo):
        #Nome do arquivo e lista de contatos
        self._nome_arquivo = nome_arquivo
        self._lista_contatos = []
        #Checa se o arquivo existe
        if isfile(self._nome_arquivo):
            #Abre o arquivo para leitura
            with open(self._nome_arquivo) as arq:
                #Criar leitor de CSV
                leitor = csv.reader(arq)
                #Ignora linha do cabeçalho
                next(leitor)
                #Percorre as linhas usando o leitor
                for linha in leitor:
                    #Cria o contato e adiciona a lista
                    contato = contato(linha)
                    self._lista_contatos.append(contato)

    def listar(self):
        #verifica se a lista de contatos está vazia
        if len(self._lista_contatos) == 0:
            print('Nenhum contato cadastrado!')
            linha()
        else:
            #Ordena a lista de contatos
            self._lista_contatos.sort()
            #Percorre a lista de contatos
            for cont, contato in enumerate(self._lista_contatos):
                print('Código: ', cont)
                print(str(contato))
                linha()

    def buscar(self, codigo):
        #Busca contato pelo código
        if 0 <= codigo and codigo < len(self._lista_contatos):
            return self._lista_contatos[codigo]
        return None

    def incluir(self):
        #Cria novo contato
        contato = Contato.novo()
        #Testa se o contatao é válido
        if contato is not None:
            #Incluir na lista de contatos
            self._lista_contatos.append(contato)

    def excluir(self, codigo):
        #Verifica se o código do contato existe
        if 0 <= codigo and codigo <len(self._lista_contatos):
            #Remove da lista de contatos
            self._lista_contatos.pop(codigo)

    def salvar(self):
        #Abre o arquivo para escrita
        with open(self._nome_arquivo, 'w') as arq:
            #Cria escritor CSV
            escritor = csv.writer(arq)
            #Escreve cabeçalho
            escritor.writerow(Contato.campos)
            #Percorre a lista de contatos
            for contato in self._lista_contatos:
                #Escreve cada contato
                escritor.writerow(contato.valores)

class Agenda:
    def __init__(self, nome_arquivo):
        #cria objeto associado ao arquivo
        self._arq = Arquivo(nome_arquivo)

    def menu(self):
        #Menu que lista e recebe a opção do úsuario
        linha()
        print("Agenda de contatos")
        linha()
        self._arq.listar()
        print('(I)ncluir | (E)xcluir | (A)lterar | (S)alvar | Sai(R)')
        return input('Informe a opção desejada: ').strip().lower()

    def executar(self):
        while True:
            resp = self.menu()
            if resp == 'i':
                self._arq.incluir()
            elif resp == 'e':
                codigo = int(input('Código do contato'))
                self._arq.excluir(codigo)
            elif resp == 'a':
                codigo = int(input('Codigo do contato'))
                #Busca contato
                contato = self._arq.buscar(codigo)
                #Testa se o contato foi encontrado
                if contato is not None:
                    contato.alterar()
            elif resp == 's':
                self._arq.salvar()
            elif resp == 'r':
                break

if __name__ == '__main__':
    agenda = Agenda('contatos.csv')
    agenda.executar()
