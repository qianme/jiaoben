import requests
import json
import time
import random
from datetime import datetime
import hashlib


# ---------------------------格式化时间
def get_current_time():
    """获取当前的日期和时间并格式化输出"""
    # 创建一个datetime对象
    now = datetime.now()
    # 格式化日期和时间
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


# ----------------------------提交关卡
def Submit_the_level(tjguanqia, token, oaid, headers):
    url_user_five = 'https://duoduohezi.hnweir.com/home/Game/saveGame'  # 提交关卡#
    data_game_five = f'token={token}&level={tjguanqia}&num=100&status=1'
    response_game_four = requests.post(url_user_five, headers=headers, data=data_game_five.encode('utf-8'))
    # 解析JSON响应 for user_info
    user_data = response_game_four.json()
    print(user_data)


# ----------------------------查询关卡
def Query_the_level(token, oaid, headers):
    url_user_four = 'http://duoduohezi.hnweir.com/home/User/userInfo'  # 查询关卡#
    # 发送POST请求 for game_notify
    data_game_four = f'token={token}&oaid={oaid}'

    response_game_four = requests.post(url_user_four, headers=headers, data=data_game_four.encode('utf-8'))
    # 解析JSON响应 for user_info
    user_data = response_game_four.json()

    # 提取关卡
    guanqia = user_data.get('data', {}).get('guanqia', '未知用户')
    tjguanqia = guanqia + 1
    print(f'{get_current_time()}  当前关卡 : {tjguanqia}')
    return tjguanqia


# ----------------------------余额
def balance(token, oaid, headers):
    url_user_Third = 'https://duoduohezi.hnweir.com/home/Game/tixianBili'  # 查询余额
    data_user_info = f'token={token}'
    response_user_Third = requests.post(url_user_Third, headers=headers, data=data_user_info.encode('utf-8'))
    # 解析JSON响应 for user_info
    user_data1 = response_user_Third.json()
    # 提取余额
    money1 = user_data1.get('data', {}).get('money', '未知余额')
    print(f'{get_current_time()}  当前余额 {money1} 元')
    return money1


# ----------------------------10位时间戳
def get_10_digit_timestamp():
    # 获取当前时间
    now = datetime.now()
    # 将时间转换为时间戳
    timestamp = int(now.timestamp())
    # 返回10位时间戳
    return timestamp


# ---------------------------提现
def withdraw_cash(token, oaid, headers, id):
    url_user_tixian = 'http://duoduohezi.hnweir.com/home/Game/withdrawal'  # 提现
    if id == 1:
        print(f'{get_current_time()}  余额大于0.5，执行提现程序。')
        print(f'{get_current_time()}  提现0.5元')
    if id == 2:
        print(f'{get_current_time()}  余额大于1，执行提现程序。')
        print(f'{get_current_time()}  提现1元')
    # 定义请求的数据 for user_info
    data_user_info = f'token={token}&type=1&zfb=null&zfbname=null&id={id}'
    # 发送POST请求 for user_info
    response_user_info = requests.post(url_user_tixian, headers=headers, data=data_user_info.encode('utf-8'))
    print(response_user_info.json())


# ----------------------------奖励
def reward(token, oaid, uuid, locationAddress):
    rdm = random.randint(1, 9)
    rdmec = random.randint(1, 6) * 10000
    timestamp = get_10_digit_timestamp()
    text = f"advertType=gdt&ecpm={rdmec}&locationAddress={locationAddress}&oaid={oaid}&timestamp={timestamp}&uuid=" + uuid + "&key=abc*#123"
    data_game_notify = f'token={token}&ccc={rdm}dW5kZWZpbmVk{rdm}&ecpm={rdmec}.0&oaid={oaid}&advertType=pangle&locationAddress={locationAddress}&sign={calculate_md5(text)}&timestamp={timestamp}&uuid={uuid}'
    url_game_notify = 'https://duoduohezi.hnweir.com/home/Game/videoNotify'  # 奖励
    # 发送POST请求 for game_notify
    response_game_notify = requests.post(url_game_notify, headers=headers, data=data_game_notify.encode('utf-8'))
    print(response_game_notify.json())


# ----------------------------md5
def calculate_md5(input_string):
    """计算输入字符串的MD5值并返回"""
    # 创建一个md5对象
    md5_obj = hashlib.md5()
    # 对字符串进行编码，因为hashlib.md5期望的是字节字符串
    md5_obj.update(input_string.encode('utf-8'))
    # 返回MD5值
    return md5_obj.hexdigest()


# ----------------------------查询
def Inquire(token, oaid):
    url_user_info = 'https://duoduohezi.hnweir.com/home/User/userInfo'  # 查询信息
    # 定义请求的头部信息
    headers = {
        'Host': 'duoduohezi.hnweir.com',
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '38'
    }
    # 定义请求的数据 for user_info
    data_user_info = f'token={token}'
    # 发送POST请求 for user_info
    response_user_info = requests.post(url_user_info, headers=headers, data=data_user_info.encode('utf-8'))
    # print(response_user_info.json())

    Code = response_user_info.json().get("code")  # 状态码
    if Code == 200:
        name = response_user_info.json().get("data").get("nickname")  # 名称
        return Code, name
    else:
        print(response_user_info.json().get("msg"))
        return Code, response_user_info.json().get("msg")


# ---------------随机字母
def generate_random_uuid_like_string():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    uuid_like_string = []

    for i in range(36):
        if i == 8 or i == 13 or i == 18 or i == 23:
            uuid_like_string.append('-')
        else:
            uuid_like_string.append(random.choice(chars))

    return ''.join(uuid_like_string)


# ------------------------------参数-----------------------------------#
headers = {
    'Host': 'duoduohezi.hnweir.com',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '38'
}
token = ''  # 请确保这里有有效的值
oaid = ''  # 请确保这里有有效的值
locationAddress = ""#例如湖北省武汉市
# ----------------------------程序-------------------------------------#
Code, name = Inquire(token, oaid)
if Code == 200:
    print(f'{get_current_time()}  登录成功')
    print(f'{get_current_time()}  用户名 ： {name}')
    for i in range(10):
        money1 = balance(token, oaid, headers)  # 余额
        if money1 >= 0.51:
            id = 1
            withdraw_cash(token, oaid, headers, id)  # 提现
            break
        if money1 >= 1.01:
            id = 2
            withdraw_cash(token, oaid, headers, id)  # 提现
            break
        else:
            tjguanqia = Query_the_level(token, oaid, headers)  # 查询关卡
            te = random.uniform(10, 15)
            print(f'{get_current_time()}  延迟{te :.2f}秒')
            time.sleep(te)
            # Submit_the_level(tjguanqia,token,oaid,headers)#提交关卡
            uuid = generate_random_uuid_like_string()
            te = random.uniform(80, 95)
            print(f'{get_current_time()}  延迟{te :.2f}秒')
            time.sleep(te)
            reward(token, oaid, uuid, locationAddress)  # 奖励


else:
    print(name)

# ------------------------------结束------------------------------------#