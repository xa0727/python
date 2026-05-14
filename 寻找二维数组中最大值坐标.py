n,m=map(int,input().split())
list1=[]
for i in range(n):
    row=list(map(int,input().split()))
    list1.append(row)

max_num=list1[0][0]
x,y=0,0

for i in range(n):
    for j in range(m):
        if list1[i][j]>max_num:
            max_num=list1[i][j]
            x=i
            y=j

print(max_num,x,y)