# Enter your code here. Read input from STDIN. Print output to STDOUT
c=input().split()
n=int(c[0])
m=int(c[1])

    #top Arriba
    #range(1,n,2) va de 1 a n y se salta la mitad porque tiene el 2
for i in range(1,n,2):
    print(('.|.'*i).center(m,'-'))
    #middle al medio
print('WELCOME'.center(m,'-'))
    #bottom abajo
for i in range(n-2,-1,-2): 
    print(('.|.'*i).center(m,'-'))
