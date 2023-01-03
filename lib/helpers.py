"""
Integrantes:
Felipe Patitucci - 120022269
Igor Torres - 119034669
Matheus Moreira do Nascimento - 119042060
Pedro Wong - 120076810
Ruan Felipe da Silva e Sousa - 119041454
"""

from typing import List

def get_registros(arquivo: str, delimiter: str, pk_column: int, header=True) -> List[str]:
    registros = []
    with open(f"{arquivo}", encoding='utf-8') as f:
        for linha, conteudo in enumerate(f):
            # skip header if needed
            if header and linha == 0:
                continue
            pk = conteudo.split(sep=delimiter)
            registros.append(pk[pk_column])
    return registros
