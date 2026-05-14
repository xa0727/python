n=int(input())
for i in range(1,n+1):
    char=chr(ord('A')+i-1)
    line=" ".join([char]*i)
    print(line)