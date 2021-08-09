from math import factorial
resultados = []

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
    if numero_int(X) and int(X)>=0:
        resultados.clear()
        resultados.append(X*X)
        resultados.append(pow(2,X))
        resultados.append(factorial(X))
        print(resultados)
        
    elif numero_int(X) and int(X)<0:
        print ("Código de error 101.\n")

    elif numero_float(X) and float(X)<0:
        print ("Código de error 102.\n")

    elif numero_float(X) and float(X)>0:
        print ("Código de error 103.\n")

    else:
        print("Código de error 3312.\n")