n=int(input())
product=1
while(n>0):
    num=n%10
    product*=num
    n=n//10
print(product)
