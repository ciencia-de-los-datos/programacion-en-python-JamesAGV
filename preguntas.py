"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

archivo=open('data.csv', mode='r').readlines()
archivo=[i.replace('\n', '') for i in archivo]
archivo=[i.split('\t') for i in archivo]


'''A continuación, funciones definidas para la resolución de las preguntas'''

def get_list_c_1(file): #Retorna una lista con enteros correspondientes a la segunda columna (1) del archivo
    return list(map(lambda x: int(x[1]), file))

def get_list_c_0(file): #Retorna una lista con letras correspondientes a la primera columna (0) del archivo
    return [i[0] for i in file]

def get_list_ordened_letters_set(): #Retorna una lista que sus elementos son la letras (únicas), ordenadas alfabéticamente
    letras=get_list_c_0(archivo) #Lista con la letra de cada registro
    letras_conjunto=set(letras) #Se obtiene un conjunto de las letras (letras únicas)
    letras_ordenadas=list(letras_conjunto) #Se obtiene una lista a partir del conjunto
    letras_ordenadas.sort() #Se ordena la lista alfabéticamente
    return letras_ordenadas

def get_list_filtered_registers_by_letter(file): #Retorna una lista de listas de registros agrupados por letras
    return [list(filter(lambda x: x[0]==i, file)) for i in get_list_ordened_letters_set()]

def get_list_values_c_2_by_letter(): #Retorna una lista de lista de valores dde la columna 2 (1) para cada letra
    return [list(map(lambda x: int(x[1]), i)) for i in get_list_filtered_registers_by_letter(archivo)]

def get_list_dates(): #Retorna una lista de lista con las fechas (columna 3 (2)) de cada registro [[año,mes,día]...]
    return [i[2].split('-') for i in archivo]

def get_list_c_4(): #retorna una lista con los elementos correspondientes a la columna 5 (4)
    return list(map(lambda x: x[4], archivo))

def get_list_keyValue_by_register(): #Retorna una lista de listas de claves y valor por registro [['jjj:12', 'bbb:3', 'ddd:9', 'ggg:8', 'hhh:2'],...]
    return [i.split(',') for i in get_list_c_4()]

def get_list_keyValue(): #Retorna una lista de listas con cada clave y valor [['jjj,'12'],['bbb,'3'],...]
    lista=[j for i in get_list_keyValue_by_register() for j in i] #['jjj:12','bbb:3','ddd:9','ggg:8','hhh:2',...]
    return [i.split(':') for i in lista] #[['jjj', '12'],['bbb', '3'],['ddd', '9'],...]

def get_list_ordened_keys_set(): #Retorna ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj']
    keys=list(set(list(map(lambda x: x[0], get_list_keyValue()))))
    keys.sort()
    return keys

def get_list_filtered_keyValue_by_key(): #Retorna lsita de listas filtradas por clave
    return [list(filter(lambda x: x[0]==i, get_list_keyValue())) for i in get_list_ordened_keys_set()]

def get_list_values_by_key(): #Retorna una lista de listas de los valores por clave
    return [list(map(lambda x: int(x[1]), i)) for i in get_list_filtered_keyValue_by_key()]

def get_list_ordened_c1_set(): #Retorna [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] proveniente de valores únics de c1
    lista=[int(i[1]) for i in archivo]
    lista=list(set(lista))
    lista.sort()
    return lista

def get_list_filtered_by_c1_values(): #Retorna una lista de listas de registros filtrador por valores de la columna 2 (1)-c1
    return [list(filter(lambda x: int(x[1])==i, archivo)) for i in get_list_ordened_c1_set()]

def get_list_letters_by_c1_vallues(): #Retorna una lista de lista de letras por cada valor de la columna 1 (c1)
    return [list(map(lambda x: x[0], i)) for i in get_list_filtered_by_c1_values()]

'''Hasta aquí van las funciones adicionales'''

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lista_c_1=get_list_c_1(archivo)
    return sum(lista_c_1)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return  [(i, get_list_c_0(archivo).count(i)) for i in get_list_ordened_letters_set()]


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista_suma= list(map(lambda x: sum(x), get_list_values_c_2_by_letter()))
    letras_ordenadas=get_list_ordened_letters_set()
    return [(letras_ordenadas[i], lista_suma[i]) for i in range(len(letras_ordenadas))]


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    months=[i[1] for i in get_list_dates()]
    months.sort()
    monthSet=list(set(months))
    monthSet.sort()
    return [(i, months.count(i)) for i in monthSet]


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    valuesList=get_list_values_c_2_by_letter()
    ordenedLetters=get_list_ordened_letters_set()
    return [(ordenedLetters[i], max(valuesList[i]), min(valuesList[i])) for i in range(len(ordenedLetters))]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return [(get_list_ordened_keys_set()[i], min(get_list_values_by_key()[i]), max(get_list_values_by_key()[i])) for i in range(len(get_list_ordened_keys_set()))]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return [(get_list_ordened_c1_set()[i], get_list_letters_by_c1_vallues()[i]) for i in range(len(get_list_ordened_c1_set()))]


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    listaSetLetras=[list(set(map(lambda x: x[0], i))) for i in get_list_filtered_by_c1_values()]
    [list(map(lambda x: x.sort(),listaSetLetras))]
    return [(get_list_ordened_c1_set()[i], listaSetLetras[i]) for i in range(len(get_list_ordened_c1_set()))]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    campoClave=[i[0] for i in get_list_keyValue()]
    return {i:campoClave.count(i) for i in get_list_ordened_keys_set()}


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

print(pregunta_09())

