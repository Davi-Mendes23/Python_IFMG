# Análise Geral do Projeto
O projeto como um todo demonstra uma boa compreensão de conceitos fundamentais da programação em Python, incluindo:

 - Programação Orientada a Objetos (POO): Todos os arquivos utilizam classes para modelar as entidades principais de cada sistema (ex: Contato, Tabuleiro, Arvore). Isso organiza o código de forma lógica e reutilizável.

 - Manipulação de Arquivos: O projeto utiliza diferentes formatos de arquivo para persistência de dados. A agenda de contatos salva as informações em formato CSV, enquanto a árvore genealógica utiliza JSON, mostrando versatilidade no tratamento de dados.

 - Interação com o Usuário: Todos os programas são projetados para serem executados em um terminal (console) e possuem menus interativos que guiam o usuário através das funcionalidades.

 - Estrutura de Dados: Utiliza estruturas de dados como listas e dicionários de forma eficaz para armazenar e gerenciar informações em memória.

# Detalhamento dos Programas
## 1. Agenda de Contatos (Agenda de Contatos.py)
Este programa implementa uma agenda de contatos simples, porém funcional, com as seguintes características:
 - Classe Contato: Modela um contato com os campos "Nome", "Telefone" e "Aniversário". O nome é um campo obrigatório para a validação.
 - Classe Arquivo: Gerencia a leitura e a escrita dos contatos em um arquivo chamado contatos.csv. O código demonstra boas práticas, como o uso de newline='' e encoding='utf-8' para evitar problemas de formatação e acentuação no arquivo CSV.
 - Funcionalidades:
   - Inclusão, exclusão e alteração: Permite ao usuário adicionar novos contatos, remover existentes por um código numérico e alterar informações de um contato.
   - Listagem Ordenada: Os contatos são sempre exibidos em ordem alfabética pelo nome.
   - Persistência de Dados: As alterações são salvas no arquivo contatos.csv quando o usuário seleciona a opção "Salvar".
 - Melhorias Notáveis: O código inclui comentários que apontam correções e melhorias, como o tratamento de erro para entradas não numéricas ao selecionar um contato para alteração ou exclusão.

## 2. Jogo da Velha (Duas Versões)
Existem duas implementações do Jogo da Velha, uma para dois jogadores humanos e outra com um adversário controlado por Inteligência Artificial (IA).
 - a) Jogo da velha.py (Jogador vs. Jogador)
   - Estrutura: Utiliza uma classe Tabuleiro para representar o estado do jogo e uma classe Velha para controlar o fluxo da partida.
   - Jogabilidade: Dois jogadores, 'X' e 'O', se alternam para fazer suas jogadas. O jogador inicial é escolhido aleatoriamente. O programa valida as jogadas e anuncia o vencedor ou um empate.
 - b) Jogo da Velha (IA).py (Jogador vs. IA)
Esta versão é uma evolução da anterior, com a adição de um oponente controlado pelo computador.
   - Lógica da IA: O método jogada_ia implementa uma estratégia de jogo em três etapas hierárquicas:
   - Verifica se pode vencer: A IA primeiro analisa o tabuleiro para ver se consegue vencer na jogada atual e, se possível, realiza o movimento vitorioso.
   - Bloqueia o oponente: Se não puder vencer, a IA verifica se o jogador humano pode ganhar na próxima rodada e, em caso afirmativo, joga para bloquear essa vitória.
   - Jogada aleatória: Se nenhuma das condições acima for atendida, a IA faz uma jogada aleatória em uma das posições vazias disponíveis.
 - Jogabilidade: O jogador humano sempre joga com 'X' e a IA com 'O'. O fluxo do jogo alterna entre a jogada humana e a da IA até que haja um vencedor ou empate.

## 3. Árvore Genealógica (Arvore Genealogica.py)
Este é o programa mais complexo do projeto, implementando um sistema para registrar e visualizar relações de parentesco.
 - Estrutura de Dados: Utiliza um dicionário para representar a árvore, onde cada chave é o nome de uma pessoa e o valor é outro dicionário contendo as chaves "Pai" e "Mãe".
 - Persistência: Os dados são salvos em um arquivo arvore.json, o que permite preservar a estrutura hierárquica das relações de forma eficiente.
 - Funcionalidades:
   - Manipulação de Pessoas: Permite incluir e excluir pessoas. Uma regra de negócio importante impede a exclusão de uma pessoa que seja pai ou mãe de outra já cadastrada.
   - Definição de Parentesco: O usuário pode definir ou alterar o pai e a mãe de uma pessoa, com a validação de que os pais informados já devem existir na árvore.
   - Visualização Recursiva: Possui funções recursivas para exibir os ancestrais (pais, avós, etc.) e os descendentes (filhos, netos, etc.) de uma pessoa, formatando a saída com indentação para criar uma visualização de árvore no console.
- Interface: Apresenta um menu claro e completo para que o usuário possa interagir com todas as funcionalidades do sistema.
