lista = []

for i in range(101):
    lista.append(i)

print(lista)
medelLista = []

for item in lista[0:92]:
    nyLista = []
    x = item
    y = item+9
    for item in lista[x:y]:
        nyLista.append(item)
    medel = sum(nyLista)/len(nyLista)
    medelLista.append(medel)

print(medelLista)
