def count_pairs(lst):
    freq={}
    for i in range(len(lst)-1):
        pair=(lst[i],lst[i+1])
        if pair in freq:
            freq[pair]+=1
        else:
            freq[pair]=1
    return freq



if __name__=='__main__':
    lst=eval(input())
    result=count_pairs(lst)
    print(result)