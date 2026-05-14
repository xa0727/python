n=int(input())
for i in range(1,n+1):
    inc=list(range(1,i+1))
    dec=list(range(i-1,0,-1))
    line=inc+dec
    line_str=" ".join(map(str,line))
    print(line_str)

    #n=4
    # 1
    # 1 2 1
    # 1 2 3 2 1
    # 1 2 3 4 3 2 1