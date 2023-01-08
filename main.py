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
    print(f'Foram encontrados {len(arquivos)} arquivo(s) .csv nesse diretório.')
    for linha, arq in enumerate(arquivos):
        print(f'{linha+1}: {arq}')
    escolhido = int(input('Digite o número do arquivo que será usado para gerar a AVL: '))
    while escolhido not in [i for i in range(1,len(arquivos)+1)]:
        print('Número inválido. Favor tentar novamente')
        escolhido = int(input('Digite o número do arquivo que será usado para gerar a AVL: '))
    arquivo = arquivos[escolhido-1]
    delimitador = input('Digite o delimitador do arquivo .csv a ser utilizado: ')
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
        print('Opções disponíveis:')
        print('1 - Inserir novo Node por chave')
        print('2 - Consultar node da AVL por chave')
        print('3 - Consultar registro da base de dados por chave')
        print('4 - Consultar registros da base de dados em um intervalo de chaves')
        print('5 - Sair')
        escolha = int(input('Escolha a opção que desejar: '))
        if escolha == 1:
            new_key = input('Digite a chave que deseja inserir: ')
            new_line = input(f'Digite a linha de referência no registro para a chave {new_key}: ')
            if avl.procura_node(new_key):
                print('Essa chave já existe na AVL.')
            else:
                avl.insert(chave=new_key, linha=new_line, printar=True)
        elif escolha == 2:
            new_key = input('Digite a chave que deseja consultar: ')
            node = avl.procura_node(chave=new_key)
            print(f'Chave buscada: {new_key}')
            print(f'Linha da chave buscada: {node.linha}')
            if node.pai != None:
                print(f'Dado do Pai: {node.pai.dado}')
            else:
                print('Não possui node pai.')
            if node.esquerda != None:
                print(f'Dado do Filho esquerdo: {node.esquerda.dado}')
            else:
                print('Não possui filho esquerdo.')
            if node.direita != None:
                print(f'Dado do Filho direito: {node.direita.dado}')
            else:
                print('Não possui filho direito.')
        elif escolha == 3:
            chave = input('Digite a chave que deseja encontrar o registro: ')
            registro = avl.procura_chave(chave=chave, file_name=arquivo)
            if registro != None:
                print(registro)
        elif escolha == 4:
            chave_inicial = input('Digite a chave inicial: ')
            chave_final = input('Digite a chave final: ')
            registros = avl.procura_intervalo_chaves(chave_inicial, chave_final, arquivo)
            if len(registros):
                print('Printando os 10 primeiros:')
                for reg in registros[:10]:
                    print(reg)
                    print()
                esc = input('Se isso for suficiente e quiser voltar às opções, basta digitar 1. Se quiser ver os outros registros, basta digitar qualquer outra coisa.')
                if esc != '1':
                    for reg in registros[10:]:
                        print(reg)
                        print()
        elif escolha == 5:
            processando = False
        else:
            print('Escolha inválida!')
    return


if __name__ == '__main__':
    main()
