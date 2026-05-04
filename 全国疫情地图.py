from pyecharts.charts import Map
from pyecharts.options import *
import json

f=open(r"D:\BaiduNetdiskDownload\资料\可视化案例数据\地图数据\疫情.txt","r",encoding="utf-8")
data=f.read()
f.close()
data_dict=json.loads(data)
province_data_list=data_dict["areaTree"][0]["children"]
data_list=[]
for province_data in province_data_list:
    province_name=province_data["name"]
    province_confirm=province_data["total"]["confirm"]
    if province_name in ["香港", "澳门"]:
        data_list.append((province_name, province_confirm))
    elif province_name == "台湾":
        data_list.append(("台湾省", province_confirm))
    elif province_name in ["北京", "上海", "天津", "重庆"]:
        data_list.append((province_name + "市", province_confirm))
    elif province_name in ["内蒙古", "西藏", ]:
        data_list.append((province_name + "自治区", province_confirm))
    elif province_name =="新疆":
        data_list.append((province_name + "维吾尔自治区", province_confirm))
    elif province_name =="广西":
        data_list.append((province_name + "壮族自治区", province_confirm))
    elif province_name =="宁夏":
        data_list.append((province_name + "回族自治区", province_confirm))
    else:
        data_list.append((province_name + "省", province_confirm))

map=Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"lable":"1-99人","color":"#CCFFFFF"},
            {"min":100,"max":999,"lable":"100-999人","color":"#FFFF99"},
            {"min":1000,"max":4999,"lable":"1000-4999人","color":"#FF9966"},
            {"min":5000,"max":9999,"lable":"5000-9999人","color":"#FF6666"},
            {"min":10000,"max":99999,"lable":"10000-99999人","color":"#CC3333"},
            {"min":100000,"lable":"100000+","color":"#990033"}
        ]
    )
)
map.render("全国疫情地图.html")