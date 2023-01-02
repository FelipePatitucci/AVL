from typing import List, Any, Union
from itertools import islice
import time

class Node:

	def __init__(self, dado: Union[str, int], linha: int):
		self.dado = dado
		self.pai = None
		self.esquerda = None
		self.direita = None
		self.linha = linha
		self.bf = 0  # fator de balanço, diferença de altura entre subarvore esquerda e direita

class AVLTree:

	def __init__(self):
		self.raiz = None

	def __printAuxiliar(self, node_atual: Node, indentacao: str, ultimo: bool) -> None:
		# printa a árvore
		if node_atual != None:
			print(indentacao, end='')
			if ultimo:
				print("R----", end='')
				indentacao += "     "
			else:
				print("L----", end='')
				indentacao += "|    "

			print(node_atual.dado)

			self.__printAuxiliar(node_atual.esquerda, indentacao, False)
			self.__printAuxiliar(node_atual.direita, indentacao, True)
	
	def __buscaAuxiliar(self, node: Node, chave: Union[str, int]) -> Node:
		# algoritmo recursivo
		if node == None:
			print(f'Registro "{chave}" não existe na base.')
			return node
		
		if chave == node.dado:
			print(f'Registro "{chave}" encontrado.')
			return node

		if chave < node.dado:
			return self.__buscaAuxiliar(node.esquerda, chave)
		return self.__buscaAuxiliar(node.direita, chave)


	def __balanceamento(self, node: Node) -> None:
		if node.bf > 0:
			if node.direita.bf < 0:
				self.rotacaoDireita(node.direita)
				self.rotacaoEsquerda(node)
			else:
				self.rotacaoEsquerda(node)
		elif node.bf < 0:
			if node.esquerda.bf > 0:
				self.rotacaoEsquerda(node.esquerda)
				self.rotacaoDireita(node)
			else:
				self.rotacaoDireita(node)


	def __atualizaBalanceamento(self, node: Node) -> None:
		if abs(node.bf) > 1:
			self.__balanceamento(node)
			return

		if node.pai != None:
			if node == node.pai.esquerda:
				node.pai.bf -= 1

			if node == node.pai.direita:
				node.pai.bf += 1

			if node.pai.bf != 0:
				self.__atualizaBalanceamento(node.pai)


	def __percorrerOrdemAuxiliar(self, node: Node) -> None:
		if node != None:
			self.__percorrerOrdemAuxiliar(node.esquerda)
			print(f'{node.dado} ')
			self.__percorrerOrdemAuxiliar(node.direita)

	def __pegaRegistro(self, file_name: str, node: Node) -> str:
		# ler só uma linha específica, sem trazer o arquivo todo pra memória
		with open(f'{file_name}', encoding='utf-8') as lines:
			linha = int(node.linha)
			for line in islice(lines, linha, linha+1):
				return line
		
	# Percorre a árvore na ordem
	# subarvore esquerda -> Node -> subarvore direita
	def emOrdem(self) -> None:
		self.__percorrerOrdemAuxiliar(self.raiz)

	# procura pela chave e retorna o node
	def procuraChave(self, chave: Any, file_name: str) -> str:
		node = self.__buscaAuxiliar(self.raiz, chave)
		if isinstance(node, type(None)):
			print('A chave informada não existe no registro.')
			return
		return self.__pegaRegistro(file_name=file_name, node=node)

	def procuraIntervaloChaves(self, chave_inicial: Union[str, int], chave_final: Union[str, int], file_name: str) -> List[str]:

		node_inicial = self.__buscaAuxiliar(self.raiz, chave_inicial)
		node_final = self.__buscaAuxiliar(self.raiz, chave_final)

		if isinstance(node_final, type(None)) or isinstance(node_inicial, type(None)):
			print('Uma das chaves informadas não existe na base.')
			return []
		# pode ser que o usuário deliberadamente digite na ordem invertida
		if node_inicial.dado > node_final.dado:
			node_inicial, node_final = node_final, node_inicial

		registros = []
		# adicionar o registro da primeira chave
		registros.append(self.__pegaRegistro(file_name=file_name, node=node_inicial))

		node_atual = node_inicial
		# adicionar todos os outros registros no intervalo das chaves
		while node_atual.dado != node_final.dado:
			prox_node = self.successor(node_atual)
			registros.append(self.__pegaRegistro(file_name=file_name, node=prox_node))
			node_atual = prox_node

		print(f'{len(registros)} registros foram encontrados entre {chave_inicial} e {chave_final}.')
		return registros

	# nó com a menor chave
	def menorChave(self, node: Node) -> Node:
		while node.esquerda != None:
			node = node.esquerda
		return node

	# nó com a maior chave
	def maiorChave(self, node: Node) -> Node:
		while node.direita != None:
			node = node.direita
		return node

	# successor do nó
	def successor(self, node: Node) -> Node:
		# se tiver subarvore a direita, o sucessor é o nó mais a esquerda dessa subarvore
		if node.direita != None:
			return self.menorChave(node.direita)

		# caso n tenha, é o menor parente
		no_pai = node.pai
		while no_pai != None and node == no_pai.direita:
			node = no_pai
			no_pai = no_pai.pai
		return no_pai

	# antecessor do nó
	def antecessor(self, node: Node) -> Node:
		# se tiver subarvore a esquerda, o antecessor é o nó mais a direita dessa subarvore
		if node.esquerda != None:
			return self.maiorChave(node.esquerda)

		# caso n tenha, é o menor parente
		no_pai = node.pai
		while no_pai != None and node == no_pai.esquerda:
			node = no_pai
			no_pai = no_pai.pai
		return no_pai

	# rotacao a esquerda para o nó
	def rotacaoEsquerda(self, node: Node) -> None:
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


	# rotacao a direita no nó
	def rotacaoDireita(self, node) -> None:
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

	# inserir a chave na posição e balancear se necessário
	def insert(self, chave: Union[str, int], linha: int) -> None:

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

		# a função checa se será necessário
		self.__atualizaBalanceamento(node)


	# print melhorzinho
	def printAVL(self) -> None:
		self.__printAuxiliar(node_atual=self.raiz, indentacao="", ultimo=True)
	
	def build_index(self, index_list: List[str], header=True) -> None:
		inicio = time.time()
		for linha, chave in enumerate(index_list):
			self.insert(chave, linha+int(header))
		fim = time.time()
		print(f'Indice construído! Levou {fim - inicio: .3f} segundos para {len(index_list)} registros.')
		return