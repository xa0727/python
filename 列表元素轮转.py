elements=list(map(int,input().split()))
k=int(input())
if k==0:
    print()
else:
    k=k%len(elements)
    rotated=elements[-k:]+elements[:-k]
    print(' '.join(map(str,rotated)))