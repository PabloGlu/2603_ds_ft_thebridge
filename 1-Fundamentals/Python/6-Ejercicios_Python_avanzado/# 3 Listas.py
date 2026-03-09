# 3 Listas

## grupo_musical --> strings
## generos --> strings
## anios --> int o tuplas

g1 = ['Madonna', 'pop', 1983]
g2 = ['ABBA', 'pop', (1972, 1982)]
g3 = ['Kosch', 'electronica', 1995]

list_total = []
list_name = []
list_genre = []
list_year = []

def inserta(grupo, genero, comienzo, fin = None):
    list_total.append([grupo, genero, (comienzo, fin)])
    list_name.append(grupo)
    list_genre.append(genero)
    list_year.append((comienzo, fin))

def busca_genero(genero):
    this_genre = []
    for i, x in enumerate(list_genre):
        if x == genero:
            this_genre.append(list_name[i])
    print(this_genre)
    return this_genre

def busca_grupos(activos = True):
    this_group = []
    for i, x in enumerate(list_year):
        if activos == True:
            if not x[1]:
                this_group.append(list_name[i])
        if activos == False:
            if x[1]:
                this_group.append(list_name[i])
    print(this_group)
    return this_group

def busca_genero_indice(genero):
    this_genre = []
    for i, x in enumerate(list_genre):
        if x == genero:
            this_genre.append(i)
    print(this_genre)
    return this_genre

def filtra_listas_genero(genero):
    this_genre = []
    this_name = []
    this_year = []
    for i, x in enumerate(list_genre):
        if x == genero:
            this_genre.append(list_genre[i])
            this_name.append(list_name[i])
            this_year.append(list_year[i])
    print(this_genre, this_name, this_year)
    return this_genre, this_name, this_year

def anios_activos():
    for i, x in enumerate(list_name):
        if not list_year[i][1]:
            print(f"{list_name[i]} --> {2026 - list_year[i][0]} años activos")
        else:
            print(f"{list_name[i]} --> {list_year[i][1] - list_year[i][0]} años activos")


inserta("ABBA", "pop",1972,1982)
inserta("Madonna","pop",1983)
inserta("Kölsch","electronica",1995)

print("pop", busca_genero("pop"))
print("electronica", busca_genero("electronica"))

print("activos", busca_grupos())
print("disueltos", busca_grupos(False))

print("indices pop", busca_genero_indice("pop"))
print("indices electronica", busca_genero_indice("electronica"))

l1,l2,l3 = filtra_listas_genero("pop")
print("pop", l1)
print("pop", l2)
print("pop", l3)

anios_activos()


filtra_listas_genero('pop')




    



