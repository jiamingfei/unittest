import requests
import json
from views.get_data_excel import Get_data
def getTableHeader(request):
    url =Get_data(a=2,b=1)
    data = Get_data(a=2,b=2)
    cookies = {'ticket':"VFhwRlBRPT07TFM4bkxTMG5MeW9uOzMxMzE="}
    res = requests.get(url=url,data=data,cookies=cookies)
    response = json.dumps(res.json(),indent=4,ensure_ascii=False)
#     print(url,data)
    return [res.json()['message'],response]
# getTableHeader('requst')


def getItem(request):
    url = 'https://webapp.leke.cn/auth/global/evaluation/eva/manage/getItem.htm?schoolId=5855&typeId=182'
    data = {
        'schoolId': '5855',
        'typeId': '182'
    }
    cookies = {'ticket': "VFhwRlBRPT07TFM4bkxTMG5MeW9uOzMxMzE="}
    res = requests.get(url=url, data=data, cookies=cookies)
    response = json.dumps(res.json(),indent=4,ensure_ascii=False)
    return [res.json()['message'],response]

def divide(a,b):
    return a/b

def login(request):
    url = 'https://cas.leke.cn/login'
    data = {
        'ty': 'yyyyy',
        'loginName': '955002',
        'password': 'jia1234567@'
    }
    res = requests.request('post',url=url,data=data)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    return res.status_code

def getTemplateList(request):
    url = 'https://webapp.leke.cn/auth/global/evaluation/eva/manage/getTemplateList.htm?schoolId=88888888'
    data = {
        'schoolId':'88888888'
    }
    cookies = { 'ticket': "VFhwRlBRPT07TFM4bkxTMG5MeW9uOzMxMzE="}
    res = requests.get(url = url,data=data,cookies=cookies)
    response = json.dumps(res.json(), indent=4, ensure_ascii=False)
    return [res.json()['message'], response]
