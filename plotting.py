# -*- coding:utf-8 -*-
from plot import *
from database import*

plt=plot()
db=DB()
db.init()

db.select("年末总人口")
plt.rect(db.selection,"年末总人口")

name_list=["男性人口","女性人口"]
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection)
plt.line(data_list,name_list,"性别人口")

name_list=["城镇人口","乡村人口"]
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection)
plt.line(data_list,name_list,"人口区域分布变化趋势")

name_list=["出国留学人员","学成回国留学人员"]
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection)
plt.line(data_list,name_list,"出国留学情况")

name_list=["农业用水总量", "工业用水总量", "生活用水总量","生态用水总量","人均用水量"]
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection[2017])
plt.pie(name_list,data_list,"2017年用水比例")

name_list=["低龄人口", "中龄人口", "老龄人口"]
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection[2017])
plt.pie(name_list,data_list,"2017年人口年龄比例")