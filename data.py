# -*- coding:utf-8 -*-
from database import*


db=DB()
db.init()
db.create()

for name in code.keys():
    dic=get_data(name)
    db.update(name,dic)



db.save()

