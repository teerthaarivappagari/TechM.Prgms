s=input()
h,m,s=s.split(':')
if(s[2:]=='PM' and hr!='12'):
    h=str(int(h)+12)
    print(h+':'+m+':'+s[:2])
elif(s[2:]=='AM' and h=='12'):
    h='00'
    print(h+':'+m+':'+s[:2])
else:
    print(h+':'+m+':'+s[:2])
