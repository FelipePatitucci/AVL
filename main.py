from lib.helpers import get_registros
from lib.AVL import AVLTree
import time
import pandas as pd

# Construindo índice para AVL
# trocar header por False caso arquivo não tenha header
# pk_column é o índice da coluna que é chave primária do arquivo (começa do 0)
index = get_registros(arquivo='anime_database.csv', delimiter=";", pk_column=1, header=True)
avl = AVLTree()
avl.build_index(index_list=index, header=True)


# Teste 1 : recuperando dados usando a chave primaria
# usando AVL:
inicio = time.time()
registro_bocchi_avl = avl.procuraChave(chave='Bocchi the Rock!', file_name='anime_database.csv')
fim = time.time()
print(f'Registro encontrado! Levou{fim - inicio: .3f} segundos para encontrar usando AVL.')

# usando Pandas:
df = pd.read_csv('anime_database.csv', sep=';')
inicio = time.time()
registro_bocchi_pd = df[df['title'] == 'Bocchi The Rock!']
fim = time.time()
print(f'Registro encontrado! Levou{fim - inicio: .3f} segundos para encontrar usando pandas.')

# Teste 2: recuperando registros dado um intervalo de chaves
# usando AVL:
inicio = time.time()
registros_avl = avl.procuraIntervaloChaves(chave_inicial='A Kite', chave_final='Wish', file_name='anime_database.csv')
fim = time.time()
print(f'Registros encontrados! Levou{fim - inicio: .3f} segundos para encontrar usando AVL.')

# usando Pandas
df = pd.read_csv('anime_database.csv', sep=';')
inicio = time.time()
# df = df.sort_values(by='title')
registros_pd = df[(df['title'] >= 'A Kite') & (df['title'] <= 'Wish')]
fim = time.time()
print(f'Registros encontrados! Levou{fim - inicio: .3f} segundos para encontrar usando pandas.')
print(len(registros_pd))