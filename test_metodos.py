import unittest
import metodos
import random

from math import factorial


def resp_correcta_metodo1(dato):
    resultados_metodo_1 = []
    # se inicia el arreglo
    if isinstance(dato, int) and dato >= 0:
        # solo si cumple las condiciones de ser numero entero positivo procede
        resultados_metodo_1.append(dato*dato)
        resultados_metodo_1.append(pow(2, dato))
        resultados_metodo_1.append(factorial(dato))
        return resultados_metodo_1
    else:
        return None


def resp_correcta_metodo2(arreglo):
    resultados_metodo_2 = []
    largo = len(arreglo)
    # cantidad de elementos del arreglo
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
    def test_add(self):

        prueba = [-1, "a", 4, 0.2, 1, 0, 5]

        i = random.randint(0, 6)
        result = metodos.multiple_op(prueba[i])
        self.assertEqual(result, resp_correcta_metodo1(prueba[i]))
        entrada_1 = prueba[random.randint(0, 6)]
        entrada_2 = prueba[random.randint(0, 6)]
        arreglo_prueba = [entrada_1, entrada_2]
        result = metodos.verify_array_op(arreglo_prueba)
        self.assertEqual(result, resp_correcta_metodo2(arreglo_prueba))
