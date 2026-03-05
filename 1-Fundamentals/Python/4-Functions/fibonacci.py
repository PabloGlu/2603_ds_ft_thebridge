def fibonacci(lista, num):
    if len(lista) == 1:
        lista.append(1)

    if len(lista)-1 >= num:
        return lista
    
    lista.append(lista[-2] + lista[-1])

    return fibonacci(lista, num)
start = [0]
print(fibonacci(start, num = 7))

