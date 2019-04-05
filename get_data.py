import requests
import time

globals = {
    'true': 0,
    'false': 1
}


# 用来获取 时间戳
def gettime():
    return int(round(time.time() * 1000))


code = {"年末总人口": '"A030101"', "男性人口": '"A030102"', "女性人口": '"A030103"', "城镇人口": '"A030104"', "乡村人口": '"A030105"',
        "低龄人口": '"A030302"', "中龄人口": '"A030303"', "老龄人口": '"A030304"',
        "研究生招生数": '"A0M0A01"', "研究生在学人数": '"A0M0A02"', "研究生毕业人数": '"A0M0A03"', "出国留学人员": '"A0M0A04"',
        "学成回国留学人员": '"A0M0A05"',
        "用水总量": '"A0C0305"', "农业用水总量": '"A0C0306"', "工业用水总量": '"A0C0307"', "生活用水总量": '"A0C0308"', "生态用水总量": '"A0C0309"',
        "人均用水量": '"A0C030A"'
        }


def get_data(value):
    
    value=code[value]
    # 用来自定义头部的
    headers = {}
    # 用来传递参数的
    keyvalue = {}
    # 目标网址(问号前面的东西)
    url = 'http://data.stats.gov.cn/easyquery.htm'
    
    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'
    
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":' + value + '}]'
    keyvalue['k1'] = str(gettime())
    
    # 发出请求，使用get方法，这里使用我们自定义的头部和参数
    # r = requests.get(url, headers=headers, params=keyvalue)
    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.get(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    # print(r.status_code)
    # 再次进行请求
    # r = s.get(url, params=keyvalue, headers=headers)
    dic = dict(eval(r.text, globals))
    # 此时我们就能获取到我们搜索到的数据了
    print(dic['returndata']['wdnodes'][0]['nodes'][0]['cname'])
    data = {}
    for i in dic['returndata']['datanodes']:
        data[i['wds'][1]['valuecode']] = i['data']['data']
    
    for date in range(1999, 2009):
        keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"' + str(date) + '"}]'
        r = s.get(url, params=keyvalue, headers=headers)
        dic = dict(eval(r.text, globals))
        data[dic['returndata']['datanodes'][0]['wds'][1]['valuecode']] = dic['returndata']['datanodes'][0]['data'][
            'data']
    '''for i in dic['returndata']['datanodes']:
        data[i['wds'][1]['valuecode']]=i['data']['data']

    for date in range(1999,2009):
        keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"'+str(date)+'"}]'
        r = s.get(url, params=keyvalue, headers=headers)
        #data[i['wds'][1]['valuecode']] = i['data']['data']
        print(r.text)'''
    print(data)
    return data


'''for s in code:
    try:
        print(get_data(code[s]))
        print("\n")
    except:
        pass'''
#get_data(code["年末总人口"])