for i in range(1,10):
# 控制行数
    for j in range(1,i+1):
# 第几行就有几个等式
        print(f"{j}*{i}={i*j}\t",end='')# 这一行结束前不换行
    print()# 这一行结束换行