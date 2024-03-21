import requests
import random
import os
import time
import re

from multiprocessing import Pool

from multiprocessing.pool import ThreadPool
import threading

forstr = ""  # 此处为助力码
key = "4fd70abe-75e5-42f4-85bb-23c988338521"

ua_list = [
    "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20231002 MMWEBID/3669 MicroMessenger/8.0.43.2480(0x28002B38) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2c) NetType/4G Language/zh_CN", ]
ua = random.choice(ua_list)


def lg():
    url = 'http://m.cdcd.plus/entry/new_lg'
    res = requests.get(url=url).text
    # host = res['jump'].split("/")[2]
    print(res)
    # return host


# 获取阅读链接
def getread(Cookie):
    # x = f'(.*)zs'
    # url = re.findall(x,xx(Cookie))[0]
    url = f"http://m365729.xedi8rkn.shop/new/get_read_url?for={forstr}"

    headers = {
        "User-Agent": ua,
        "Cookie": Cookie,
        # "Host": m365729.xedi8rkn.shop,
    }

    read = requests.get(url=url, headers=headers).json()
    x = read["jump"]
    list = x.split("read?")
    # print(list)
    return list


def draw(Cookie,user):
    headers = {
        "User-Agent": ua,
        "Cookie": Cookie,
        "Host": 'm365729.xedi8rkn.shop',
    }
    tuijian=requests.get('http://m365729.xedi8rkn.shop/tuijian',headers=headers).json()
    score=int(tuijian['data']['user']['score'].split('.')[0])
    if score>=30:
        url='http://m365700.xedi8rkn.shop/withdrawal/doWithdraw'
        data={'amount':score,'type':'wx'}
        res=requests.post(url,headers=headers,data=data).text
        codes = f'"code":(.*),"msg'
        code = re.findall(codes,res)
        code = int(code[0])
        if code == 0:
            print(f'本次体现{score/100}元')
        else:
            print(f'体现失败，请尝试手动体现')
    else:
        print(f'{user}余额不足,当前余额{score/100}元'.center(30,"💴"))


def do_read(Cookie, user):
    dict = {}
    referer = f"http://m365729.xedi8rkn.shop/new"
    # host1=getread(Cookie,host,ua)[0]
    iu = getread(Cookie)[1]
    num1 = random.uniform(0, 1)
    num2 = random.uniform(0, 1)
    url = f"http://m365729.xedi8rkn.shop/tuijian/do_read?for={forstr}&zs=&pageshow&r={num1}&{iu}"
    headers = {
        "Host": 'm365729.xedi8rkn.shop',
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Referer": referer,
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*"
    }
    # print(url)
    res = requests.get(url=url, headers=headers).json()
    # print(res['url'])

    if "success_msg" in res:
        # print(res)
        return res["success_msg"]
    try:
        if "chksm" in res["url"]:
            wxpuser(res["url"], user)
            time.sleep(30)
        dict["jkey"] = res["jkey"]
        # jkey=dict["jkey"]
        n = 1
        while n < 31:
            # try:
                print(f"账号{user}|开始阅读第{n}篇")
                jkey = dict["jkey"]
                time.sleep(3)
                re_url = f"http://m365729.xedi8rkn.shop/tuijian/do_read?for={forstr}&zs=$pageshow&r={num2}&{iu}&jkey={jkey}"
                res1 = requests.get(url=re_url, headers=headers)
                code = res1.status_code
                # print(url)
                # print(res1)
                if code == 200:
                    res1 = res1.json()
                    # print(res1)
                    msg = res1["success_msg"]
                    if msg == "本轮阅读已完成":
                        print(f"账号{user}|{msg}")
                        draw(Cookie,user)
                        return "$" * 20
                    elif "阅读成功" in msg:
                        print(f"账号{user}|{msg}")
                        if "chksm" in res1["url"]:
                            if res1['url'] == None:
                                return print('检测文章url未生成，请过段时间重试！')
                            else:
                                wxpuser(res1["url"], user)
                                time.sleep(30)
                        dict["jkey"] = res1["jkey"]
                        n += 1
                    else:
                        print(f"账号{user}|检测未通过！！！")
                        draw(Cookie, user)
                        return res1
                else:
                    res1 = res1.text
                    return res1
            # except Exception as e:
            #     print(f'未知错误：{e}')
                n + 1
        del dict["jkey"]
    except:
        print('未获取到检测URL，请果断时间重试！')


def wxpuser(url, user):
        uid='UID_0hclUZCe7BmOZl5gFWiRkQgUuN2R'#小号
        # uid = 'UID_HQbK6SQvaQVlJcMRGd4lvVbu7FbN'  # 小黑
        # token="AT_xvmcniW2lUpwFJVTGv6ql54bTskpy4LD"#小黑
        token='AT_MQ2YndKLrFznFX95HsR7LFxN57IRhrHp'#小号
        #token = 'AT_lHJcAk4T8r4VjYIioWaHqMXOKKp7fBAI'
        content = '''请在20秒内完成验证!\n<body onload="window.location.href='link'">'''
        content = content.replace('link', url)
        headers={"Content-Type": "application/json"}
        url_WXPusher ="http://wxpusher.zjiecode.com/api/send/message"
        body={
        "appToken":token,
        "content":content,
        "summary":f"账号{user}检测文章-可乐",#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
        "contentType":2,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
        "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
          123],
          "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
          uid,],
          "url":url, #原文链接，可选参数
          #"verifyPay":false #是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
    }
        res=requests.post(url=url_WXPusher,json=body,headers=headers).json()
        # print(res)
        if res['success'] == True:
            print(f"[通知]--->检测发送成功！")
        else:
            print(f"[通知]====>发送失败！！！！！")
    # f = datetime.datetime.now()
    # f1 = f.hour
    # f2 = f.minute
    # f3 = f.second
    # 任务时间 = f"{f1}:{f2}:{f3}"
    # url1 = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key
    # payload = {
    #     "msgtype": "news",
    #     "news": {
    #         "articles": [
    #             {
    #                 "title": f"账号{user}|{任务时间}",
    #                 "description": "请在60秒之内点击链接",
    #                 "url": url,
    #                 "picurl": "http://tc.562455.xyz/i/2023/11/19/6559b6c7d6ac5.png"
    #             }
    #         ]
    #     }
    # }
    # res = requests.post(url1, json=payload).text


def check(Cookie):
    # url = f" http://{m365729.xedi8rkn.shop}/zs?for={forstr}"
    url='http://m365729.xedi8rkn.shop/tuijian'
    # print(url)
    headers = {
        "User-Agent": ua,
        "Cookie": Cookie,
        # "Host": m365729.xedi8rkn.shop,
    }
    # print(headers)
    res = requests.get(url=url, headers=headers).json()
    # print(res)
    user=res['data']['user']['username']
    rest=res["data"]['infoView']["rest"]
    if rest == 0:
        msg = res["data"]["infoView"]["msg"]
        print(f"账号{user}|{msg}".center(30,'*'))
        # draw(Cookie,user)
        return "¥" * 20
    else:
        print(f'{user}剩余{rest}篇文章')
        do_read(Cookie, user)


if __name__ == "__main__":
    # kele = os.environ["bhkl"]
    kele='PHPSESSID=hlpn7vqi50u53rru61ht57fvh9; udtauth3=ec4806I18S5DRH8qgfGCEABEzXm6fIRIccxl%2FZ5sdS7a7eWUjHh2kTn2AQKMou5wygCiIaoWP47SiYlFITc2pZ0hhJGtbogfPvUdD%2BTTD0b1KVxutAiZwMj%2FHGDAZ5oURwkdfpvshCTq91nZdshl9f0QJjVcMlDTcqKfOeio0DY&udtauth3=1fe9TP7jzsDNTFnxnlJXk0LGYWcamdbYcf4c1H4I9723bcX4jrg1zdosx0gLaV3xM3erE8%2FJGptRSGsVr5quX1fFy77rPSx5TsYt%2BpUrT35Vdj5vSNKObGLJmKNF8gxQvBr2skPofMdnZCULiUKCsQuf8hrEsIlM%2BvncrdR9ywE; PHPSESSID=g2ks6esdbj0e85eksih3dhda4n&PHPSESSID=7b0rav1l0aihealq58r3o386h7; udtauth3=f879Vp7MdFeOgBvlw4rKZ7x%2FEsG55%2B2BLUgqXsaBsmXHS0wlf5SRxK4dafdIsPa5xNXkXPeqDWiUJcSHGZtWjEBBVAEzPb%2BtaLb5VxaNck2QX4mTJkHli%2B9zB2x9ujQsabOAqlD%2BQ5FM6KV3001TPu2AdpyEL4Snl%2BiJU4XX4Dc'
    # kele='PHPSESSID=ct9j2o45b051j5omujnmjdlrgj; udtauth3=fc72gSShlyS8vIE3m%2BXbmvsTBfX850mDm1bBPh%2FHsrNFzsbt8JUdx9bkWJsjgDc4j4NRC7zWNPw%2BzkNbh%2BwMLnejs76iIO13sP4d4SMcuywY2JJQtGbnF5t0tI0KKNPVXGN9nbLwwBs%2BwxUscO2ALVRhrYuBchCk2KQYyxtOqa0'
    list = kele.split('&')
    # print(list)
    max_concurrency = 1
    print(f"获取到{len(list)}个账号")
    with Pool(processes=len(list)) as pool:
        thread_pool = ThreadPool(max_concurrency)

        # thread_pool.starmap(check, [kele for kele in enumerate(list, start=1)])
        thread_pool.map(check,list)


