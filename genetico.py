import math
import random as ran
from matplotlib import pyplot as plt
import pandas as pd


class genetico ():

    def conversion(self):
        print("/////////////////////////////////////////////////")
        print("CONVERSION A BINARIO")
        print("indica los individuios :")
        individuos = int(input())
        self.individuos = individuos
        print("indica la longitud de la ristra")
        ristra = int(input())
        self.ristra = ristra
        self.aleatorios(individuos, ristra)

    def aleatorios(self, individuos, ristra):
        k = 0
        for i in range(individuos):
            binar = ""
            k += 1
            for j in range(ristra):
                binar += str(ran.randint(0, 1))
                self.binar = binar
                self.decimal = self.binariodecimal(binar)
            print(f"{binar}")
            #print(f"Individuo valor binario: {k}:{binar}")
            #print(f"Individuo valor decimal {k}:{self.decimal}")
        return binar

    def binariodecimal(self, numerobinar):
        numdecimal = 0
        self.numerobinar = numerobinar
        for posicion, digito_string in enumerate(numerobinar[::-1]):
            numdecimal += int(digito_string) * 2 ** posicion
            self.numdecimal = numdecimal
            self.digito_string = digito_string
        return numdecimal

    def calculoGeneral(self):
        print("IMPRIME PARAMETROS FUNCION DE ADAPTACIÓN")
        print("digita el valor minimo>:")
        valorMinimo = float(input())
        print("Digita el valor maximo>:")
        valorMaximo = float(input())
        senoMin = math.sin(valorMinimo)
        senoMax = math.sin(valorMaximo)
        calculaMin = (6*senoMin) + (8*(pow(valorMinimo, 2)))
        calculaMax = (6*senoMax) + (8*(pow(valorMaximo, 2)))
        self.calculaMin = calculaMin
        self.calculaMax = calculaMax
        self.valorMinimo = valorMinimo
        self.valorMaximo = valorMaximo
        print('////////////////////////////////////////////////////////////')
        print("Valor mínimo :>", calculaMin, "Valor máximo :>", calculaMax)
        self.valorReal(valorMinimo, valorMaximo)
        self.valorAdaptacion()
        self.calculaPorcentaje()

    def valorReal(self, valorMinimo, valorMaximo):
        print('////////////////////////////////////////////////////////////')
        j = 0
        numerodecimal = 0
        posicion = 0
        for i in range(self.individuos):
            posicion += 1
            numerodecimal += int(self.digito_string) * 2 ** posicion
            j += 1
            xreal = valorMinimo + \
                (numerodecimal*((valorMaximo - valorMinimo)/(pow(2, self.ristra) - 1)))
            print("Valor real para el individuo", j, ":>", xreal)
            self.xreal = xreal

    def valorAdaptacion(self):
        print('////////////////////////////////////////////////////////////')
        j = 0
        x = 0
        sumaTotal = 0
        for i in range(self.individuos):
            j += 1
            x += int(self.digito_string) * 2 ** j
            valorReal = self.valorMinimo + (x*((self.valorMaximo - self.valorMinimo)/(pow(2, self.ristra) - 1)))
            senAdaptativo = math.sin(valorReal)
            calculaAdaptacion = (6*senAdaptativo) + (8*(pow(valorReal, 2)))
            print("Valor de adaptacion para",
                  j, ":>", calculaAdaptacion)
            self.calculaAdaptacion = calculaAdaptacion
            sumaTotal = sumaTotal+calculaAdaptacion
        self.sumaTotal = sumaTotal

    def calculaPorcentaje(self):

        numerodecimal = 0
        porcentaje = []
        inicio = 0
        j = 0
        sumatoriaporcentual = 0
        for i in range(self.individuos):
            numerodecimal += int(self.digito_string) * 2 ** j
            valorReal = self.valorMinimo + \
                (numerodecimal*((self.valorMaximo - self.valorMinimo)/(pow(2, self.ristra) - 1)))
            senAdaptativo = math.sin(valorReal)
            calculaAdaptacion = (6*senAdaptativo) + (8*(pow(valorReal, 2)))
            sumatoriaporcentual = sumatoriaporcentual + calculaAdaptacion
            porcentaje.insert(inicio, calculaAdaptacion)

        porciento = 0
        porciento = porciento + self.sumaTotal
        print("Porcentaje total:", porciento)
        plt.pie(porcentaje, autopct="%0.1f %%")
        plt.show()

    def cruceUnPunto(self):
        listaPadre1 = []
        listaPadre2 = []
        
        listaHijo1= []
        listaHijo2= []
        
        for i in range(self.individuos):
            
            binario = ""
            binario += str(self.digito_string)
            listaPadre1.append(self.binar)
            listaPadre2.append(self.binar)
            tamanio = self.ristra            
            pcorte = ran.randint(1, tamanio-1)

            listaHijo1[pcorte:] = listaPadre2[pcorte:].copy()
            listaHijo2[pcorte:] = listaPadre1[pcorte:].copy()

        print(listaHijo1)
        print(listaHijo2)

    def cruceDosPuntos(self):
        listaPadre1 = []
        listaPadre2 = []
        
        listaHijo1= []
        listaHijo2= []
        
        for i in range(self.individuos):
            
            binario = ""
            binario += str(self.digito_string)
            listaPadre1.append(self.binar)
            listaPadre2.append(self.binar)
            tamanio = self.ristra            
            pcorte = ran.randint(1, tamanio-1)
            pcorte2 = ran.randint(1,tamanio-1)

            listaHijo1[pcorte:pcorte2] = listaPadre2[pcorte:pcorte2].copy()
            listaHijo2[pcorte:pcorte2] = listaPadre1[pcorte:pcorte2].copy()
            
        print(listaHijo1)
        print(listaHijo2)

if __name__ == '__main__':
    obj = genetico()
    obj.conversion()
    obj.calculoGeneral()
    #obj.cruceUnPunto()
