import math
import matplotlib.pyplot as plt
import random
import numpy as np

from math import e
binarios = ['1010101', '0001001', '1110101', '0000100', '1111001', '0001111']
tamRista = 7
decimales = []
reales = []
adaptativos = []
dic = {}
xMin = 2
xMax = 7
rista = 7

def binDecimal(binarios):
    for x in range(len(binarios)):
        decimal = 0
        binario = binarios[x]
        for posicion, digito_string in enumerate(binario[::-1]):
            decimal += int(digito_string) * 2 ** posicion
        decimal = round(decimal, 2)
        decimales.append(decimal)

def decReal(decimales, xMin, xMax, rista):
    for x in range(len(decimales)):
        decimal = decimales[x]
        real = xMin + decimal * ((xMax-xMin)/(2**rista - 1))
        real = round(real, 2)
        reales.append(real)

def realAdap(reales):
    for x in range(len(reales)):
        real = reales[x]
        adap = 20 + e - 20 * (e**-0.2*np.abs(real))
        adap = round(adap, 2)
        adaptativos.append(adap)

def decimal(binario):
    decimal = 0
    for posicion, digito_string in enumerate(binario[::-1]):
        decimal += int(digito_string) * 2 ** posicion
    return decimal

def real(decimal):
    real = xMin + decimal * ((xMax-xMin)/(2**rista - 1))
    real = round(real, 2)
    return real

def adaptado(real):
    adaptado = 20 + e - 20 * (e**-0.2*np.abs(real))
    adaptado = round(adaptado, 2)
    return adaptado

def unir(binarios, adaptativos):
    for x in range(len(binarios)):
        dic[binarios[x]] = adaptativos[x]

def cruce():
    totalIndi = len(binarios)
    tCruces = (totalIndi * 50) / 100
    tCruces = round(tCruces)
    puntoCorte = 3
    for i in range(tCruces):
        contador = 0
        bit = tamRista
        x = random.randrange(0, totalIndi)
        ind1 = binarios[x]
        hijo1 = list(ind1)
        y = random.randrange(0, totalIndi)
        ind2 = binarios[y]
        hijo2 = list(ind2)
        for j, z in zip(ind1[::-1], ind2[::-1]):
            bit = bit-1
            #print(ind1[bit], ind2[bit])
            if contador < puntoCorte:
                hijo1[bit] = ind2[bit]
                hijo2[bit] = ind1[bit]
                #print(contador)
            else:
                break
            contador = contador + 1
            #print(bit)
        hijo1 = "".join(hijo1)
        hijo2 = "".join(hijo2)
        print('individuo 1: ', ind1)
        print('individuo 2: ', ind2)
        print('hijo 1: ', hijo1)
        print('hijo 2: ', hijo2)
        decimalh1 = decimal(hijo1)
        decimalh2 = decimal(hijo2)
        realh1 = real(decimalh1)
        realh2 = real(decimalh2)
        adaph1 = adaptado(realh1)
        adaph2 = adaptado(realh2)
        indDebil = ind2 if adaptativos[x] > adaptativos[y] else ind1
        valorMin = adaptativos[x] if adaptativos[x] > adaptativos[y] else adaptativos[y]
        hijoFuerte = adaph1 if adaph1 > adaph2 else adaph2
        if hijoFuerte > valorMin:
            print('Es mayor')
        else:
            print('ni uno es mayor')
        
        # print(adaptado(reales[x])) #indi 1
        # print(adaptado(reales[y])) #indi 2

print(binarios)
binDecimal(binarios)
print(decimales)
decReal(decimales, xMin, xMax, rista)
print(reales)
realAdap(reales)
print(adaptativos)
unir(binarios, adaptativos)
#ordenados = sorted(adaptativos, reverse=True)
#print(ordenados)
print(adaptado(xMax))
print(dic)
cruce()
# fig, ax = plt.subplots()
# ax.scatter(binarios, adaptativos)
# ax.scatter(2.5, 2046.27)
# plt.show()