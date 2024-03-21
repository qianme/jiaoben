# Author: lindaye
# Update:2023-11-26
# 文博大会答题
# 活动入口：TG内部群
# 添加账号说明(青龙/本地)二选一
#   青龙: 青龙变量wbtoken 值{"ck":"xxxxtokenxxxx","uuid":"xxx","sign":"xxx"} 一行一个(回车分割)
#   本地: 脚本内置ck方法ck_token = [{"ck":"xxxxtokenxxxx","uuid":"xxx","sign":"xxx"},{"ck":"xxxxtokenxxxx","uuid":"xxx","sign":"xxx"}]
# 软件版本
version ="0.0.1"#line:1
name ="文博大会答题"#line:2
linxi_token ="wbtoken"#line:3
linxi_tips ='{"ck":"xxxxtokenxxxx","uuid":"xxx","sign":"xxx"}'#line:4
import requests #line:5
import json #line:6
import os #line:7
import re #line:8
import time #line:9
from random import randint ,choice #line:10
from multiprocessing import Pool #line:11
Btype ="青龙"#line:14
domain ='https://wbdh.jiiimo.cn/api'#line:16
turl ="http://wbdt.lieren.link"#line:17
ss =requests .session ()#line:19
headers ={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.39 (0x18002733) NetType/WIFI Language/zh_CN','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}#line:23
def user_info (i ,ck_token ):#line:25
    headers ['token']=ck_token ['ck']#line:26
    res =ss .post (domain +"/user/info",headers =headers ,data ={"uuid":ck_token ['uuid'],"sign":ck_token ['sign']}).json ()#line:27
    if res ['code']==0 :#line:28
        print (f"账号【{i+1}】用户:{res['data']['nickname']} 余额:{res['data']['balance']}元 积分:{res['data']['point']} 签到:{res['data']['days']}天")#line:29
    else :#line:30
        print (f"账号【{i+1}】请检查你的CK是否正确!")#line:31
def do_read (i ,ck_token ):#line:35
    headers ['token']=ck_token ['ck']#line:36
    res =ss .post (domain +"/home/checkin",headers =headers ,data ={"uuid":ck_token ['uuid'],"sign":ck_token ['sign']}).json ()#line:37
    if res ['code']==0 :#line:38
        print (f"账号【{i+1}】今日签到: {res}")#line:39
    else :#line:40
        print (f"账号【{i+1}】今日签到: {res['msg']}")#line:41
    res =ss .post (domain +"/home/question",headers =headers ,data ={"uuid":ck_token ['uuid'],"sign":ck_token ['sign']}).json ()#line:42
    if res ['code']==0 :#line:43
        id =res ['data']['id']#line:44
        mid =res ['data']['mid']#line:45
        while True :#line:46
            res =ss .post (domain +"/question/get",headers =headers ,data ={"qid":id ,"mid":mid ,"uuid":ck_token ['uuid'],"sign":ck_token ['sign']}).json ()#line:47
            id =""#line:48
            if res ['code']==0 :#line:49
                title =res ['data']['title']#line:50
                options =res ['data']['options']#line:51
                print (f"账号【{i+1}】获取题目成功[{res['data']['number']}/{res['data']['totalNumber']}]: 题目:{title}\n答案:{options}")#line:52
                id =res ['data']['id']#line:53
                wyy =res ['data']['wyy']#line:54
                wyy_point =res ['data']['wyy_point']#line:55
                option =["A","B","C"]#line:56
                answer =search (title ,options )#line:57
                if answer ==4 :#line:58
                    why =choice (option )#line:59
                else :#line:60
                    why =option [answer ]#line:61
                res =ss .post (domain +"/question/post",headers =headers ,data ={"id":id ,"select":why ,"wyy":wyy ,"wyy_point":wyy_point ,"uuid":ck_token ['uuid'],"sign":ck_token ['sign']}).json ()#line:62
                if res ['code']==0 :#line:63
                    if answer ==4 :#line:64
                        upload (title ,options [why ],False )#line:65
                    if why ==list (res ['data']['answer'].keys ())[0 ]:#line:66
                        print (f"账号【{i+1}】回答正确,答案为: {options[why]}")#line:67
                    else :#line:68
                        print (f"账号【{i+1}】回答错误,答案为: {options[why]}")#line:69
                        if answer !=4 :#line:70
                            upload (title ,options [why ],True )#line:71
                    time .sleep (2 )#line:72
                else :#line:73
                    print (f"账号【{i+1}】回答异常: {res}")#line:74
                    break #line:75
            else :#line:76
                print (f"账号【{i+1}】获取题目失败: {res['msg']}")#line:77
                break #line:78
    else :#line:79
        print (f"账号【{i+1}】获取首页题目失败: {res}")#line:80
def search (question ,title ):#line:82
    for i in range (4 ):#line:83
        try :#line:84
            res =ss .get (turl +"/search?question="+question ).json ()#line:85
            if res ["status"]=='200':#line:86
                try :#line:87
                    return title .index (res ["content"])#line:88
                except :#line:89
                    return randint (0 ,2 )#line:90
            else :#line:91
                return 4 #line:92
        except :#line:93
            print (f"[题库服务器异常]: 搜索题目失败，即将自动尝试当前{i+1}次!")#line:94
            time .sleep (1 )#line:95
    return 4 #line:96
def upload (question ,answer ,update ):#line:98
    for i in range (4 ):#line:99
        try :#line:100
            if update :#line:101
                res =ss .get (turl +"/upload?question="+question +f"&answer={answer}&update={update}").json ()#line:102
                print (f"上传题库服务器(更新答案):{res['msg']}")#line:103
            else :#line:104
                res =ss .get (turl +"/upload?question="+question +f"&answer={answer}").json ()#line:105
                print (f"上传题库服务器(新增题目):{res['msg']}")#line:106
            return True #line:107
        except :#line:108
            print (f"[上传题库服务器异常]: 上传题目或题目更新失败，即将自动尝试当前{i+1}次!")#line:109
            time .sleep (1 )#line:110
    return False #line:111
if __name__ =="__main__":#line:113
    if Btype =="青龙":#line:123
        if os .getenv (nxfl_token )==None :#line:124
            print (f'青龙变量异常: 请添加{nxfl_token}变量示例:{nxfl_tips} 确保一行一个')#line:125
            exit ()#line:126
        ck_token =[json .loads (OO00O0OOOOO000O00 )if "&"in O00OOOOOO00O0OO0O else json .loads (O00OOOOOO00O0OO0O )for O00OOOOOO00O0OO0O in os .getenv (linxi_token ).splitlines ()for OO00O0OOOOO000O00 in re .findall (r'{.*?}',O00OOOOOO00O0OO0O )]#line:129
    else :#line:130
        ck_token =[]#line:134
        if ck_token ==[]:#line:135
            print (f'本地变量异常: 请添加本地ck_token示例:{linxi_tips}')#line:136
    with Pool ()as pool :#line:139
        print ("==================获取账号信息=================")#line:141
        pool .starmap (user_info ,list (enumerate (ck_token )))#line:142
        print ("==================开始执行任务=================")#line:143
        pool .starmap (do_read ,list (enumerate (ck_token )))#line:144
        print ("==================获取账号信息=================")#line:145
        pool .starmap (user_info ,list (enumerate (ck_token )))#line:146
        pool .close ()#line:150
        pool .join ()#line:152
        ss .close #line:155
        print (f"================[{name}V{version}]===============")