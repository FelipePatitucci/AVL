"""

      __      ___      
     /\ \    / / |     
    /  \ \  / /| |     
   / /\ \ \/ / | |     
  / ____ \  /  | |____ 
 /_/    \_\/   |______|

Integrantes:
Felipe Patitucci              - 120022269
Igor Torres                   - 119034669
Matheus Moreira do Nascimento - 119042060
Pedro Wong                    - 120076810
Ruan Felipe da Silva e Sousa  - 119041454
"""

from lib.AVL import AVLTree
import time
import pandas as pd

if __name__ == '__main__':
    # testando a árvore
    print('AVL teste com números de 1 a 100')
    avl_teste = AVLTree()
    for val in range(1,101):
        avl_teste.insert(val, val+100)
    avl_teste.printAVL()

    # BASE PEQUENA
    # Construindo índice para AVL
    avl = AVLTree()
    avl.cria_indice(arquivo='anime_databases.csv', delimiter=";", pk_column=1, header=True)


    # Teste 1 : recuperando dados usando a chave primaria
    # usando AVL:
    inicio = time.time()
    registro_bocchi_avl = avl.procura_chave(chave='Bocchi the Rock!', file_name='anime_database.csv')
    fim = time.time()
    print(f'Registro encontrado! Levou{fim - inicio: .3f} segundos para encontrar usando AVL.')

    # usando Pandas:
    df = pd.read_csv('anime_database.csv', sep=';')
    inicio = time.time()
    registro_bocchi_pd = df[df['title'] == 'Bocchi The Rock!']
    fim = time.time()
    print(f'Registro encontrado! Levou{fim - inicio: .3f} segundos para encontrar usando pandas.')

    # método de força bruta
    inicio = time.time()
    with open('anime_database.csv', encoding='utf-8') as arq:
        for linha, conteudo in enumerate(arq):
            data = conteudo.split(';')
            if data[0] == '47917':
                fim = time.time()
                print(f'Registro encontrado! Levou{fim - inicio: .3f} segundos para encontrar usando força bruta.')
                break
    
    print(f'Registro: {registro_bocchi_avl}')


    # Teste 2: recuperando registros dado um intervalo de chaves
    # usando AVL:
    inicio = time.time()
    registros_avl = avl.procura_intervalo_chaves(chave_inicial='Fruits Basket', chave_final='Mirai Nikki',  file_name='anime_database.csv')
    fim = time.time()
    print(f'Registros encontrados! Levou{fim - inicio: .3f} segundos para encontrar usando AVL.')

    # usando Pandas
    df = pd.read_csv('anime_database.csv', sep=';')
    inicio = time.time()
    registros_pd = df[(df['title'] >= 'Fruits Basket') & (df['title'] <= 'Mirai Nikki')]
    fim = time.time()
    print(f'Registros encontrados! Levou{fim - inicio: .3f} segundos para encontrar usando pandas.')

    # método de força bruta
    inicio = time.time()
    registros_brute = []
    with open('anime_database.csv', encoding='utf-8') as arq:
        for linha, conteudo in enumerate(arq):
            data = conteudo.split(';')
            if data[1] >= 'Fruits Basket' and data[1] <= 'Mirai Nikki':
                registros_brute.append(linha)
        fim = time.time()
        print(f'Registros encontrados! Levou{fim - inicio: .3f} segundos para encontrar usando força bruta.')

    input('Aperte enter para encerrar.')
