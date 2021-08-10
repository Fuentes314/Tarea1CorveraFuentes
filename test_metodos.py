import unittest
import metodos
import random
    #Llamado de las librerías a usar. 
from math import factorial
    #Importación de librerías para el factorial

def resp_correcta_metodo1(dato):
    #Función para determinar la respuesta correcta del métdo 1
    resultados_metodo_1 = []
    # se inicia el arreglo vacío
    if isinstance(dato, int) and dato >= 0:
        # solo si cumple las condiciones de ser numero entero positivo procede
        #Se crean los resultados que se van a agregar al arreglo
        resultados_metodo_1.append(dato*dato)
        resultados_metodo_1.append(pow(2, dato))
        resultados_metodo_1.append(factorial(dato))
        return resultados_metodo_1
        #Devuelve el arreglo con los resultados
    else:
        return None


def resp_correcta_metodo2(arreglo):
    # Fución para determinar la respuesta correcta del método 2 (Array)
    resultados_metodo_2 = []
    # Arreglo vacío para almacenar los resultados 
    largo = len(arreglo)
    # Fijar cantidad de elementos del arreglo
    i = 0
    while i < largo:
        # ciclo que recorre cada elemento del arreglo
        # y llama a la funcion uno enviandolo el dato del arreglo

        if isinstance(arreglo[i], int) and arreglo[i] >= 0:
            resultados_metodo_2.append(resp_correcta_metodo1(arreglo[i]))
        else:
            return None
        i += 1


class TestMetodos(unittest.TestCase):
    # Se crea una clase para realizar el test de los métodos
    def test_add(self):
    # función para realizar el test haciendo uso de número random
        prueba = [-1, "a", 4, 0.2, 1, 0, 5]
        # Arreglo que hace función de base de datos a probar

        i = random.randint(0, 6)  # Se asigna un valor entre el rango de 0 a 6
        result = metodos.multiple_op(prueba[i])
        self.assertEqual(result, resp_correcta_metodo1(prueba[i]))
        entrada_1 = prueba[random.randint(0, 6)]
        entrada_2 = prueba[random.randint(0, 6)]
        # Se selecciona una entrada al azar del arreglo prueba
        arreglo_prueba = [entrada_1, entrada_2]
        result = metodos.verify_array_op(arreglo_prueba)
        # Se verifican los dos datos del arreglo sellecionado de prueba
        self.assertEqual(result, resp_correcta_metodo2(arreglo_prueba))
