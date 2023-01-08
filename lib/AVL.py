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

from typing import List, Union, Optional
from itertools import islice
import time
from .helpers import get_registros

class Node:
	def __init__(self, dado: Union[str, int], linha: int):
		self.dado: Union[str, int] = dado
		self.pai: Optional[Node] = None
		self.esquerda: Optional[Node] = None
		self.direita: Optional[Node] = None
		self.linha: int = linha
		self.bf: int = 0  # fator de balanço, diferença de altura entre subarvore esquerda e direita


class AVLTree:
	def __init__(self):
		self.raiz: Optional[Node] = None

	def __print_auxiliar(self, node_atual: Node, indentacao: str, ultimo: bool) -> None:
		if node_atual != None:
			print(indentacao, end='')
			if ultimo:
				print("R----", end='')
				indentacao += "     "
			else:
				print("L----", end='')
				indentacao += "|    "

			print(node_atual.dado)
			self.__print_auxiliar(node_atual.esquerda, indentacao, False)
			self.__print_auxiliar(node_atual.direita, indentacao, True)
	
	def __busca_auxiliar(self, node: Node, chave: Union[str, int]) -> Node:
		if node == None:
			print(f'Registro "{chave}" não existe na base.')
			return node
		
		if chave == node.dado:
			print(f'Registro "{chave}" encontrado.')
			return node

		if chave < node.dado:
			return self.__busca_auxiliar(node.esquerda, chave)
		return self.__busca_auxiliar(node.direita, chave)
	
	def __rotacao_esquerda(self, node: Node) -> None:
		aux = node.direita
		node.direita = aux.esquerda
		if aux.esquerda != None:
			aux.esquerda.pai = node

		aux.pai = node.pai
		if node.pai == None:
			self.raiz = aux
		elif node == node.pai.esquerda:
			node.pai.esquerda = aux
		else:
			node.pai.direita = aux
		aux.esquerda = node
		node.pai = aux
		# atualiza o fator de balanço
		node.bf = node.bf - 1 - max(0, aux.bf)
		aux.bf = aux.bf - 1 + min(0, node.bf)

	def __rotacao_direita(self, node) -> None:
		aux = node.esquerda
		node.esquerda = aux.direita
		if aux.direita != None:
			aux.direita.pai = node
		
		aux.pai = node.pai
		if node.pai == None:
			self.raiz = aux
		elif node == node.pai.direita:
			node.pai.direita = aux
		else:
			node.pai.esquerda = aux
		
		aux.direita = node
		node.pai = aux
		# atualiza o fator de balanço
		node.bf = node.bf + 1 - min(0, aux.bf)
		aux.bf = aux.bf + 1 + max(0, node.bf)

	def __balanceamento(self, node: Node) -> None:
		if node.bf > 0:
			if node.direita.bf < 0:
				self.__rotacao_direita(node.direita)
				self.__rotacao_esquerda(node)
			else:
				self.__rotacao_esquerda(node)
		elif node.bf < 0:
			if node.esquerda.bf > 0:
				self.__rotacao_esquerda(node.esquerda)
				self.__rotacao_direita(node)
			else:
				self.__rotacao_direita(node)

	def __atualiza_balanceamento(self, node: Node) -> None:
		if abs(node.bf) > 1:
			self.__balanceamento(node)
			return

		if node.pai != None:
			if node == node.pai.esquerda:
				node.pai.bf -= 1

			if node == node.pai.direita:
				node.pai.bf += 1

			if node.pai.bf != 0:
				self.__atualiza_balanceamento(node.pai)

	def __percorrer_auxiliar(self, node: Node) -> None:
		if node != None:
			self.__percorrer_auxiliar(node.esquerda)
			print(f'{node.dado} ')
			self.__percorrer_auxiliar(node.direita)

	def __menor_chave(self, node: Node) -> Node:
		while node.esquerda != None:
			node = node.esquerda
		return node

	def __maior_chave(self, node: Node) -> Node:
		while node.direita != None:
			node = node.direita
		return node

	def __pega_registro(self, file_name: str, node: Node) -> str:
		# ler só uma linha específica, sem trazer o arquivo todo pra memória
		with open(f'{file_name}', encoding='utf-8') as lines:
			linha = int(node.linha)
			for line in islice(lines, linha, linha+1):
				return line
	
	def __pega_linhas(self, left: Union[str, int], right: Union[str, int]) -> List[int]:
		start = self.raiz
		lista = []
		def __pega_nodes(node: Node) -> None:
			if left <= node.dado <= right:
				lista.append(node.linha)
			if node.dado > left and node.esquerda != None:
				__pega_nodes(node.esquerda)
			if node.dado < right and node.direita != None:
				__pega_nodes(node.direita)
		__pega_nodes(start)
		return lista

	# Percorre a árvore na ordem crescente de chaves
	def percorrer_AVL(self) -> None:
		self.__percorrer_auxiliar(self.raiz)

	def procura_node(self, chave:Union[str, int]) -> Node:
		return self.__busca_auxiliar(self.raiz, chave)
 
	# procura pela chave e retorna o registro
	def procura_chave(self, chave: Union[str, int], file_name: str) -> str:
		node = self.__busca_auxiliar(self.raiz, chave)
		if isinstance(node, type(None)):
			print('A chave informada não existe no registro.')
			return
		return self.__pega_registro(file_name=file_name, node=node)

	# procura todos os registros com chaves em um range de duas chaves
	def procura_intervalo_chaves(self, chave_inicial: Union[str, int], chave_final: Union[str, int],file_name: str) -> List[str]:
		node_inicial = self.__busca_auxiliar(self.raiz, chave_inicial)
		node_final = self.__busca_auxiliar(self.raiz, chave_final)

		if isinstance(node_final, type(None)) or isinstance(node_inicial, type(None)):
			print('Uma das chaves informadas não existe na base.')
			return []

		registros = []
		filhos = self.__pega_linhas(node_inicial.dado, node_final.dado)
		arq = open(f'{file_name}', encoding='utf-8')
		texto = arq.read().split("\n")
		arq.close()
		for linha in filhos:
			try:
				registros.append(texto[linha])
			except TypeError:
				print(f'O registro de linha {linha} provavelmente foi inserido manualmente e por isso não existe no registro.')

		print(f'{len(registros)} registros foram encontrados entre {chave_inicial} e {chave_final}.')
		return registros

	def successor(self, node: Node) -> Node:
		# se tiver subarvore a direita, o sucessor é o nó mais a esquerda dessa subarvore
		if node.direita != None:
			return self.__menor_chave(node.direita)

		# caso n tenha, é o menor parente
		no_pai = node.pai
		while no_pai != None and node == no_pai.direita:
			node = no_pai
			no_pai = no_pai.pai
		return no_pai

	def antecessor(self, node: Node) -> Node:
		# se tiver subarvore a esquerda, o antecessor é o nó mais a direita dessa subarvore
		if node.esquerda != None:
			return self.__maior_chave(node.esquerda)

		# caso n tenha, é o menor parente
		no_pai = node.pai
		while no_pai != None and node == no_pai.esquerda:
			node = no_pai
			no_pai = no_pai.pai
		return no_pai

	# inserir a chave na posição correta e balancear se necessário
	def insert(self, chave: Union[str, int], linha: int, printar=False) -> None:
		node = Node(chave, linha)
		aux = None
		raiz = self.raiz
		while raiz != None:
			aux = raiz
			if node.dado < raiz.dado:
				raiz = raiz.esquerda
			else:
				raiz = raiz.direita

		node.pai = aux
		if aux == None:
			self.raiz = node
		elif node.dado < aux.dado:
			aux.esquerda = node
		else:
			aux.direita = node
		self.__atualiza_balanceamento(node)
		if printar:
			print('Registro adicionado na AVL!')

	# print melhorzinho
	def printAVL(self) -> None:
		self.__print_auxiliar(node_atual=self.raiz, indentacao="", ultimo=True)
	
	def cria_indice(self, arquivo: str, delimiter: str, pk_column: int, header=True) -> None:
		inicio = time.time()
		index_list = get_registros(arquivo, delimiter, pk_column, header)
		for linha, chave in enumerate(index_list):
			self.insert(chave, linha+int(header))
		fim = time.time()
		print(f'Indice construído! Levou {fim - inicio: .3f} segundos para {len(index_list)} registros.')
		return
