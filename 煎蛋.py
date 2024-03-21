import time
from urllib.parse import quote

import requests


def times():
    ts = int(time.time() * 1000)
    curr = time.localtime()
    timestamp = time.strftime('%Y%m%d%H%M%S', curr)
    return timestamp, ts


timestamp, ts = times()


# 页面
def encrypt():
    data = {
        "encrypt_operation": "ecb",
        "encrypt_padding": "PKCS7",
        "encrypt_len": "256",
        "encrypt_key": "SFV2fb8D09jreH2Xdf4M0FGk5Di2DX2O",
        "encrypt_iv": "null",
        "encrypt_value": f"exposureType=1&pageSize=20&pageIndex=1&ClientTime={timestamp}",
        "encrypt_aad": ""
    }
    headers = {
        "Host": "server.try8.cn",
        "Connection": "keep-alive",
        "Content-Length": "217",
        "sec-ch-ua": "\"Chromium\";v=\"118\", \"Android WebView\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
        "sign": "eyJ1c2VyX2lkIjoiIiwidG9rZW4iOiIifQ==",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://try8.cn",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://try8.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    res = requests.post('https://server.try8.cn/tool/cipher/aes/encrypt', json=data, headers=headers)
    ase_encrypt = res.json()['data']['aes_encrypt']
    return ase_encrypt


def list():
    headers = {
        "channel": "jiandan",
        "pkgName": "com.cq.jdcover",
        "encryption": "1",
        "version": "3.0.0.8",
        "timeZoom": "GMT+08:00",
        "timeSpan": str(ts),
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg2NzU2NDQsImV4cCI6MTcwODc2MjM0NCwiaWF0IjoxNzA4Njc1OTQ0fQ.kYcjKLus0bSlloRtXc8tMot7WqglSQmPnOeFW_Un6dU",
        "AchievementIds": "[27]",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Content-Length": "64",
        "Host": "api.zzmdwl.cn",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.12.13"
    }
    data = encrypt()
    res = requests.post('https://api.zzmdwl.cn/Tasks/Exposure/GetPageExposureList', data=data, headers=headers).json()
    print(res)


# 余额
def aes():
    headers = {
        "sign": "eyJ1c2VyX2lkIjoiIiwidG9rZW4iOiIifQ==",
    }
    data = {
        "encrypt_operation": "ecb",
        "encrypt_padding": "PKCS7",
        "encrypt_len": "256",
        "encrypt_key": "SFV2fb8D09jreH2Xdf4M0FGk5Di2DX2O",
        "encrypt_iv": "null",
        "encrypt_value": f"cashOutType=0&ClientTime={timestamp}",
        "encrypt_aad": ""
    }
    res = requests.post("https://server.try8.cn/tool/cipher/aes/encrypt", data=data, headers=headers).json()
    ase = res['data']['aes_encrypt']
    return ase


def KS():
    headers = {
        "encryption": "1",
        "timeSpan": str(ts),
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg2NzU2NDQsImV4cCI6MTcwODc2MjM0NCwiaWF0IjoxNzA4Njc1OTQ0fQ.kYcjKLus0bSlloRtXc8tMot7WqglSQmPnOeFW_Un6dU"
    }
    res = requests.get(f'https://api.woaizhuanqian9.cn/SysBase/User/GetUserCashOutBasicInfo?KSystemWork={aes()}',
                       headers=headers).json()
    print(res)


# 领取
def Gain():
    headers = {
        "channel": "jiandan",
        "pkgName": "com.cq.jdcover",
        "encryption": "1",
        "version": "3.0.0.8",
        "timeZoom": "GMT+08:00",
        "timeSpan": str(int(time.time() * 1000)),
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg2NzU2NDQsImV4cCI6MTcwODc2MjM0NCwiaWF0IjoxNzA4Njc1OTQ0fQ.kYcjKLus0bSlloRtXc8tMot7WqglSQmPnOeFW_Un6dU",
        "AchievementIds": "[27]",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Content-Length": "64",
        "Host": "api.zzmdwl.cn",
        "Connection": "Keep-Alive",
        "User-Agent": "http/3.12.13"
    }
    data = encrypt()
    res = requests.post("https://api.zzmdwl.cn/Tasks/Exposure/GainExposure", headers=headers, data=data).json()
    print(res)


def url(text):
    str = quote(text,'utf-8')
    # print(str)
    return str


def base(key, text):
    headers = {
        "Host": "server.try8.cn",
        "Connection": "keep-alive",
        "Content-Length": "217",
        "sec-ch-ua": '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
        "sign": "eyJ1c2VyX2lkIjoiIiwidG9rZW4iOiIifQ==",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://try8.cn",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://try8.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "encrypt_operation": "ecb",
        "encrypt_padding": "PKCS7",
        "encrypt_len": "256",
        "encrypt_key": key,
        "encrypt_iv": "null",
        "encrypt_value": text,
        "encrypt_aad": ""
    }
    res = requests.post('https://server.try8.cn/tool/cipher/aes/encrypt', json=data, headers=headers).json()
    ase = res['data']['aes_encrypt']
    # print(ase)
    return ase


def login(user, password):
    Text = '{"account":' + f'"{user}"' + ',"deviceId":"262f4677ade11232","password":' + f'"{url(base("q7LxfQk7EBcaJIWB5QzE85vekGJP7FXa", password))}' + '%0A","ClientTime":' + timestamp + '}'
    # print(Text)
    headers = {
        "channel": "jiandan",
        "pkgName": "com.cq.jdcover",
        "encryption": "1",
        "version": "3.0.0.8",
        "timeZoom": "GMT+08:00",
        "timeSpan": str(ts),
        # "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5ri45a6iIiwiSWQiOiIwIiwiQWNjb3VudCI6IjAiLCJBcHBVc2VyUm9sZVR5cGUiOiIwIiwiSXNTZGtTZXJ2aWNlIjoiMCIsIm5iZiI6MTcwODgwMTMyMywiZXhwIjoxNzA4ODg4MDIzLCJpYXQiOjE3MDg4MDE2MjN9.JmI35Yg1NlJoa3SUMfY_Lzq6uZ8T-8ii6MnK4T2SxFk",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg2NzU2NDQsImV4cCI6MTcwODc2MjM0NCwiaWF0IjoxNzA4Njc1OTQ0fQ.kYcjKLus0bSlloRtXc8tMot7WqglSQmPnOeFW_Un6dU",
        "AchievementIds": 'NoData',
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": "260",
        "Host": "api.zzmdwl.cn",
        "Connection": "gzip",
        "User-Agent": "okhttp/3.12.13"
    }
    data = base('SFV2fb8D09jreH2Xdf4M0FGk5Di2DX2O', Text)
    # print(data)
    res = requests.post('https://api.zzmdwl.cn/SysBase/Account/SingInNormal', headers=headers, data=data).json()
    print(res)


# user = "13194929316"
user='15878265826'
password='woaini1320'
# deviceId='0CFD122D82724A6EB2830E3919239454a9765287aba90c2b5f0b6745f1bce61a'
# password = "my123456"
login(user, password)

