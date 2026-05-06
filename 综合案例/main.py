#设计一个抽象类，定义文件读取的相关功能，使用子类实现具体功能
from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options  import *
from pyecharts.globals import ThemeType

from pymysql import Connection

text_file_reader=TextFileReader(r"D:\BaiduNetdiskDownload\第13章资料\2011年1月销售数据.txt")
json_file_reader=JsonFileReader(r"D:\BaiduNetdiskDownload\第13章资料\2011年2月销售数据JSON.txt")

jan_data:list[Record]=text_file_reader.read_data()
feb_data:list[Record]=json_file_reader.read_data()
#将两个月的数据合并为一个list存储
all_data:list[Record]=jan_data+feb_data

#构建sql链接对象
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="18735817946",
    autocommit=True
)
#获得游标对象
cursor=conn.cursor()
#选择数据库
conn.select_db("py_sql")
for record in all_data:
    sql=f"insert into orders(order_date,order_id,money,province)"\
        f"values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    cursor.execute(sql)

#关闭链接
conn.close()