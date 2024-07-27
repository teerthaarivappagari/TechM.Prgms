n=int(input())
grades=list(map(int,input().split()))
for i in range(n):
    if(grades[i]>=38):
        temp=grades[i]//5
        temp=(temp+1)*5
        if((temp-grades[i])<3):
            grades[i]=temp
print(grades)
