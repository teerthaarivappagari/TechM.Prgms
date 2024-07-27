n=int(input())
li=list(map(int,input().split()))
s1=0
for i in range(n):
    if(i%2==0):
        s1+=li[i]
print(s1)
