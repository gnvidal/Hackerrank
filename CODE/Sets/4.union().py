enN=int(input())
enSet=set(map(int,input().split()))
frN=int(input())
frSet=set(map(int,input().split()))
least=enSet|frSet
print(len(least))
