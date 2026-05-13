x,y=map(int,input().split())
if x&1==1:
    print(True)
else:
    print(False)
if y&1==0:
    print(True)
else:
    print(False)
x=x^y
y=x^y
x=x^y
print(x,y)
