mylist=[1,2,3,4,5,6,7,8,9,10]
index=0
list1=[]
while index< len(mylist):
    i=mylist[index]
    if i%2==0:
        list1.append(i)
    index+=1
print(list1)

list2=[]
for i in mylist:
    if i%2==0:
        list2.append(i)
print(list2)