def ehPrimo(x):
    cont = 1
    if x == 1:
        return True
    else:
        for y in range (2,x):
            if x % y == 0:
                cont = cont + 1
        if cont < 2:
            return True
        else:
            return False


def contaPrimos(num):
    lista = []
    i = 1
    cont = 0
    while num > cont:
        if ehPrimo(i):
            cont = cont+1
            lista.append(i)
            i = i+1
        else:
            i = i+1
    return lista

n = contaPrimos(12)

print(n)
