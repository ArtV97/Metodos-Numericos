from math import fabs

class LU():
	def __init__(self, A):
		self.n = len(A[0])
		self.A = A
		self.perm = []

	def pivoteamento(self, i):
		linhaMaior = i
		for x in range(i+1, self.n):
			if fabs(self.A[linhaMaior][i]) < fabs(self.A[x][i]):
				linhaMaior = x
		self.perm.append(i)
		self.perm.append(linhaMaior)
		for j in range(self.n):
			aux = self.A[i][j]
			self.A[i][j] = self.A[linhaMaior][j]
			self.A[linhaMaior][j] = aux

	def fatoracao(self):
		for i in range(self.n):
			self.pivoteamento(i)
			for x in range(i+1,self.n):
				coef = self.A[x][i]/self.A[i][i]
				self.A[x][i] = coef
				for k in range(i+1,self.n):
					self.A[x][k] -= coef * self.A[i][k]

	#função auxiliar(Ly = b)
	def substituicao(self, b):
		y = []
		for i in range(self.n):
			y.append(b[i])
			if i != 0:
				k = 0
				while k != i:
					y[i] -= y[k] * self.A[i][k]
					k += 1
		return y

	#função auxiliar(Ux = y)
	def retrosubstituicao(self, y):
		x = [0 for i in range(self.n)] #cria o vetor solução com valor 0 em todas as posições
		for i in range(self.n-1, -1, -1): #começa em n-1 e vai até 0
			x[i] = y[i]
			k = self.n-1
			while k != i:
				x[i] -= x[k] * self.A[i][k]
				k -= 1
			x[i] = x[i]/self.A[i][i]
		return x

	#utilizar as funções abaixo apenas após chamar a função fatoracao para obter a LU
	def det(self):
		determinante = self.A[0][0]
		for i in range(1, self.n):
			determinante = determinante * self.A[i][i]
		return determinante * (-1)**(len(self.perm)//2)

	def recalc_b(self, b):
		for x in range(0, len(self.perm), 2):
			aux = b[self.perm[x]]
			b[self.perm[x]] = b[self.perm[x+1]]
			b[self.perm[x+1]] = aux
		return b
	
	def sol_sistema(self, b):
		if len(self.perm) != 0:
			b = self.recalc_b(b)
		return self.retrosubstituicao(self.substituicao(b))
	
	def inversa(self):
		A_inv = [[0 for j in range(self.n)]for i in range(self.n)]
		for i in range(self.n):
			e = [0 for x in range(self.n)]
			e[i] = 1
			e = self.sol_sistema(e)
			for x in range(self.n):
				A_inv[x][i] = e[x]
		return A_inv
