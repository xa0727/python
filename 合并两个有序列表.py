def merge_sorted_lists(lst1,lst2):
    i=j=0
    result=[]
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

if __name__=='__main__':
    n,m=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    result=merge_sorted_lists(lst1,lst2)
    print(' '.join(map(str,result)))
