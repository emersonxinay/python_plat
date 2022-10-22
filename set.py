# concepto: los sets se parecen mucho a las listas y los diccionarios

# crear un programa donde se pueda eliminar los valores repetidos
def duplicados(random_list):
    return list(set(random_list))


def datos_lista():
    random_list = [1, 33, 44, 33, 1, 4]
    print(duplicados(random_list))


if __name__ == '__main__':
    datos_lista()
