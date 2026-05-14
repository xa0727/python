n,m,target=map(int,input().split())
list1=[]
for _ in range(n):
    row=list(map(int,input().split()))
    list1.append(row)


# print(list1)

count=0
for i in range(n):
    for j in range(m):
        if list1[i][j]==target:
            count+=1
print(count)