a=int(input())
b=0
c=list(map(int,input().split()))
for i in c:
    b=i+b
for j in c:
    print(b-j,end=" ")
