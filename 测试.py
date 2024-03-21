import httpx
import asyncio
# import requests


Host = 'http://wxr.jjyii.com'


headers = {
    'Host': 'wxr.jjyii.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'a_h_n': 'http%3A%2F%2F5851796cc98.eigqlyr.cn%2F%3Fa%3Dgt%26goid%3Ditrb%26_v%3D5123571253/23b9ff7b103745769a8a887105c2c4d3',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://5851796cc98.eigqlyr.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2d) NetType/WIFI Language/zh_CN',
    'Connection': 'keep-alive',
    'Referer': 'http://5851796cc98.eigqlyr.cn/'
    }
async def user():
    with httpx.Client() as client:
        url = f'{Host}/user/getinfo?v=5'
        res = httpx.post(url=url,headers=headers).json()
        id=res['data']['id']
        balance = res['data']['balance']
        print(f"ID：{id}|拥有金币{balance}")
        # await v13()


async def v13():
    with httpx.Client() as client:
        url = f'{Host}/r/get?v=13'
        body = {
            "o":"http://5851776e164.eigqlyr.cn/?a=gt&goid=itrb&_v=5123571253&t=quick"
        }
        res = client.post(url=url,headers=headers,data=body).json()
        print(res)
        data_url=res['data']['url']
        # asyncio.sleep(10)
        return data_url
        # print(data_url)
        # if data_url != None:
        #     await wxpuser(url)
        #     asyncio.sleep(10)
        #     await v20()
        # else:
        #     print('本轮阅读已结束！')

async def v20():
    with httpx.Client() as client:
        url = f"{Host}/r/ck?v=20"
        body = {
            "t":"quick",
            "t2":2,
            "r1":"9197079d1964d0b5aa6df76fb0919f531700894807245",
            "r2":"c5cb4525ea6bfffde429cf9daaa07afa",
            "r3":135
        }
        res = client.post(url=url,data=body,headers=headers).text
        print(res)
        # await user()
    
async def wxpuser(url,i):
    with httpx.Client() as client:
        #uid="UID_34OJG1NUNGXO1XnA6hnGX2Ukf01Q"#宝的
        #uid='UID_0hclUZCe7BmOZl5gFWiRkQgUuN2R'#小号
        uid = 'UID_vwlpx9TGd9SSOKG9ACaJXmCAN9SG'
        #token="AT_qiv1LekziJzktGaBDIu79sfyUxKcIEEh"#我宝的
        token = 'AT_lHJcAk4T8r4VjYIioWaHqMXOKKp7fBAI'
        content = '''请在20秒内完成验证!\n<body onload="window.location.href='link'">'''
        content = content.replace('link', url)
        headers={"Content-Type": "application/json"}
        url_WXPusher ="https://wxpusher.zjiecode.com/api/send/message"
        body={
        "appToken":token,
        "content":content,
        "summary":f"账号{i}检测文章-可乐",#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
        "contentType":2,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown 
        "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
        123],
        "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
        uid,],
        "url":url, #原文链接，可选参数
        #"verifyPay":false #是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
    }
        res=client.post(url=url_WXPusher,json=body,headers=headers).json()
        print(res)
        if res['success'] == True:
            print(f"[通知]--->检测发送成功！")
            asyncio.sleep(60)
        else:
            print(f"[通知]====>发送失败！！！！！")


async def main():
    result = await user()
    n = 1
    while n<30:
        result1 = await v13()
        print(result1)
        if result1 != None:
            result2 = await v20()
        else:
            print('本轮已经结束')
            return '$'*30



# if __name__=="__main__":
#     kele = os.environ["klyd"]
#     list=kele.split('&')
#     max_concurrency = 1  
#     print(f"获取到{len(list)}个账号")
#     with Pool(processes=len(list)) as pool:

#             thread_pool = ThreadPool(max_concurrency)

#             thread_pool.starmap(check, [(kele, i) for i, kele in enumerate(list, start=1)])
# asyncio.run(user())
asyncio.run(main())









# def wxpuser(url,i):
#     #uid="UID_34OJG1NUNGXO1XnA6hnGX2Ukf01Q"#宝的
#     #uid='UID_0hclUZCe7BmOZl5gFWiRkQgUuN2R'#小号
#     uid = 'UID_vwlpx9TGd9SSOKG9ACaJXmCAN9SG'
#     # token="AT_qiv1LekziJzktGaBDIu79sfyUxKcIEEh"
#     token='AT_lHJcAk4T8r4VjYIioWaHqMXOKKp7fBAI'
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
# url = 'http://baidu.com'
# wxpuser(url,1)