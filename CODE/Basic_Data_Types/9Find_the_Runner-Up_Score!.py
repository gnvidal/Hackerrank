if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(list(set(arr)))
    print(arr[-2])
    #list(set(arr)) obtener el conjunto de los datos y hacerlos lista
    #sorted() ordena los datos de menor a mayor
    #print(valor)
