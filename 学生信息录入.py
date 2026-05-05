class student:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

stu=[]
num=0
for i in range(10):
    num+=1
    print(f"当前录入第{num}位学生的信息，总共需要录入10位学生的信息")

    name=input("请输入学生的姓名：")
    age=input("请输入学生的年龄：")
    address=input("请输入学生的地址：")

    s=student(name,age,address)
    stu.append(s)
    print(f"学生{num}的信息录入完毕，信息为：【学生姓名：{s.name},学生年龄：{s.age},学生地址：{s.address}】")