t1=tuple(map(int,input().split()))
t2=tuple(map(int,input().split()))

new_t1=(t2[0],)+t1[1:]
new_t2=(t1[0],)+t2[1:]
result=new_t1+new_t2
print(result)
