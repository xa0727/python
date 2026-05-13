m,n=map(int,input().split())
list1=[]
for _ in range(m):
    a=list(map(int,input().split()))
    list1.append(a)
for i in range(n):
    list2=[]
    for j in range(m):
        list2.append(str(list1[j][i]))
    print(' '.join(list2))
