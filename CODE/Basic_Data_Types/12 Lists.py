if __name__ == '__main__':
    N = int(input())
    Lista=[]
    for _ in range(N):
        code=input().split()
    if "insert"==code[0]:
        Lista.insert(code[1], code[2])
    elif "remove"==code[0]:
        Lista.remove(int(code[1]))
    elif "append"==code[0]:
        Lista.append(int(code[1]))
    elif "sort"==code[0]:
        Lista.sort()
    elif "pop"==code[0]:
        Lista.pop()
    elif "reverse"==code[0]:
        Lista.reverse()
    elif "print"==code[0]:
        print(Lista)
