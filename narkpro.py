import httpx
import requests
import json

#登陆

def sendSms():
    phone = int(input('请在60s秒内输入手机号码：'))
    if phone == None:
        print('没有输入手机号，已退出')
    else:
        url='http://nark.562455.xyz/sms/SendSMS'
        data={
        "phone": f'{phone}',
        }
        res=requests.post(url,json=data).json()
        print(res)
        if res['success'] == True:
            code(phone)
        else:
            print('短信发送失败，请检查手机号是否正确(或者联系管理员)')

def code(phone):
    code=int(input('请收到验证码后再60s内回复：'))
    url='http://nark.562455.xyz/sms/VerifyCode'
    data={
    "phone": f'{phone}',
    "code": f'{code}',
    }
    res=requests.post(url,json=data).text
    print(res)
    if res['success'] == True:
        print('登录成功')
    else:
        print('d登录失败，请稍后重试！')
sendSms()