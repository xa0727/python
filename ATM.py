money=5000000
name=None
name=input("请输入您的姓名：")
def query(show_header):# 定义查询函数
    if show_header:
        print("---------查询余额---------")
    print(f"{name},您好，您的余额剩余：{money}元")

def saving(num):# 定义存款函数
    global money
    money+=num
    print("---------存款---------")
    print(f"{name},您好，您存款{num}元成功")

    query(False)# 调用查询余额

def get_money(num):# 定义取款函数
    global money
    money-=num
    print("---------取款---------")
    print(f"{name},您好，您取款{num}元成功")

    query(False)

def main():
    print("---------主菜单----------")
    print(f"{name},您好，欢迎来到黑马ATM，请继续操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环
while True:
    keyboard_input=main()
    if keyboard_input=="1":
        query(True)
        continue# 继续下一次循环，一进来就是主菜单
    elif keyboard_input=="2":
        num=int(input("您想要存多少钱："))
        saving(num)
        continue
    elif keyboard_input=="3":
        num=int(input("您想要取多少钱："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break

