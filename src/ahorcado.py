import random

def cargar_palabras(ruta):

    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
        return res

def elegir_palabra(palabras):

    res = random.choice(palabras)
    return res

def enmascarar_palabra(palabra, letras_probadas):
   
    res = []
    for f in palabra:
        if f in letras_probadas:
            res.append(f)
        else:
            res.append("_")
    return ' '.join(res)
    
def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''

#Hola putosssssss
#Buenas como tamos

