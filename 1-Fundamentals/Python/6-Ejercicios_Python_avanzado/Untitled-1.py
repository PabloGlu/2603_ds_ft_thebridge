def devolver(lista):
    lista1 = []
    for x in lista:
        if x == 'rojo':
            lista1.append('stop')
            return 
        if x == 'verde':
            lista1.append(['avance'])
        if x == 'amarillo':
            lista1.append(['precaución'])
    print(lista1)
    return lista1

devolver(['rojo', 'verde', 'amarillo'])