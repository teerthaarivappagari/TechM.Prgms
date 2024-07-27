n=int(input())
li=[]
for i in range(n):
    l=list(map(int,input().split()))
    li.append(l)
ld=0
rd=0
for row in range(n):
    for col in range(n):
        if(row==col):
            ld+=li[row][col]
        if(row+col==n-1):
            rd+=li[row][col]
print(ld,rd)
print(abs(ld-rd))
