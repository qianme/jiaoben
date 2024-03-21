import requests
import random
import json
import os
from datetime import datetime, time
from time import sleep

def openbox():
    url = "https://speciesweb.whjzjx.cn/v1/box/open"
    data = {
        "config_id": 3
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    msg = response_json['msg']
    if msg == 'success':
        coin_val = response_json['data']['coin_val']
        Text(f'开宝箱获得>>>{coin_val}币')
        # 随即延迟
        randomtime()
        boxvideo(coin_val)
    else:
        Text(f'开宝箱错误>>>{msg}')


def boxvideo(coin_val):
    url = "https://speciesweb.whjzjx.cn/v1/box/view_ad"
    data = {
        "config_id": 3,
        "coin_val": coin_val,
        "ad_num": 1
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    msg = response_json['msg']
    if msg == 'success':
        coin_val = response_json['data']['coin_val']
        Text(f'看宝箱视频获得>>>{coin_val}币')
    else:
        Text(f'看宝箱视频错误>>>{msg}')


def randomtime():

    random_number = random.randint(15, 25)
    sleep(random_number)
    return


def videocoin():
        url = "https://speciesweb.whjzjx.cn/v1/sign"
        data = {
            "type": 4,
            "mark": 1
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        Text(response.text)
        response_json = response.json()
        msg = response_json['msg']
        if "成功" in msg:
            coin_val = response_json['data']['species']
            Text(f'看视频领金币>>>{coin_val}币')
        else:
            Text(f'看视频领金币>>>{msg}')


def video15():
        url = 'https://speciesweb.whjzjx.cn/v1/sign/escalation'
        data = {
            "type": 2
        }
        response = requests.post(url, headers=headers, json=data)
        Text(response.text)
        msg = response.json()['msg']
        if "签到过" in msg:
            Text("每日看剧15分钟>>>完成过了")
        elif "成功" in msg:
            Text("每日看剧15分钟>>>成功")
            url2 = 'https://speciesweb.whjzjx.cn/v1/sign'
            data2 = {
                "type": 2,
                "make": 3
            }
            response = requests.post(url2, headers=headers, json=data2)
            Text(response.text)
            response_json = response.json()
            msg = response_json['msg']
            species = response_json['species']
            if "成功" in msg:
                Text(f"领取成功>>>{species}币")
            else:
                Text(f"领取失败>>>{msg}")


def video180():
        url = 'https://speciesweb.whjzjx.cn/v1/sign/escalation'
        data = {
            "type": 3
        }
        response = requests.post(url, headers=headers, json=data)
        Text(response.text)
        msg = response.json()['msg']
        if "完成" and "超出" in msg:
            Text("每日看剧>>>任务已完成")
        elif "成功" in msg:
            Text("每日看剧>>>完成任务")
            randomtime()
        url = "https://speciesweb.whjzjx.cn/v1/sign/sign_multi_stage"
        data = {
            "type": 3,
            "makes": [1, 2, 3, 4],
            "device_id": "3818F866-06F5-4902-9658-6819540D50E3"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if "上限" in response.text:
            Text("领取看短剧>>>领取过了")
        elif "成功" in response.text:
            coin_value = response.json()['coin_value']
            Text(f"领取看短剧>>>{coin_value}币")
            randomtime()
            url = "https://speciesweb.whjzjx.cn/v1/sign/view_ad"
            data = {
                "coin_val": coin_value
            }
            # 发送POST请求
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response_json = response.json()
            coin_val = response_json['data']['coin_val']
            Text(f"激励视频奖励>>>{coin_val}币")


def draw():  # 抽奖
        url = "https://speciesweb.whjzjx.cn/v1/coin-match/lottery?device_id=2011181552b3632dabb4ff7eac5f62ead&is_login=2"
        response = requests.get(url, headers)
        Text(response.text)
        list_json = response.json()['data']['prize_list']
        url = "https://speciesweb.whjzjx.cn/v1/coin-match/lottery"
        response = requests.post(url, headers=headers)
        if "已完成" in response.text:
            Text("抽奖>>>今日已完成")
        else:
            type = response.json()['data']['type']
            # 遍历JSON列表
            for item in list_json:
                if item['type'] == type:
                    Text("抽奖>>>", item['name'])
                    break


st = middleware.bucketGet("sm_gaia_userData_QB", userID)
stj = json.load(st)
if st == None:
    Text('该账号没有注册，请先充值或使用卡密')
elif stj['balance'] == 0:
    Text('该账号积分为0，请先充值或使用卡密！')
else:
    Text(f"本次运行扣除10积分，剩余积分{stj['balance']}")
    balance = int(stj['balance']) - 10
    Text(f"剩余积分{balance}")
    now = time.localtime()
    time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    data = {"balance": balance, "isBlacklist": false, "registrationTime": time}
    data=json.dumps(data)
    middleware.bucketSet("sm_gaia_userData_QB", userID, data)

XingYa = middleware.bucketGet('XingYa', userID)
if XingYa is None:
    Text("未找到环境变量XingYa")
elif "&" not in XingYa:
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Authorization": XingYa,
    }
    openbox()
    videocoin()
    video15()
    video180()
    draw()
else:
    XingYas = XingYa.split('&')
    Text(f"共{len(XingYas)}个账号\n")
    for i, XingYa in enumerate(XingYas):
        Text(f'正在执行第{i + 1}个帐号')
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Authorization": XingYa,
        }
        openbox()
        videocoin()
        video15()
        video180()
        draw()
    randomtime()

