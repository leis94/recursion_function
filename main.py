
def chequear_pares_impares(lista, n, par, impar):
    longitud_lista = len(lista)
    if longitud_lista == 1:
        return 'La lista solo tiene un elemento'
    
    elif n < longitud_lista:
        if lista[n] % 2 == 0:
            par += 1
            n += 1
            return chequear_pares_impares(lista, n, par, impar)
        else:
            n += 1
            impar += 1
            return chequear_pares_impares(lista, n, par, impar)  
    
    print(par)
    print(impar)
    if (longitud_lista % 2 == 0) and (par == impar):
        return True
    elif(longitud_lista % 2 != 0 and (par > impar)):
        return True
    else:
        return False

            

if __name__ == "__main__":
    lista = [0,0,0,3,5,3,2]
    pares_impares = chequear_pares_impares(lista, 0, 0, 0)
    if pares_impares:
        print(f'La lista está altenada por pares e impares')
    else:
        print(f'La lista NO está altenada por pares e impares')
