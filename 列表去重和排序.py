list1=list(map(int,input().split()))
list2=list(set(list1))
list2.sort()
print(' '.join(map(str,list2)))