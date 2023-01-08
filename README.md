# AVL como índice

## Introdução:

Membros do grupo

- Felipe Patitucci
  $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$
  DRE: 120022269
- Igor Torres
  $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$
  DRE: 119034669
- Matheus Moreira do Nascimento
  $\:\:\:$
  DRE: 119042060
- Pedro Wong
  $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$
  DRE: 120076810
- Ruan Felipe da Silva e Sousa $\:\:\:\:\:\:\:\:\:\:\:$
  DRE: 119041454

O programa implementa uma AVL em Python utilizando programação orientada a objeto.
Ela é populada a partir de uma base de dados que pode ser passada como parâmetro pelo usuário.

## Objetos e seus métodos:

Node: Esse é o objeto que descreve um nó genérico (seja galho ou folha) da AVL.

- Atributos:

  - dado : chave primária que será usada para consulta de dados no arquivo
  - linha : referência para a localização da chave primária no arquivo
  - pai : Node que representa o pai, se houver (default: None)
  - esquerda : Node que representa o filho esquerdo, se houver (default: None)
  - direita : Node que representa o filho direito, se houver (default: None)
  - bf : fator de balanço, diferença de altura entre subarvore esquerda e direita (default: 0)

- Métodos:
  - Nenhum

AVLTree: Esse é o objeto que representa a árvore em si.

- Atributos:

  - raiz : Node que representa a raiz da AVL, se possuir (default: None)

- Métodos
  - \_\_print_auxiliar: Função interna recursiva para printar AVL de forma organizada
  - \_\_busca_auxiliar: Função interna recursiva que procura um Node na AVL dada uma chave
  - \_\_percorrer_auxiliar: Função interna recursiva para percorrer os Nodes da AVL do menor até o maior
  - \_\_balanceamento: Função interna para a lógica de balanceamento da AVL após inserção de novo Node
  - \_\_atualiza_balanceamento: Função interna recursiva para atualizar o fator de balanço de um Node
  - \_\_rotacao_direita: Função interna para fazer a rotação da AVL para direita em um certo Node
  - \_\_rotacao_esquerda: Função interna para fazer a rotação da AVL para esquerda em um certo Node
  - \_\_menor_chave: Função interna que retorna o Node com a menor chave em uma subtree
  - \_\_maior_chave: Função interna que retorna o Node com a maior chave em uma subtree
  - \_\_pega_registro: Função interna para encontrar um registro no arquivo dado um Node
  - \_\_pega_linhas: Função interna recursiva para pegar todas os Nodes da AVL que estão entre duas chaves específicas (retorna uma lista com a linha de referência no arquivo para cada Node)
  - percorrer_AVL: Função que printa todas as chaves da AVL percorrendo-a da menor para a maior
  - procura_node: Função que retorna um Node dada uma chave
  - procura_chave: Função que procura um registro no arquivo dada sua chave da AVL
  - procura_intervalo_chaves: Função que pega todos os registros que possuem chave primária entre dois valores
  - sucessor: Função que retorna o Node sucessor dado um Node
  - antecessor: Função que retorna o Node antecessor dado um Node
  - insert: Função que insere um Node na AVL dado uma chave e uma linha
  - print_AVL: Função que printa a estrutura da AVL
  - cria_indice: Função que cria um índice para um arquivo, com base na pk, usando a AVL

## Projeto Funcional:

Ao iniciar, o programa solicita o nome do arquivo que deverá ser escaneado para
a criação da AVL. Além disso, também será requisitado o separador (; , ? etc) do arquivo, o índice da coluna que deverá ser usada como chave primária (contagem começa do 0) e se o arquivo possuir header.

Se nenhum nome for passado, ou o arquivo não existir, a AVL será criada usando a base "anime_database", usando a coluna "title_name" como pk.

Após isso, uma lista de opções será exibida.

## Requisitos Para Uso

Necessario python instalado.

**Comando para baixar as bibliotecas:**

```sh
pip install -r requirements.txt
```

## Como Utilizar:

**Comando para execução:**

```sh
python main.py
```

**Caso queira rodar os testes de comparação feitos:**

```sh
python comparacao.py
```
