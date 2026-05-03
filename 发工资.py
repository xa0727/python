from random import random
money = 10000
for i in range(1,21):
    import random
    num=random.randint(1,10)
    if money>=1000:
        # 先判断是否有钱发工资，在判断每个人的情况
        if num<5:
            print(f"员工{i}绩效分{num}，不发工资，下一位")
            continue
        # 跳出这个员工，判断下一个
        else:
            money-=1000
            print(f"员工{i}，满足条件发工资，余额{money}")
    else:
        print(f"余额不足，下个月再发")
        break
