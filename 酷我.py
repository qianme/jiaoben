import os
import requests
import time
import datetime


devId=''#设备ID

#签到
def sign():
    #看广告
    ggurl=f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=sign&adverId=20130802-13059416115&token=&extraGoldNum=88&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile='
    ggres=requests.get(ggurl).json()
    if ggres['data']['status'] == 1:
        print(f"观看签到广告获得{ggres['data']['obtain']}金币")
    else:
        print(f"观看签到广告：{ggres['data']['description']}")

# 看视频
def videoadver():
    url = f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=videoadver&goldNum=58&adverId=&token=&extraGoldNum=0&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; LE2110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36/ kuwopage'}
    res = requests.get(url, headers=headers).json()
    if res['data']['obtain'] != None:
        print(f'本次视频看完，获得{res["data"]["obtain"]}金币')
    else:
        print(f'看视频:{res["data"]["description"]}')
    # print(res)


# 听音乐时长
def listen():
    tt={5:43,10:57,20:60,30:99}
    for key in tt:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; LE2110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36/ kuwopage'}
        url = f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=listen&goldNum={tt[key]}&adverId=&token=&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile=&listenTime={key}'  # BUT0pYUGZWCtTEqP7%252Fbcg3jM9AfFms%252BqUqXGX3Z9qnHasq5uBs2gJbAmzkIzMPySU%252BU3nfUO8%252B%252BuD8gKrsI3MvA%253D%253D
        res = requests.get(url, headers=headers).json()
        if res['data']['obtain'] != None:
            print(f'本次音乐时长任务，获得{res["data"]["obtain"]}金币')
        # elif
        else:
            print(f'听音乐时长：{res["data"]["description"]}')
    # print(res)


# 抽奖
def lucky():
    url = f'https://integralapi.kuwo.cn/api/v1/online/sign/loterry/getLucky?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&source=kwplayer_ar_10.7.6.2_18.apk&type=free'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; LE2110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36/ kuwopage'}
    res = requests.get(url, headers=headers).json()
    if res['code'] == 200:
        print(f'本次抽奖获得{res["data"]["loterryname"]}')
    elif res["msg"] == "免费次数用完了":
        urls=f'https://integralapi.kuwo.cn/api/v1/online/sign/loterry/getLucky?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&source=kwplayer_ar_10.7.6.2_18.apk&type=video'
        rese=requests.get(urls,headers=headers).json()
        if rese['code'] ==200:
            print(f"本次抽奖获得{rese['data']['loterryname']}")
        else:
            print(f"所有抽奖次数都用完啦！")
        # print(rese)
    else:
        print(f'抽奖：{res["msg"]}')


#听歌曲
def moble():
    url=f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=mobile&goldNum=18&adverId=&token=&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile=&listenTime=0'
    res=requests.get(url).json()
    if res['data']['status'] == 1:
        print(f"今日听歌任务完成！获得{res['data']['obtain']}金币")
    else:
        print(f"今日听歌任务:{res['data']['description']}")

# moble()
#听故事
def novel():
    url=f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=novel&goldNum=18&adverId=&token=&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile=&listenTime=0'
    res=requests.get(url).json()
    if res["data"]["status"] == 1:
        print(f"本次听故事任务获得{res['data']['obtain']}金币")
    else:
        print(f'听故事{res["data"]["description"]}')
    # print(res)

#收藏
def collect():
    url = f'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen?loginUid={loginUid}&loginSid={loginSid}&appUid={appUid}&terminal=ar&from=collect&goldNum=18&adverId=&token=&clickExtraGoldNum=0&surpriseType=&verificationId=&mobile=&listenTime=0'
    res=requests.get(url).json()
    if res["data"]["status"] == 1:
        print(f"本次收藏任务获得{res['data']['obtain']}金币")
    else:
        print(f'收藏：{res["data"]["description"]}')
    # print(res)

def box():
    url = f'https://integralapi.kuwo.cn/api/v1/online/sign/new/newBoxFinish?loginUid={loginUid}&loginSid={loginSid}&devId={devId}&appUid={appUid}&source=kwplayer_ar_10.7.6.2_18.apk&version=kwplayer_ar_10.7.6.2&r=&action=new&time={timee}&goldNum=28&extraGoldnum=38&clickExtraGoldNum=0'
    res = requests.get(url).json()
    if res['data']['status'] == 1:
        print(f"本次开宝箱获得{res['data']['obtain']}金币")
    else:
        print(f"开宝箱：{res['data']['description']}")

if __name__=='__main__':
    #判断时间
    t = datetime.datetime.now().hour
    if 0 <= t < 8:
        timee = "00-08"
    elif 8 <= t < 10:
        timee = '08-10'
    elif 10 <= t < 12:
        timee = '10-12'
    elif 12 <= t < 14:
        timee = '12-14'
    elif 14 <= t < 16:
        timee = '14-16'
    elif 16 <= t < 18:
        timee = '16-18'
    elif 18 <= t < 20:
        timee = '18-20'
    else:
        timee = '20-24'


    #正式运行脚本
    idlist=os.getenv('kuwo')
    ids=idlist.split('&')
    for dis in ids:
        loginUid=dis.split('#')[0]
        loginSid=dis.split('#')[1]
        appUid=dis.split('#')[2]
        print('任务开始'.center(15,'_'))
        sign()#签到
        time.sleep(3)
        videoadver()#看视频
        time.sleep(3)
        if timee=='20-24':
            listen()#听音乐
            time.sleep(3)
        videoadver()#看视频
        time.sleep(3)
        box()#开宝箱
        time.sleep(3)
        lucky()#抽奖
        time.sleep(3)
        lucky()#抽奖
        time.sleep(3)
        moble()#听歌曲
        time.sleep(3)
        novel()#听故事
        time.sleep(3)
        collect()#收藏
        print("本次任务完成！".center(15,"_"))





