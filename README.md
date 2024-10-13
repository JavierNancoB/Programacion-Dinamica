# Análisis de Algoritmos - Comparación de Complejidad Cuadrática y Cúbica

Este programa implementa dos algoritmos de **Programación Dinámica** para resolver el problema de particionar una cadena en subcadenas palíndromas con el mínimo número de cortes. Se utiliza **Python** junto con la biblioteca **Matplotlib** para visualizar el rendimiento de ambos enfoques: uno de complejidad **cuadrática** y otro de complejidad **cúbica**. El objetivo es medir los tiempos de ejecución de ambos algoritmos y compararlos gráficamente.

## Características del Programa

1. **Algoritmo Cuadrático**:
   - Evalúa todas las posibles subcadenas para verificar si son palíndromas.
   - Utiliza un arreglo para calcular el número mínimo de cortes necesarios hasta cada posición de la cadena.
   - Complejidad temporal: O(n²).

2. **Algoritmo Cúbico**:
   - Evalúa todas las subcadenas posibles y calcula el número óptimo de cortes mediante la verificación de todos los puntos de corte.
   - Utiliza dos matrices: una para verificar palíndromas y otra para almacenar los cortes mínimos.
   - Complejidad temporal: O(n³).

3. **Generación de Palabras**:
   - Se generan aleatoriamente cadenas de caracteres de longitud creciente para medir el tiempo de ejecución de ambos algoritmos.

4. **Visualización de Tiempos**:
   - El programa genera un gráfico que compara los tiempos de ejecución de los dos algoritmos para las diferentes cadenas generadas.
   - La visualización muestra los tiempos en función del tamaño de las palabras, permitiendo observar cómo se comportan los algoritmos a medida que aumenta la longitud de las cadenas.

## Dependencias

- **Python 3.x**
- **Matplotlib** (Para la visualización de gráficos)

### Instalación de Matplotlib:
```bash
pip install matplotlib
```

## Cómo Ejecutar el Programa

1. Asegúrate de tener instalados Python y Matplotlib.
2. Ejecuta el archivo Python:
   ```bash
   python analisis_entregable.py
   ```
3. El programa generará palabras aleatorias de hasta 200 caracteres y medirá los tiempos de ejecución de los dos algoritmos.
4. Al finalizar, se mostrará un gráfico comparativo con los resultados de los tiempos de respuesta.

## Funciones Principales

- **min_cut_dp()**: Implementa el enfoque cuadrático para calcular los cortes mínimos en una cadena palíndroma.
- **min_palindrome_cuts()**: Implementa el enfoque cúbico para calcular los cortes mínimos, evaluando todas las posibles divisiones.
- **generar_palabras()**: Genera una lista de palabras aleatorias de longitud variable.
- **medir_tiempos()**: Calcula los tiempos de ejecución para ambos algoritmos.
- **visualizar_tiempos()**: Crea un gráfico que compara los tiempos de ejecución de los dos algoritmos.

## Resultados Esperados

- El algoritmo **cuadrático** es más rápido para cadenas pequeñas y medianas.
- El algoritmo **cúbico** es capaz de manejar casos más complejos, pero su tiempo de ejecución aumenta significativamente para cadenas más largas.
- El gráfico permitirá observar visualmente cómo el tiempo de respuesta de cada algoritmo crece a medida que aumenta el tamaño de las cadenas.

Este programa es útil para analizar el comportamiento de distintos algoritmos en función de su complejidad y observar cómo estos algoritmos escalan cuando se procesan datos de mayor tamaño.
