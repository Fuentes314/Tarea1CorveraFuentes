from math import factorial #importacion de libreria para realizar el factorial

def numero_int(entrada): #función que verifica que el numero sea entero
    return isinstance(entrada, int) #si es entero "int" regresa un booleano "True", en otro caso retorna "False"

def numero_float(entrada):
    return isinstance(entrada, float)

def multiple_op(X): #metodo uno, verifica que recibe un numero, realiza operaciones y retorna un arreglo con el resultado. El parametro de entrada es un numero
    resultados_metodo_1 = [] #se inicia el arreglo 

    if numero_int(X) and int(X)>=0: #solo si cumple las condiciones de ser numero entero positivo procede
        resultados_metodo_1.append(X*X)
        resultados_metodo_1.append(pow(2,X))
        resultados_metodo_1.append(factorial(X))
        return resultados_metodo_1 #retorno del arreglo final
        
    elif numero_int(X) and int(X)<0:
        print ("Código de error 1010.\n")

    elif numero_float(X) and float(X)<0:
        print ("Código de error 1020.\n")

    elif numero_float(X) and float(X)>0:
        print ("Código de error 1030.\n")

    else:
        print("Código de error 3312.\n")

def verify_array_op(arreglo): #metodo dos, verifica que recibe solo numeros, llama al metodo 1 y retorna un arreglo con el resultado. El parametro de entrada es un arreglo
    resultados_metodo_2 = []
    largo = len(arreglo) #cantidad de elementos del arreglo
    i = 0
    while i < largo : #ciclo que recorre cada elemento del arreglo y llama a la funcion uno enviandolo el dato del arreglo
        if numero_int(arreglo[i]) and int(arreglo[i])>=0:
            resultados_metodo_2.append(multiple_op(arreglo[i]))
            
        else:
            print("Código de error 3141.\n")
        i+=1
    print(resultados_metodo_2) #una vez que termina la lista imprime el resultado como un arreglo de arreglos

"""
Codigos de error:
1010 #codigo de error para numero menor a cero
1020 #codigo de error para numero negativo y decimal
1030 #codigo de error para numero decimal
3141 #codigo de error para elemento del arreglo que no cumple con ser numero entero positivo
3312 #codigo de error para caracter o cadena de caracteres
"""
