import requests
import time
import os
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import threading




#变量名 wbdh 变量值 uuid--sign


max_concurrency = 3  #线程数，请根据线程数需要更改,默认线程数位：3


#请勿更改
demo = 'http://wbdh.jiiimo.cn/api/'
headers ={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.39 (0x18002733) NetType/WIFI Language/zh_CN','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
ss = requests.session()

def user_info(cks,i):
    ck = cks.split("--")
    data ={"uuid":ck [0],"sign":ck [1]}
    # headers ['token']=ck_token ['ck']
    # print(data)
    res =ss .post (f"{demo}user/info",headers =headers,data=data).json()
    if res ['code']==0 :
        print (f"账号【{i}】用户:{res['data']['nickname']} 余额:{res['data']['balance']}元 积分:{res['data']['point']} 签到:{res['data']['days']}天")
        number(cks,i,res['data']['nickname'])
    else :#line:30
        print (f"账号【{i}】请检查你的CK是否正确!")

def question(cks,i,number,name):
    ck = cks.split("--")
    #签到
    qd =ss .post (f"{demo}home/checkin",headers =headers,data={"uuid":ck [0],"sign":ck [1]}).json()
    if qd ['code']==0 :
        print (f"账号【{i}】今日签到: {qd}")
    else :
        print (f"账号【{i}】今日签到: {qd['msg']}")
    #获取mid
    res=ss .post (f"{demo}home/question",headers =headers,data={"uuid":ck [0],"sign":ck [1]}).json()
    if res ['code']==0 :
        id = res['data']['id']
        mid = res['data']['mid']
        tm(cks,i,number,name,mid,id)
    else:
        print (f"账号【{i}】获取首页题目失败: {res}")

def tm(cks,i,number,name,mid,id):
    ck = cks.split("--")
    #mids=12
    while number<21:
        #获取题目
        tm=ss .post (f"{demo}question/get",headers =headers,data ={"mid":mid,"id":id,"uuid":ck [0],"sign":ck [1]}).json()
        # print(tm)
        id = ""
        if tm ['code']==0 :
            title =tm ['data']['title']
            options =tm ['data']['options']
            print (f"账号【{i}】获取题目成功[{tm['data']['number']}/{tm['data']['totalNumber']}]: 题目:{title}\n答案:{options}")#
            id =tm ['data']['id']
            wyy =tm ['data']['wyy']
            wyy_point =tm ['data']['wyy_point']
            option =["A","B","C"]
            #请求题库
            tk=requests.get(f"http://tk.562455.xyz/answer?question={id}").json()
            #print(tk)
            if tk["code"] == 200:
                selcet = tk['data'][0]
                # print(selcet)
                #答题
                dt=ss .post (f"{demo}question/post",headers =headers,data ={"id":id ,"select":selcet ,"wyy":wyy ,"wyy_point":wyy_point ,"uuid":ck [0],"sign":ck [1]}).json()
                # print(dt)
                if dt ['code']==0:
                    key = list(dt['data']['answer'].keys())[0]
                    # print(key)
                    if selcet == key:
                        print (f"账号【{i}】回答正确,答案为: {key}")
                        print(t)
                        if tm['data']['number'] == tm['data']['totalNumber']:
                            print("本轮已结束")
                            if mid<22:
                                print(">"*15 + "开始抽奖" + "<"*15)
                                lottery(cks,i,name,mid)
                                print(">"*15 + "抽奖完成，2秒后进行下一轮" + "<"*15)
                                time.sleep(2)
                                question(cks,i,number,name)
                            
                            number -=1
                    else:
                        print (f"账号【{i}】回答错误,答案为: {key}")
                        print("稍后上传正确答案至题库！！！！")
                        print(upload(id,key))
                elif dt['code'] == 1:
                    return dt['msg']
                print(">"*15 + "等待两秒进行下一题" + "<"*15)
                time.sleep(2)
            else:
                print("抱歉题库不存在该题答案！")
                print("准备上传该题库")
                print(upload(id,key))
                time.sleep(2)
        elif tm["code"]==1 :
            return tm["msg"]
        else:
            print (f"账号【{i}】获取题目失败: {res['msg']}")
            break
#else:
        #print (f"账号【{i}】获取首页题目失败: {res}")

def number(cks,i,name):
    ck = cks.split("--")
    res =ss .post (f"{demo}user/rule",headers =headers,data={"uuid":ck [0],"sign":ck [1]}).json()
    number = res['data']['number']
    print(f"账号【{i}】剩余{number}次，{res['data']['residualTime']}后刷新")
    if number==0:
        print(f"次数已用尽，请等待{res['data']['residualTime']}后刷新")
        return number
    print(question(cks,i,number,name))
    return number
    

def upload(id,key):
    data={"question":id,
    "answer":key}
    url="http://tk.562455.xyz/upload"
    headers ={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    res=requests.post(url=url,json=data).text
    return f"题目ID{id}{res}"

def lottery(cks,i,name,mid):
    ck = cks.split("--")
    res=requests.post(f"{demo}prize/get",headers=headers,data={"mid":mid,"uuid":ck[0],"sign":ck[1]}).json()
    if res["code"]==0:
        if res["data"]["type"]==2:
            print(f"账号【{i}】用户:{name}获得积分{res['data']['money']}")
            return
        else:
            print(f"账号【{i}】用户:{name}获得现金{res['data']['money']}")
            return
    else:
        print(f"账号【{i}】用户:{name}{res['msg']}")
    return

if __name__=="__main__":
    wbdh = os.environ["wbdh"]
    wbdhs=wbdh.split('&') 
    print(f"获取到{len(wbdhs)}个账号")
    with Pool(processes=len(wbdhs)) as pool:
            thread_pool = ThreadPool(max_concurrency)
            thread_pool.starmap(user_info, [(wbdh,i) for i, wbdh in enumerate(wbdhs, start=1)])