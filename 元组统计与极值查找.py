t=tuple(map(int,input().split()))
a=0
b=0
c=0
for i in t:
    if i>0:
        a+=1
    elif i<0:
        b+=1
    else:
        c+=1
max_num=max(t)
min_num=min(t)
result=(a,b,c,max_num,min_num)
print(result)