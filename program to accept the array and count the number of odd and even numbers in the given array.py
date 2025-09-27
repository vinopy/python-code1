n=int(input())
a=input()
l=a.split()
even=0
for i in l:
    if int(i)%2==0:
        even=even+1
print("Odd =",n-even)
print("Even =",even)
