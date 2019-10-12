class Arquivo():
	def __init__(self):
		self.arqLeitura = open("SISTEMA.txt", "r")
		self.arqEscrita = open("RESUL.txt", "w")
		self.m = int(self.arqLeitura.readline()) #quantidade de sistemas lineares
		self.cont_read = 0
		self.cont_write = 0

	def leitor(self):
		self.cont_read += 1
		n = int(self.arqLeitura.readline())
		aux = []
		b = []
		for i in range(n):
			aux.append(list(map(float, self.arqLeitura.readline().split())))
			b.append(aux[i][n])
			del(aux[i][n])
		if self.cont_read == self.m:
			self.arqLeitura.close()
		aux2 = [aux, b]
		return aux2

	def escritor(self, m, sol, det):
		self.cont_write += 1
		self.arqEscrita.write("Sistema {}\n".format(m+1))
		self.arqEscrita.write("->Solução = " + ", ".join("%.4f" % f for f in sol)+"\n")
		self.arqEscrita.write("->determinante = {}\n\n".format("%.4f" % det))
		if self.cont_write == self.m:
			self.arqEscrita.close()