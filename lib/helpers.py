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
