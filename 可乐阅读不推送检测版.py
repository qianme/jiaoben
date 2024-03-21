import requests
import random
import time
import os
import datetime
import time

from multiprocessing import Pool

from multiprocessing.pool import ThreadPool
import threading



forstr = " " #此处为助力码
#oWimAi

ua_list = ["Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20231002 MMWEBID/3669 MicroMessenger/8.0.43.2480(0x28002B38) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2c) NetType/4G Language/zh_CN",]
ua=random.choice(ua_list)

def lg():
    url = 'https://m.cdcd.plus/entry/new_lg'
    res = requests.get(url=url).json()
    host = res['jump'].split("/")[2]
    #print(host)
    return host
    
#获取阅读链接
def getread(Cookie):
    # x = f'(.*)zs'
    # url = re.findall(x,xx(Cookie))[0]
    url=f"http://{lg()}/new/get_read_url?for={forstr}"
    
    headers={
        "User-Agent": ua,
        "Cookie": Cookie,
        "Host": lg(),
    }
    
    read=requests.get(url=url,headers=headers).json()
    x=read["jump"]
    list=x.split("read?")
    #print(list)
    return list


def do_read(cookie,i,uid):
    dict={}
    referer=f"http://{lg()}/new"
    #host1=getread(Cookie,host,ua)[0]
    iu=getread(Cookie)[1]
    num1=random.uniform(0,1)
    num2=random.uniform(0,1)
    url=f"http://{lg()}/tuijian/do_read?for={forstr}&zs=&pageshow&r={num1}&{iu}"
    headers={
        "Host":lg(),
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Referer": referer,
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*"
    }
   # print(url)
    res=requests.get(url=url,headers=headers).json()
    print(res)

    if "success_msg" in res:
        # print(res)
        return res["success_msg"]
    if "chksm" in res["url"]:
        print(res["url"])
        return '发现检测文章，跳过此账号！！！！'
        # wxpuser(res["url"],i,uid)
        # time.sleep(30)
    dict["jkey"]=res["jkey"]
    #jkey=dict["jkey"]
    n=1
    while n < 31:
        try:
            print(f"账号{i}|开始阅读第{n}篇")
            jkey=dict["jkey"]
            time.sleep(3)
            re_url=f"http://{lg()}/tuijian/do_read?for={forstr}&zs=$pageshow&r={num2}&{iu}&jkey={jkey}"
            res1=requests.get(url=re_url,headers=headers)
            code = res1.status_code
            print(url)
            print(res1)
            if code == 200:
                res1=res1.json()
                #print(res1)
                msg=res1["success_msg"]
                if msg=="本轮阅读已完成":
                    print(f"账号{i}|{msg}")
                    return "$"*20
                elif "阅读成功" in msg:
                    print(f"账号{i}|{msg}")
                    if "chksm" in res1["url"]:
                        # print("发现检测文章，跳过次账号")
                        return "发现检测文章，跳过次账号"
                        # wxpuser(res1["url"],i,uid)
                        # time.sleep(30)
                    dict["jkey"]=res1["jkey"]
                    n += 1
                    print("$"*15)
                else:
                    print(f"账号{i}|系统错误，请检测")
                    return res1
            else:
                res1=res1.text
                return res1
        except Exception as e:
            print(f'未知错误：{e}')
            n+1
            
    del dict["jkey"]


# def wxpuser(url,i,uid):
#     token="AT_qiv1LekziJzktGaBDIu79sfyUxKcIEEh"
#     content = '''请在20秒内完成验证!\n<body onload="window.location.href='link'">'''
#     content = content.replace('link', url)
#     headers={"Content-Type": "application/json"}
#     url_WXPusher ="https://wxpusher.zjiecode.com/api/send/message"
#     body={
#     "appToken":token,
#     "content":content,
#     "summary":f"账号{i}检测文章-可乐",#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
#     "contentType":2,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown 
#     "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
#       123],
#       "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
#       uid,],
#       "url":url, #原文链接，可选参数
#       #"verifyPay":false #是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
# }
#     res=requests.post(url=url_WXPusher,json=body,headers=headers).json()
#     print(res)
#     if res['success'] == True:
#         print(f"[通知]--->检测发送成功！")
#     else:
#         print(f"[通知]====>发送失败！！！！！")

def check(Cookie,i):
    cookie = Cookie.split('@')[0]
    uid = Cookie.split('@')[1]
    url=f" http://{lg()}/zs?for={forstr}"
    headers={
        "User-Agent": ua,
        "Cookie":Cookie,
        "Host": lg(),
    }
    res=requests.get(url=url,headers=headers).json()
    #print(url)
    #print(res)
    if "msg" in res["data"]["info"]:
        msg=res["data"]["info"]["msg"]
        print(f"账号{i}|{msg}")
        return "¥"*20
    else:
        do_read(cookie,i,uid)

   
if __name__=="__main__":
    kele = os.environ["bhkl"]
    list=kele.split('&')
    max_concurrency = 5  
    print(f"获取到{len(list)}个账号")
    with Pool(processes=len(list)) as pool:

            thread_pool = ThreadPool(max_concurrency)

            thread_pool.starmap(check, [(kele, i) for i, kele in enumerate(list, start=1)])
