N = int(input())
for i in range(N):
    print(" "*(2*N-i-1),end="")
    print("*",end="")
    print(" "*N,end="")
    print("*",end="")
    print(" "*(2*i+1),end="")
    print("*",end="")
    print(" "*(N-i-1))

for i in range(N):
    print(" "*(N-i-1),end="")
    print("*",end="")
    print(" "*(N+(i*2)+1),end="")
    print("*",end="")
    print(" "*(2*N-(2*i)-1),end="")
    print("*",end="")
    print(" "*i)