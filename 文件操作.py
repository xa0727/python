f=open(r"D:\python\4.26\word.txt","r",encoding="UTF-8")
# r进行转义\

# content=f.read()
# count=content.count("itheima")
# print(f"itheima在文件中出现了：{count}")
# f.close()

count=0
for line in f:
    line=line.strip()
    #去除开头的空格和换行符
    words=line.split(" ")
    for word in words:
        if word=="itheima":
            count+=1
print(f"itheima在文件中出现了：{count}")
f.close()
