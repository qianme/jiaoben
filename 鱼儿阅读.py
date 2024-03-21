import requests
import re
import random
import time
import datetime
import os

key = "4fd70abe-75e5-42f4-85bb-23c988338521"

host = 'h5.127-server.xyz'


def url1():
    url = f'http://{host}/entry/pp'
    res = requests.get(url=url).json()
    url1 = res["jump"]
    # print(url1)
    return url1


def jump(Cookie):
    host1 = url1()
    host_re = f'http://(.*)/pi'
    host2 = re.findall(host_re, host1)[0]
    # print(host2)
    url = f"http://{host2}/read_task/get_read_url"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2d) NetType/4G Language/zh_CN",
        # "host": host2,
        "Cookie": Cookie
    }
    res = requests.get(url=url, headers=headers).text
    print(res)
    # jump = res['jump']
    # return jump


jump('PHPSESSID=fopbq05i89dvskcfabr9ulmdfr')


def do_read(Cookie, i):
    dict = {}
    iu_re = f'iu=(.*)'
    iu = re.findall(iu_re, jump(Cookie))[0]
    print(iu)
    # referer_re = f'(.*)/read'
    # referer = re.findall(referer_re, jump(Cookie))[0]
    r = random.uniform(0, 1)

    url = f"https://{host}/read_task/do_read?iu={iu}&type=7&pageshow&r={r}"
    headers = {
        # "Host":host,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2d) NetType/4G Language/zh_CN",
    }
    res = requests.get(url=url, headers=headers).text
    print(res)
    if 'jkey' in res:
        if "success_msg" in res:
            # print(res)
            return res["success_msg"]
        if "chksm" in res["url"]:
            print(res["url"])
            return "发现检测文章，跳过此账号！！！！！！"
            # ts(res["url"],i)
            # time.sleep(60)
        dict["jkey"] = res["jkey"]
    else:
        return "本轮阅读已经完成"

    n = 1
    while n < 31:
        print(f"开始阅读第{n}篇")
        jkey = dict["jkey"]
        time.sleep(6)
        re_url = f"https://{host}/read_task/do_read?iu={iu}&type=7&pageshow&r={r}&jkey={jkey}"
        res1 = requests.get(url=re_url)
        code = res1.status_code
        # print(url)
        if code == 200:
            res1 = res1.json()
            if 'jkey' in res1:
                print('阅读成功')
                if "chksm" in res1["url"]:
                    return "发现检测文章，跳过此账号！！！！！！"
                    # ts(res1["url"],i)
                    # time.sleep(60)
                dict["jkey"] = res1["jkey"]
                n += 1
                print("$" * 15)
            else:
                return "本轮阅读已经完成"
        else:
            res1 = res1.text
            return res1

    del dict["jkey"]


# def ts(url1,i):
#     uid="UID_34OJG1NUNGXO1XnA6hnGX2Ukf01Q"
#     token="AT_qiv1LekziJzktGaBDIu79sfyUxKcIEEh"
#     content = '''请在20秒内完成验证!\n<body onload="window.location.href='link'">'''
#     content = content.replace('link', url1)
#     headers={"Content-Type": "application/json"}
#     url_WXPusher ="https://wxpusher.zjiecode.com/api/send/message"
#     body={
#     "appToken":token,
#     "content":content,
#     "summary":f"账号{i}|检测文章-可乐\n",#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
#     "contentType":2,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
#     "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
#       123],
#       "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
#       uid,],
#       "url":url1, #原文链接，可选参数
#       #"verifyPay":false #是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
# }
#     res=requests.post(url=url_WXPusher,json=body,headers=headers).json()
#     print(res)
#     if res['success'] == True:
#         print(f"[通知]--->检测发送成功！")
#     else:
#         print(f"[通知]====>发送失败！！！！！")

def main():
    # kele = os.environ["yeyd"]
    kele='PHPSESSID=bc9v9re1i7gsv492pi6vhku7et&PHPSESSID=7tkebjkiunj1466gulbt3ohvir&PHPSESSID=bmcohnv1qnpsunfct4c5cvs3p6&PHPSESSID=3ocso4hnp5lj43tmsik4sr0ppd'
    list = kele.split('&')
    # list=['PHPSESSID=bc9v9re1i7gsv492pi6vhku7et',"PHPSESSID=bmcohnv1qnpsunfct4c5cvs3p6"]
    print(f"获取到{len(list)}个账号")
    i = 1
    for Cookie in list:
        print(f"第{i}个号正在阅读")
        print(do_read(Cookie, i))
        i += 1
        print("￥" * 15)
        time.sleep(10)


# main()
