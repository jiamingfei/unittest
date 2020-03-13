import requests

def is_prime(number):
    if number<0 or number in (0,1):
        return False
    for element in range(2,number):
        if number % element ==0:
            return False
    return True

def add(a,b):
    return a+b

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

def getGroupDatas(request):
    url = 'https://oa.leke.cn/auth/oa/def/getGroupDatas.htm?orgId=6&bizType=2'
    data = {
        'orgId': '6',
        'bizType': '2'
    }
    cookies = { 'ticket':"VFdwclBRPT07TEMwbEx5d2xMU2dsOzI5Mjk="}
    res = requests.get(url = url,data=data,cookies=cookies)

    return [(res.json()['message']),res.json()]
#getGroupDatas('request')
#print(getGroupDatas('request')[1])