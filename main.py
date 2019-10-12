from arquivo import*
from lu import*

arq = Arquivo()
for x in range(arq.m):
	temp = arq.leitor()
	print ('Matriz A')
	print('\n'.join(['  '.join(['{:4.4f}'.format(item) for item in row]) 
      for row in temp[0]]))
	obj = LU(temp[0])
	obj.fatoracao()
	sol = obj.sol_sistema(temp[1])
	arq.escritor(x, sol, obj.det())
	print("Solucao = ",", ".join("%.4f" % f for f in sol))