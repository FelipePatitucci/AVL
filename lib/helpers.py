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

from typing import List
import csv

def get_registros(arquivo: str, delimiter: str, pk_column: int, header=True) -> List[str]:
    """
    Lê um arquivo em formato .csv e retorna os uma lista com os valores da coluna de índice pk_column.
    Se o arquivo não tiver header, basta colocar o parâmetro header como False.
    """
    registros = []
    with open(f"{arquivo}", encoding='utf-8') as f:
        reader = csv.reader(f, quotechar='"', delimiter=delimiter,
                     quoting=csv.QUOTE_ALL)
        for linha in reader:
            if header:
                header = False
                continue
            registros.append(linha[pk_column])
    return registros
