n = int(input())
s = set(map(int, input().split()))
p=int(input())
for i in range(p):
    s1=input().split()
    if s1[0]=='remove':
        s.remove(int(s1[1]))
    elif s1[0]=='discard':
        s.discard(int(s1[1]))
    else:
        s.pop()
print(sum(list(s)))
