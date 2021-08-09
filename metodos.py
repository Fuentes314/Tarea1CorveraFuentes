from math import factorial

def numero_int(entrada):
    try:
        return isinstance(entrada, int)
    except ValueError:
        return False

def numero_float(entrada):
    try:
        return isinstance(entrada, float)
    except ValueError:
        return False

def multiple_op(X):
    resultados_metodo_1 = []

    if numero_int(X) and int(X)>=0:
        resultados_metodo_1.append(X*X)
        resultados_metodo_1.append(pow(2,X))
        resultados_metodo_1.append(factorial(X))
        return resultados_metodo_1
        
    elif numero_int(X) and int(X)<0:
        print ("Código de error 101.NEGATIVO\n")

    elif numero_float(X) and float(X)<0:
        print ("Código de error 102.DECIMAL NEGATIVO\n")

    elif numero_float(X) and float(X)>0:
        print ("Código de error 103.DECIMAL\n")

    else:
        print("Código de error 3312.CARACTER\n")

def verify_array_op (arreglo):
    resultados_metodo_2 = []
    largo = len(arreglo)
    i = 0
    while i <= largo :
        if numero_int(arreglo[i]) and int(arreglo[i])>=0:
            resultados_metodo_2.append(multiple_op(arreglo[i]))
            
        elif numero_int(arreglo[i]) and int(arreglo[i])<0:
            print ("Código de error 101.NEGATIVO\n")

        elif numero_float(arreglo[i]) and float(arreglo[i])<0:
            print ("Código de error 102.DECIMAL NEGATIVO\n")

        elif numero_float(arreglo[i]) and float(arreglo[i])>0:
            print ("Código de error 103.DECIMAL\n")

        else:
            print("Código de error 3312.CARACTER\n")
    print(resultados_metodo_2)
        
