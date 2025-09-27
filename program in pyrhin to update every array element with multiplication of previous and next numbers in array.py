a=int(input())
b=list(map(int,input().split()))
print(b[0]*b[1],end=" ")
for i in range(1,len(b)-1):
    print(b[i-1]*b[i+1],end=" ")
print(b[a-1]*b[a-2],end=" ")
