## 一、 实现原理

登陆国家统计局网站[http://data.stats.gov.cn/easyquery.htm](http://data.stats.gov.cn/easyquery.htm)，审查元素（我用的火狐浏览器），

![](/home/chaf/Program/Python/HW/image/1.png)

在"网络"—“XHR”一项可以观察到有一个POST和两个GET，其中m=QueryData的响应就含有我们所要的数据

当前主页面参数如下：

![](/home/chaf/Program/Python/HW/image/2.png)

由于没有选定项目，dfwds依旧是空，当从页面中选定某项时，比如选择“人口”—“总人口”：

![](/home/chaf/Program/Python/HW/image/3.png)

此时可以观察到多出来两个新的请求与响应，新的响应参数为：

![](/home/chaf/Program/Python/HW/image/4.png)

多次试验之后发现，wdcode的值一直都是“zb”，而valuecode的取值与所选项有关。更进一步，在“响应”中观察到

![](/home/chaf/Program/Python/HW/image/5.png)

注意到一个项目下的类别的valuecode为项目valuecode加上一后缀，像人口分布为“A0301”，人口分布下的年末总人口为“A030101”, “男性人口”为 “A030102”等。利用这一点就可以进行数据爬取。

## 二、程序设计

### （一）文件结构

整个项目由5个python文件构成，其中，get_data.py包含获取数据的函数和valuecode字典；plot.py包含绘图的类与方法；database.py包含数据库操作的类和方法；data.py为获取数据的脚本；plotting.py为绘图的脚本。爬取到的数据将保存在./data/data.db中，绘制的图也将保存在./data中。

### （二）用到的库

#### 1、requests

进行http请求与获取响应

#### 2、sqlite3

进行数据库操作

#### 3、matplotlib

数据可视化

### （四）主要用到的类和方法

#### 1、plot

##### （1）作用：

绘图类

##### （2）方法

- init ：初始化，主要是设置中文显示和解决负号显示
- rect：绘制直方图
- line：绘制折线图
- pie：绘制饼状图

#### 2、DB

##### （1）作用：

数据库类

##### （2）方法

- init ：初始化数据库
- create：创建数据库
- update：更新数据库
- select：选择数据
- save：保存数据

## 三、实验结果分析

### （一）年末总人口直方图

![](/home/chaf/Program/Python/HW/data/%E5%B9%B4%E6%9C%AB%E6%80%BB%E4%BA%BA%E5%8F%A3.png)

从图中可见，中国年末总人口数自1999年以来保持稳定每年略有增长。

### （二）性别人口变化趋势

![](/home/chaf/Program/Python/HW/data/%E6%80%A7%E5%88%AB%E4%BA%BA%E5%8F%A3.png)

从图中可见，中国不同性别的人口数量逐年增长，且男性人口多于女性人口。

### （三）人口区域分布变化趋势

![](/home/chaf/Program/Python/HW/data/%E4%BA%BA%E5%8F%A3%E5%8C%BA%E5%9F%9F%E5%88%86%E5%B8%83%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png)

从图可见，从1999到现在，乡村人口在逐年减少而城镇人口在增加，表明近些年有许多乡村人口到城镇工作。

### （四）出国留学人数变化趋势

![](/home/chaf/Program/Python/HW/data/%E5%87%BA%E5%9B%BD%E7%95%99%E5%AD%A6%E6%83%85%E5%86%B5.png)

从图可知留学生人数与海归学生人数逐年增多，这与中国教育事业的发展、社会经济水平的提高和综合国力的发展有密不可分的关系。（最后的下滑是因为2018年数据缺失）

### （五）2017年人口年龄结构

![](/home/chaf/Program/Python/HW/data/2017%E5%B9%B4%E4%BA%BA%E5%8F%A3%E5%B9%B4%E9%BE%84%E6%AF%94%E4%BE%8B.png)

由图可见，老龄人口11.4%已表明我国社会已进入老龄化阶段（国际一般标准：60岁以上的人口占总人口比例达到10%，或65岁以上人口占总人口的比重达到7%）

### （六）2017年用水比例

![](/home/chaf/Program/Python/HW/data/2017%E5%B9%B4%E7%94%A8%E6%B0%B4%E6%AF%94%E4%BE%8B.png)

由图可见用水比例最大的为农业用水。

## 四、实验评估

1、此实验难度适中，在解决http问题之后便好办很多。

2、本实验基于Ubuntu18.04LTS，在matplotlib的中文支持上折腾了一番。

3、爬取数据依旧需要实现获得目标valuecode，暂时无法做到全自动爬取。