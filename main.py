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

import os
from lib.AVL import AVLTree

def main():
    arquivos = [arq for arq in os.listdir() if arq.split('.')[-1] == 'csv']
    print(f'Foram encontrados {len(arquivos)} .csv nesse diretório.')
    for linha, arq in enumerate(arquivos):
        print(f'{linha+1}: {arq}')
    escolhido = int(input('Digite o número do arquivo que será usado para gerar a AVL.'))
    while escolhido not in [i for i in range(1,len(arquivos)+1)]:
        print('Número inválido. Favor tentar novamente')
        escolhido = int(input('Digite o número do arquivo que será usado para gerar a AVL.'))
    arquivo = arquivos[escolhido-1]
    delimitador = input('Digite o delimitador do arquivo .csv a ser utilizado.')
    pk_col = int(input('Digite o índice da coluna de chave primária do arquivo .csv a ser utilizado. Se é a primeira coluna, digite 0, por exemplo.'))
    header = input('Se o arquivo possui header, digite sim. Caso contrário, digite nao.')
    avl = AVLTree()
    if header.lower() in ('sim', 's'):
        header = True
    else:
        header = False
    try:
        avl.cria_indice(arquivo, delimitador, pk_col, header)
    except FileNotFoundError:
        print('O caminho passado não existe ou está incorreto. Usando .csv padrão.')
        avl.cria_indice('anime_database.csv', ';', 1, True)
    processando = True
    while processando:
        break
    return


if __name__ == '__main__':
    main()
