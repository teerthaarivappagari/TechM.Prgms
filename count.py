n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
count=0
for i in l1:
    if i not in l2:
       count+=1
for i in l2:
    if i not in l1:
       count+=1
print(count)
