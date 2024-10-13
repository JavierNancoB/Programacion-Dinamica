import time
import random
import matplotlib.pyplot as plt

############################################# FUNCIONES #############################################

#cuadratico
def min_cut_dp(largo,cortesminimosdp,palabra):
    start_time = time.time()
    
    #inicio
    for final in range(1, largo):
        cortesminimosdp[final] = final  #el máximo número posible de cortes (peor caso (inicialmente) = no hay palindromos, luego se actualiza en base a las iteraciones)
        
        for inicio in range(final, -1, -1): #vamos desde i hasta 0
            #si encontramos un palíndromo, actualizamos el mínimo número de cortes
            if palabra[inicio:final+1] == palabra[inicio:final+1][::-1]: #si es palindromo
                if inicio == 0:
                    cortesminimosdp[final] = 0 #toda la palabra es un palindromo
                else:
                    #se calcula en base a la tabla (peor caso y luego peores casos)
                    cortesminimosdp[final] = min(cortesminimosdp[final], 1 + cortesminimosdp[inicio - 1])
                                #tabla(pal ideal), 1 + anterior (no hay pal, por eso se suma la letra nueva al anterior)
    
    #dos for anidados que se recorren completamente o casi completamente? entonces es cuadratico 
    
    #retornamos lo pedido yipi
    #solucion = return minCutDp[n-1]
    
    end_time = time.time()
    return end_time - start_time

#cubico
def min_palindrome_cuts(mincut,palindromo,largo,string):
    start_time = time.time()
    
    # Calcular para subcadenas más grandes
    for largo_interno in range(2, largo + 1): #recorremos todas las cadenas posibles
        for i in range(largo - largo_interno + 1):
            final = i + largo_interno - 1 #posicion final de la subcadena
            if largo_interno == 2: #solo comparamos los extremos
                palindromo[i][final] = (string[i] == string[final])
            else:
                palindromo[i][final] = (string[i] == string[final]) and palindromo[i + 1][final - 1]
            
            if palindromo[i][final]: #si es palindromo, simplemente no hay cortes
                mincut[i][final] = 0
            else:
                mincut[i][final] = float('inf') #numero grande? na, infinito
                for k in range(i, final): #simplemente buscamos la mejor forma de cortar la palabra
                    mincut[i][final] = min(mincut[i][final], mincut[i][k] + mincut[k + 1][final] + 1)
                    
    #dos for anidados que se recorren completamente o casi completamente? entonces es cubicoD   
                 
    #retornamos lo pedido yipi
    #solucion = return mincut[0][n-1]
    
    end_time = time.time()
    return end_time - start_time

############################################# FUNCIONES #############################################

############################################# INICIALIZACION #############################################

def inicializar_cuadratico(palabra):
    largo = len(palabra)
    cortesminimosdp = [0] * largo
    return min_cut_dp(largo,cortesminimosdp,palabra)

def inicializar_cubico(string):
    n = len(string)
    C = [[0] * n for _ in range(n)]
    P = [[False] * n for _ in range(n)]
    
    # Casos base (diagonales)
    for i in range(n):
        P[i][i] = True
    
    return min_palindrome_cuts(C,P,n,string)

############################################# INICIALIZACION #############################################

############################################# GENERICO #############################################

def generar_palabras(num_palabras):
    palabras = []
    for i in range(5,num_palabras+5): #i va a ser la longitud de la palabra
        palabra = ''.join(random.choices('abcde', k=i))
        palabras.append(palabra)
    return palabras

# visualización de los tiempos de respuesta con un grafico bonito c:
def visualizar_tiempos(tiempos_A, tiempos_B):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(tiempos_A)), tiempos_A, color='blue', marker='o', label='cuadratico')
    plt.plot(range(len(tiempos_B)), tiempos_B, color='red', marker='o', label='cubico')
    plt.xlabel('Palabra')
    plt.ylabel('Tiempo de respuesta (segundos)')
    plt.title('Comparación de tiempos de respuesta')
    plt.legend()
    plt.grid(True)
    plt.show()

# medicion de tiempos en base a las palabras
def medir_tiempos(palabras):
    tiempos_A = []
    tiempos_B = []
    for palabra in palabras:
        # inicializar_cuadratico e inicializar_cubico inicializa lo que necesitan las funciones (matrices, arreglos, largos, etc)
        # para que la medicion sea unicamente de ejecucion saltandonos la inicializacion
        tiempo_A = inicializar_cuadratico(palabra)
        tiempo_B = inicializar_cubico(palabra)
        tiempos_A.append(tiempo_A)
        tiempos_B.append(tiempo_B)
    return tiempos_A, tiempos_B

############################################# GENERICO #############################################

# cantidad de palabras (va aumentando de 1 en 1 hasta llegar a cantidad_letras porque parte de 5)
cantidad_letras = 200

palabras = generar_palabras(cantidad_letras)

tiempos_A, tiempos_B = medir_tiempos(palabras)

visualizar_tiempos(tiempos_A, tiempos_B)
