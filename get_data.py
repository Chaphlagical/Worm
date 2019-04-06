import requests
import time

globals = {
    'true': 0,
    'false': 1
}


# 用来获取 时间戳
def gettime():
    return int(round(time.time() * 1000))

# 相关内容对应的valuecode
code = {"年末总人口": '"A030101"', "男性人口": '"A030102"', "女性人口": '"A030103"', "城镇人口": '"A030104"', "乡村人口": '"A030105"',
        "低龄人口": '"A030302"', "中龄人口": '"A030303"', "老龄人口": '"A030304"',
        "研究生招生数": '"A0M0A01"', "研究生在学人数": '"A0M0A02"', "研究生毕业人数": '"A0M0A03"', "出国留学人员": '"A0M0A04"',
        "学成回国留学人员": '"A0M0A05"',
        "用水总量": '"A0C0305"', "农业用水总量": '"A0C0306"', "工业用水总量": '"A0C0307"', "生活用水总量": '"A0C0308"', "生态用水总量": '"A0C0309"',
        "人均用水量": '"A0C030A"'
        }

# 获取数据
def get_data(value):
    
    value=code[value]
    headers = {}
    keyvalue = {}
    url = 'http://data.stats.gov.cn/easyquery.htm'

    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'
    
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":' + value + '}]'
    keyvalue['k1'] = str(gettime())
    
    s = requests.session()
    r = s.get(url, params=keyvalue, headers=headers)
    dic = dict(eval(r.text, globals))
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
    print(data)
    return data


