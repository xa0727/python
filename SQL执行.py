from pymysql import Connection
#构建MySQL数据库的连接
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="18735817946",
)

# print(conn.get_server_info())
#执行非查询性质SQL
cursor=conn.cursor()#获取游标对象
#选择数据库
conn.select_db("test")
#执行SQL
cursor.execute("create table test_pymysql(id int);")

conn.close()