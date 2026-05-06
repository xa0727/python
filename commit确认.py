from pymysql import Connection
#构建MySQL数据库的连接
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="18735817946",
)

cursor=conn.cursor()#获取游标对象
#选择数据库
conn.select_db("world")
cursor.execute("insert into student values(10001,'周杰伦',31,'男')")
conn.commit()

conn.close()