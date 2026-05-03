import random
num=random.randint(1,100)
flag=True
count=0
while flag:
    count+=1
    guess_num=int(input("请输入你猜的数字："))
    if guess_num==num:
        flag=False
        print("猜对了")
    else:
        if guess_num>num:
            print("猜大了")
        else:
            print("猜小了")
print(f"你猜测的次数为{count}")