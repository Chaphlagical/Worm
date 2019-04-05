# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib

colors=['red','blue','green','orange','black']

class plot():
    
    def init(self):
        matplotlib.rcParams['font.serif'] = ['simhei']
        matplotlib.rcParams['axes.unicode_minus'] = False
    
    def rect(self,dict,name):
        label=dict.keys()
        num=[dict[i] for i in dict.keys()]
        x=range(len(num))
        fig=plt.figure(figsize=(20,12))
        rects1 = plt.bar(left=x, height=num, width=0.5, alpha=0.8, color='red')
        plt.ylim(0, max(num)*6/5)
        plt.ylabel(name)
        plt.xticks([index for index in x], label)
        plt.xlabel("年份")
        plt.title(name+'关于年份的变化趋势')
        plt.savefig("./data/" + name + ".png")
    
    def line(self,dict_list,name_list,y_label):
        fig = plt.figure(figsize=(20, 12))
        year=list(dict_list[0].keys())
        color=colors[0:len(name_list)]
        for i in range(len(name_list)):
            y_data=[dict_list[i][x] for x in year]
            label=name_list[i]
            plt.plot([str(y) for y in year],y_data,c=color[i],label=label)
        plt.xlabel("年份")
        plt.ylabel(y_label)
        plt.legend(loc='upper left')
        plt.title(y_label+"与年份的关系")
        plt.savefig("./data/" + y_label + ".png")

    def pie(self,labels,fracs,name):
        fig = plt.figure(figsize=(20, 20))
        plt.pie(x=fracs, labels=labels,  autopct='%3.1f %%',
                shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6
                )
        plt.title(name)
        plt.savefig("./data/" + name + ".png")