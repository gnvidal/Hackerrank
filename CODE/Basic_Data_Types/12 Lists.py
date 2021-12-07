if __name__ == '__main__':
    N = int(input())
    Lista=[]
    for _ in range(N):
        code=input().split()
        if code[0]=="insert":
            Lista.insert(int(code[1]), int(code[2]))
        elif code[0]=="remove":
            Lista.remove(int(code[1]))
        elif code[0]=="append":
            Lista.append(int(code[1]))
        elif code[0]=="sort":
            Lista.sort()
        elif code[0]=="pop":
            Lista.pop()
        elif code[0]=="reverse":
            Lista.reverse()
        elif code[0]=="print":
            print(Lista)
