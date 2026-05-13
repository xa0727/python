elements=list(map(int,input().split()))
k=int(input())
n=len(elements)
if k==0:
    print()
else:
    k=k%n
    rotated=elements[-k:]+elements[:-k]
    print(' '.join(map(str,rotated)))