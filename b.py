import pandas as pd
import random
import warnings
from math import factorial
import matplotlib.pyplot as plt
import numpy as np
warnings.filterwarnings("ignore")

x = pd.read_csv("data.csv")

def ss_or_nn (x,lista,n,aux=False):
	
	if x['color_value'][n] == 'Yellow' or aux == True:
		return 1
	return 0

def criar_classe(x,lista,n,aim_key='continent'):
	if x[aim_key][n] not in lista:
		lista.update({x[aim_key][n] :{} })

def criar_lista_estratificada(x,lista={},aim_key='continent'):
	for n in range(len(x)):
		criar_classe(x,lista,n)
		try:
			w = ss_or_nn(x,lista,n,lista[x[aim_key][n]][x['country'][n]])
			lista[x[aim_key][n]].update({x['country'][n] : w})
		except:
			lista[x[aim_key][n]].update({x['country'][n] : 0})
	return lista

def criar_lista(x,lista={}):


	for n in range(len(x)):
		try:
			w = ss_or_nn(x,lista,n,aux = lista[x['country'][n]])
			lista.update({x['country'][n] : w})
		except:
			lista.update({x['country'][n] : 0})
	return lista

def gerar_amostra_estratificada(lista,d1={}):
	for n in lista:
		aux = {n:{}}
		raldo = random.sample (lista[n].keys(),4)
		for m in raldo:
			aux[n].update({m:lista[n][m]})
		d1.update(aux)
	return d1

def gerar_amostra_aleatoria(lista,d1={}):
	aux = {}
	raldo = random.sample (lista.keys(),20)
	for n in raldo:
		aux.update({n:lista[n]})
	return aux

def gerar_amostra_sistematizada(lista):
	aux0 = [k for k in lista.keys()]
	return [lista[aux0[i]] for i in range(0,213,3)]

def desalfabetizar (dicionario,lista=[]):
	for key in dicionario:
		lista.append (dicionario[key])
	return lista

def checkTrues(lista):
	count = 0
	for n in lista:
		if lista[n] == True:
			count+=1
	return count/len(lista)

def checkTruesPlus(lista):
	results = {}
	for n in lista:
		count = 0
		for m in lista[n]:
			if lista[n][m] == True:
				count += 1
		results.update({n:(count,len(lista))})
	return results

def checkTrues(lista):
	count = 0
	for n in lista:
		if lista[n] == True:
			count+=1
	return count,len(lista)

def checkTruesPlus(lista):
	results = {}
	for n in lista:
		count = 0
		for m in lista[n]:
			if lista[n][m] == True:
				count += 1
		results.update({n:count/len(lista)})
	return results

def calcular_media(lista): return sum(lista)/len(lista)

def calcular_variancia(lista,var=0):
  media =calcular_media(lista)
  for numero in lista:
    var += (numero - media)**2
  var = var/len(lista)
  return var

def calcular_desvio_padrão(lista):
    return calcular_variancia(lista)**(1/2)

def probabilidadeBinomial(x,n,p,q):
  return (factorial(n)/(factorial(n-x)*factorial(x)))*(p**x)*(q**(n-x))


dl = criar_lista_estratificada(x)
ul = criar_lista(x)
sample_str = gerar_amostra_estratificada(dl)
sample_unstr = gerar_amostra_aleatoria(ul)
sample_sist = gerar_amostra_sistematizada (ul)
aux0 = [k for k in ul.keys()]
sample_sist = [{aux0[i]:ul[aux0[i]]} for i in range(3,213,3)]

p = checkTrues(ul)[0]/checkTrues(ul)[1]
q = (checkTrues(ul)[0]-checkTrues(ul)[1])/-checkTrues(ul)[1]


print ("\nAnálises - países que tem amarelo na bandeira(1) ou não (0)\n")

print('amostra aleatória (20 países randômicos): %s\n' % sample_unstr)
print('amostra estratificada (4 países por continente): %s\n' % sample_str)
print('amostra sistemática (países de endereço multiplo de 3 menor que 213): %s\n' % sample_sist)

print('p: %.2f q: %.2f'%(p,q))
print('variância: %.2f' % (p*q))
print('desvio padrão: %.2f' % (p*q)**2)

n = 21
x = [i for i in range(n+1)]

def pbin(p,q,n,probabilidades = []):
	
	for x in range(n+1):
	  px = probabilidadeBinomial(x,n,p,q)
	  print('P(',x,')=%.3f%s'%(px*100,'%'))
	  probabilidades.append(px)

	print ("soma dos P:%.2f%s"
		% ((np.sum(probabilidades))*100,"%")
	)
	return (probabilidades)

probabilidades = pbin(p,q,n)

plt.bar(x,probabilidades)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Distribuição de Probabilidade (n =21)')
plt.grid(True)
plt.show()
