import math
import random
import pandas as pd

class crearIndividuos():
    __tPoblacion = int(input("Ingrese la cantidad de poblacion: "))
    __rista = int(input("Ingresa la lingitud de la rista: "))
    __limMen = int(input("Define el rango, limite menor: "))
    __limMax = int(input("Define el rango, limite mayor: "))
    tCruces = round((__tPoblacion * 50) / 100)
    if round((__tPoblacion * 10) / 100) < 1:
        tMutaciones = 1
    else: 
        tMutaciones = round((__tPoblacion * 10) / 100)
    individuos = []
    decimales = []
    reales = []
    adaptados = []
    datos = {}
    
    def __init__(self):
        self.creacionPob()

    def creacionPob(self):
        for i in range(self.__tPoblacion):
            binario = ""
            for j in range(self.__rista):
                binario += str(random.randint(0, 1))
            self.individuos.append(binario)
    
    def recorrePob(self):
        for i in range(self.__tPoblacion):
            bina = self.individuos[i]
            dec = self.binDecimal(bina)
            real = self.decReal(dec)
            adap = self.realAdap(real)
            self.decimales.append(dec)
            self.reales.append(real)
            self.adaptados.append(adap)
        self.unir()
                        
    def binDecimal(self, binario):
        decimal = 0
        for posicion, digito_string in enumerate(binario[::-1]):
            decimal += int(digito_string) * 2 ** posicion
        return decimal
    
    def decReal(self, decimal):
        real = self.__limMen + decimal * ((self.__limMax-self.__limMen)/(2**self.__rista - 1))
        real = round(real, 3)
        return real
    
    def realAdap(self, real):
        adaptado = 6*math.sin(real) + 8 * (real**2) 
        adaptado = round(adaptado, 3)
        return adaptado
    
    def unir(self):
        self.datos = {'individuos': self.individuos,
                 'decimales': self.decimales,
                 'reales': self.reales,
                 'adaptados': self.adaptados}
        self.mostrar()
    
    def mostrar(self):
        self.dataF = pd.DataFrame(self.datos)
        print('\n',self.dataF) 
    
    def ordenRuleta(self):
        self.ordenado = self.dataF.sort_values('adaptados', ascending=False)
        print('\n-----ORDENADOS-----\n\n', self.ordenado, '\n')
        #self.cruceUnPunto()
        #self.cruceDosPunto()
        self.cruceUniforme()
    
    def evaluar(self, hijo1, hijo2, adapP1, adapP2, x, y):
        decimalh1 = self.binDecimal(hijo1)
        decimalh2 = self.binDecimal(hijo2)
        realh1 = self.decReal(decimalh1)
        realh2 = self.decReal(decimalh2)
        adaph1 = self.realAdap(realh1)
        adaph2 = self.realAdap(realh2)
        if adapP1 > adapP2:
            if adaph1 > adapP2:
                self.ordenado.iloc[y] = {'individuos': hijo1,
                                        'decimales': decimalh1,
                                        'reales': realh1,
                                        'adaptados': adaph1}
                print("El hijo 1 sustituye a padre 2")
            elif adaph2 > adapP2:
                self.ordenado.iloc[y] = {'individuos': hijo2,
                                        'decimales': decimalh2,
                                        'reales': realh2,
                                        'adaptados': adaph2}
                print("El hijo 2 sustituye a padre 2")
            else:
                print('Ninguno sustituye')
        else:
            if adaph1 > adapP1:
                self.ordenado.iloc[x] = {'individuos': hijo1,
                                        'decimales': decimalh1,
                                        'reales': realh1,
                                        'adaptados': adaph1}
                print("El hijo 1 sustituye a padre 1")
            elif adaph2 > adapP2:
                self.ordenado.iloc[y] = {'individuos': hijo2,
                                        'decimales': decimalh2,
                                        'reales': realh2,
                                        'adaptados': adaph2}
                print("El hijo 2 sustituye a padre 1")
            else:
                print('Ninguno sustituye')
    
    def cruceUnPunto(self):
        puntoCorte = int(input("Ingrese el punto de corte: "))
        for i in range(self.tCruces):
            bit = self.__rista-1
            contador = 0
            x = random.randrange(0, (self.__tPoblacion-1))
            y = random.randrange(0, (self.__tPoblacion-1))
            individuo1 = self.ordenado.iloc[x]
            individuo2 = self.ordenado.iloc[y]
            padre1 = individuo1[0]
            padre2 = individuo2[0]
            hijo1 = list(padre1)
            hijo2 = list(padre2)
            for j, z in zip(padre1[::-1], padre2[::-1]):
                if contador < puntoCorte:
                    hijo1[bit] = padre2[bit]
                    hijo2[bit] = padre1[bit]
                else:
                    break
                bit = bit-1
                contador = contador + 1
            hijo1 = "".join(hijo1)
            hijo2 = "".join(hijo2)
            print('\nindividuo 1: ', padre1)
            print('individuo 2: ', padre2)
            print('hijo 1: ', hijo1)
            print('hijo 2: ', hijo2)
            self.evaluar(hijo1, hijo2, individuo1[3], individuo2[3], x, y)
        print('\n-----Despues de los cruces-----\n')
        print(self.ordenado, '\n')
        self.mutacion()
    
    def cruceDosPunto(self):
        puntoCorteInf = int(input("Ingrese el punto de corte inferior: "))
        puntoCorteSup = int(input("Ingrese el punto de corte superior: "))
        for i in range(self.tCruces):
            bit = self.__rista-1
            contador = 0
            x = random.randrange(0, (self.__tPoblacion-1))
            y = random.randrange(0, (self.__tPoblacion-1))
            individuo1 = self.ordenado.iloc[x]
            individuo2 = self.ordenado.iloc[y]
            padre1 = individuo1[0]
            padre2 = individuo2[0]
            hijo1 = list(padre1)
            hijo2 = list(padre2)
            for j, z in zip(padre1[::-1], padre2[::-1]):
                if contador >= (puntoCorteInf-1) and contador <= (puntoCorteSup-1):
                    print(contador)
                    hijo1[bit] = padre2[bit]
                    hijo2[bit] = padre1[bit]
                bit = bit-1
                contador = contador + 1
            hijo1 = "".join(hijo1)
            hijo2 = "".join(hijo2)
            print('\nindividuo 1: ', padre1)
            print('individuo 2: ', padre2)
            print('hijo 1: ', hijo1)
            print('hijo 2: ', hijo2)
            self.evaluar(hijo1, hijo2, individuo1[3], individuo2[3], x, y)
        print('\n-----Despues de los cruces-----\n')
        print(self.ordenado, '\n')
        self.mutacion()
    
    def cruceUniforme(self):
        mascara = ""
        for j in range(self.__rista):
            mascara += str(random.randint(0, 1))
        print('La mascara es: ', mascara)
        mascara = list(mascara)
        for i in range(self.tCruces):
            x = random.randrange(0, (self.__tPoblacion-1))
            y = random.randrange(0, (self.__tPoblacion-1))
            individuo1 = self.ordenado.iloc[x]
            individuo2 = self.ordenado.iloc[y]
            padre1 = individuo1[0]
            padre2 = individuo2[0]
            hijo1 = list(padre1)
            hijo2 = list(padre2)
            for j in range(self.__rista):
                if mascara[j] == '0':
                    hijo1[j] = padre1[j]
                    hijo2[j] = padre2[j]
                else:
                    hijo1[j] = padre2[j]
                    hijo2[j] = padre1[j]
            hijo1 = "".join(hijo1)
            hijo2 = "".join(hijo2)
            print('\nindividuo 1: ', padre1)
            print('individuo 2: ', padre2)
            print('hijo 1: ', hijo1)
            print('hijo 2: ', hijo2)
            self.evaluar(hijo1, hijo2, individuo1[3], individuo2[3], x, y)
        print('\n-----Despues de los cruces-----\n')
        print(self.ordenado, '\n')
        self.mutacion()
    
    def mutacion(self):
        bitMutado = random.randrange(0, (self.__rista-1))
        for i in range(self.tMutaciones):
            x = random.randrange(0, (self.__tPoblacion-1))
            bit = self.__rista-1
            contador = 0
            individuo = self.ordenado.iloc[x]
            print(self.ordenado.iloc[x])
            ind = list(individuo[0])
            for j in ind[::-1]:
                if contador == bitMutado:
                    print(individuo[0])
                    if ind[bit] == '0':
                        ind[bit] = '1'
                    else:
                        ind[bit] = '0'
                    break
                bit = bit-1
                contador = contador + 1 
            print('Cambio en el bit: ', bitMutado)
            indMut = "".join(ind)
            print(ind)
            deciMut = self.binDecimal(ind)
            realMut = self.decReal(deciMut)
            adapMut = self.realAdap(realMut)
            self.ordenado.iloc[x] = {'individuos': indMut,
                                        'decimales': deciMut,
                                        'reales': realMut,
                                        'adaptados': adapMut}
            print(self.ordenado.iloc[x])
            print('\n-----Despues de la mutacion-----\n')
            print(self.ordenado, '\n')
                        
def main():
    obj = crearIndividuos()
    obj.recorrePob()
    obj.ordenRuleta()
    
if __name__ == '__main__':
    main()