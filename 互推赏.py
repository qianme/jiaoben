import os
import random
import requests
import time
import hashlib
import random
import json
import datetime

# 获取环境变量中的账号和密码
accounts_env = os.getenv('hts')

# 检查环境变量是否已设置
if accounts_env:
    # 使用换行符分割账号密码对
    accounts_list = accounts_env.strip().split('\n')
    
    # 遍历每个账号密码对
    for account_info in accounts_list:
        # 使用 '#' 分割账号和密码
        account, password = account_info.split('#')
        # 打印或处理账号和密码
        print(f"账号: {account}, 密码: {password}")

        #程序
        # 生成随机字符串
        随机值 = "vbmqnqe5hfl4" + str(random.randint(12345, 98765)) + "aluoiqgmf5f9kah"
        # 设置请求头
        headers = {
            "Host": "vip.hutuishang.com",
            "Referer": "https://vip.hutuishang.com/user/account",
            "Cookie": f"NiuToken={随机值}; popUid=241448"
            }
        # 发送GET请求以获取登录页面
        response = requests.get("http://vip.hutuishang.com/cas/login", headers=headers)
        # 提取CSRF令牌
        _csrf_token = response.text.split('value="')[1].split('"')[0]
        # 设置POST请求的数据
        data = {
           "_csrf_token": _csrf_token,
           "_target_path": "",
           "_username": account,
           "_password": password
           }
        # 发送POST请求以登录
        response = requests.post("https://vip.hutuishang.com/cas/login?_random=1698600311802", data=data, headers=headers)
        # 检查是否登录成功
        if response.status_code == 200:
            # 提取用户名
            用户名 = response.text.split('<div class="name">')[1].split('<')[0]
            print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}   {用户名}')
            # 提取USER_REMEMBER_ME cookie
            USER_REMEMBER_ME = response.headers['Set-Cookie'].split("USER_REMEMBER_ME=")[1].split(";")[0]
            # 更新请求头
            headers = {
              "Host": "vip.hutuishang.com",
              "Cookie": f"popUid=241448; NiuToken={随机值}; USER_REMEMBER_ME={USER_REMEMBER_ME}"
              }
            # 检查是否已签到
            response = requests.get("https://vip.hutuishang.com/user/active/daily_sign", headers=headers)
            # 检查是否包含所需的字符串
            if 'csrfToken' in response.text:
                csrf_token = response.text.split('csrfToken ="')[1].split('"')[0]
                print(csrf_token)

                # 签到
                response = requests.post("https://vip.hutuishang.com/user/active/daily_sign/sign?_random=1698600393006",
                                 data={"csrfToken": csrf_token},
                                 headers=headers)
                result = response.json()
                print(result)

                sign_days = result['data']['signCount']  # 签到天数
                reward = result['data']['grantMoney']    # 奖励金额
                print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  账号已签到{sign_days}天 | 获取{reward / 10000}元')
            else:
                print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  今日已签到')
            ck=f"popUid=241448; NiuToken={随机值}; USER_REMEMBER_ME={USER_REMEMBER_ME}"
            for i in range(4):
                # 发送GET请求
                response = requests.get("https://vip.hutuishang.com/pangle_video/launch?_random=" + str(int(time.time() * 1000)) + "&type=slide", headers={
                      "Accept": "application/json, image/webp",
                      "User-Agent": "Mozilla/9.0 (Linux; Android 14; Redmi Note 9 Build/QKQ1.00174.02; wv) AppleWebKit/53.36 (KHTML, like Gecko) Version/4.0 Chrome/9.0.4103.101 Mobile Safari/537.3 HuoNiuFusion/7.24.0_699982",
                      "X-Requested-With": "XMLHttpRequest",
                      "Cookie": ck
                       })
                temp = response.json()
                if temp.get('code') == 0:
                    csrfToken = temp['data']['extArgs']['csrfToken']
                    随机 = random.randint(1234, 9876)
                    deviceId = f"{随机}6b3df18b{随机}"
                    算法 = f"{csrfToken}#{deviceId}#{int(time.time())}"  # 假设这里使用的是北京时间戳
                    # 计算SHA-1
                    sha1 = hashlib.sha1(算法.encode('utf-8')).hexdigest()
                    print("SHA1:", sha1)
        
                    # 构造请求头部
                    headers = {
                       "User-Agent": "Mozilla/7.0 (Linux; Android 10; Redmi Note 9 Build/QKQ1.200174.002; wv) AppleWebKit/538.36 (KHTML, like Gecko) Version/4.0 Chrome/8.0.4103.101 Mobile Safari/537.36 HuoNiuFusion/7.24.0_630982",
                       "Cookie": ck,
                     }
        
                    # 构造请求参数
                    data = {
                        "csrfToken": csrfToken,
                        "deviceId": deviceId,
                        "timestamp": int(time.time()),  # 使用当前UTC时间戳，如果需要北京时间，请加上8小时
                        "sign": sha1,
                       }
        
                    # 发送POST请求
                    response = requests.post("https://vip.hutuishang.com/pangle_video/award/grant?_t=1708360366", data=data, headers=headers)
        
                    # 解析响应
                    if response.status_code == 200:
                        temp = response.json()
                        if temp.get('code') == 0:
                            print(f"获得{temp.get('data', {}).get('awardMoney', 0)}元")
                            te= random.uniform(30, 45)
                            print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  延迟{te :.2f}秒')
                            time.sleep(te)
          
                        else:
                            print(temp.get('msg', '未知错误'))
                            break
                    else:
                        print(f"请求失败，状态码：{response.status_code}")
                else:
                    print("获取csrfToken失败，无法继续执行。")


            for i in range(4):
                # 发送GET请求
                response = requests.get("https://vip.hutuishang.com/kwai_video/launch?_random=" + str(int(time.time() * 1000)) + "&type=slide", headers={
                      "Accept": "application/json, image/webp",
                      "User-Agent": "Mozilla/9.0 (Linux; Android 14; Redmi Note 9 Build/QKQ1.00174.02; wv) AppleWebKit/53.36 (KHTML, like Gecko) Version/4.0 Chrome/9.0.4103.101 Mobile Safari/537.3 HuoNiuFusion/7.24.0_699982",
                      "X-Requested-With": "XMLHttpRequest",
                      "Cookie": ck
                       })
                temp = response.json()
                if temp.get('code') == 0:
                    csrfToken = temp['data']['extArgs']['csrfToken']
                    随机 = random.randint(1234, 9876)
                    deviceId = f"{随机}6b3df18b{随机}"
                    算法 = f"{csrfToken}#{deviceId}#{int(time.time())}"  # 假设这里使用的是北京时间戳
                    # 计算SHA-1
                    sha1 = hashlib.sha1(算法.encode('utf-8')).hexdigest()
                    print("SHA1:", sha1)
        
                    # 构造请求头部
                    headers = {
                       "User-Agent": "Mozilla/7.0 (Linux; Android 10; Redmi Note 9 Build/QKQ1.200174.002; wv) AppleWebKit/538.36 (KHTML, like Gecko) Version/4.0 Chrome/8.0.4103.101 Mobile Safari/537.36 HuoNiuFusion/7.24.0_630982",
                       "Cookie": ck,
                     }
        
                    # 构造请求参数
                    data = {
                        "csrfToken": csrfToken,
                        "deviceId": deviceId,
                        "timestamp": int(time.time()),  # 使用当前UTC时间戳，如果需要北京时间，请加上8小时
                        "sign": sha1,
                       }
        
                    # 发送POST请求
                    response = requests.post("https://vip.hutuishang.com/kwai_video/award/grant?_t=1708360366", data=data, headers=headers)
        
                    # 解析响应
                    if response.status_code == 200:
                        temp = response.json()
                        if temp.get('code') == 0:
                            print(f"获得{temp.get('data', {}).get('awardMoney', 0)}元")
                            te= random.uniform(30, 45)
                            print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  延迟{te :.2f}秒')
                            time.sleep(te)
          
                        else:
                            print(temp.get('msg', '未知错误'))
                            break
                    else:
                        print(f"请求失败，状态码：{response.status_code}")
                else:
                    print("获取csrfToken失败，无法继续执行。")


        else:
            print("登录失败，状态码：", response.status_code)    



else:
    print("环境变量 'hts' 未设置或为空")