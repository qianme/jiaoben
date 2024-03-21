import requests
import sys
import json

def printf(message):
    print(message, "(line:", sys._getframe().f_lineno, ")")

# 本地服务的请求，返回请求的数据
def get_local_service_response(path:str,data):
    url = "http://localhost:8080/otto"+path
    response = requests.post(
        url=url, 
        json=data,
        headers={"Content-Type":"application/json"},
    )
    printf("网络请求响应"+response.text)
    if response.status_code==200:
        # 将json字符串转换为json对象
        json_obj=json.loads(response.text)
        return json_obj
    else:
        raise Exception("请求失败")

# 获取发送者ID,整型
def getSenderID():
    return sys.argv[1]

# 推送消息
def push(imType,groupCode,userID,title,content):
    path="/push"
    data={
        "imType":imType,
        "groupCode":groupCode,
        "userID":userID,
        "title":title,
        "content":content
    }
    get_local_service_response(path,data)

# 获取机器人名称
def name():
    path="/name"
    data={}
    response=get_local_service_response(path,data)
    return response["data"]

# 获取机器id
def machineId():
    path="/machineId"
    data={}
    response=get_local_service_response(path,data)
    return response["data"]

# 获取autMan版本
def version():
    path="/version"
    data={}
    response=get_local_service_response(path,data)
    return response["data"]

# 获取数据库数据
def get(key):
    path="/get"
    data={
        "key":key
    }
    response=get_local_service_response(path,data)
    return response["data"]

# 设置数据库数据
def set(key,value):
    path="/set"
    data={
        "key":key,
        "value":value,
    }
    response=get_local_service_response(path,data)
    return response["code"]==200


# 删除数据库数据
def delete(key):
    path="/delete"
    data={
        "key":key
    }
    response=get_local_service_response(path,data)
    return response["code"]==200

# 获取指定数据库指定key的值
def bucketGet(bucket,key):
    path="/bucketGet"
    data={
        "bucket":bucket,
        "key":key
    }
    response=get_local_service_response(path,data)
    return response["data"]

# 设置指定数据库指定key的值
def bucketSet(bucket,key,value):
    path="/bucketSet"
    data={
        "bucket":bucket,
        "key":key,
        "value":value
    }
    response=get_local_service_response(path,data)
    return response["code"]==200

# 删除指定数据库指定key的值
def bucketDel(bucket,key):
    path="/bucketDel"
    data={
        "bucket":bucket,
        "key":key
    }
    response=get_local_service_response(path,data)
    return response["code"]==200

# 获取指定数据库的所有值为value的keys
def bucketKeys(bucket,value):
    path="/bucketKeys"
    data={
        "bucket":bucket,
        "value":value
    }
    response=get_local_service_response(path,data)
    # 使用逗号分隔字符串
    return response["data"]

# 获取指定数据库的所有的key集合
def bucketAllKeys(bucket):
    path="/bucketAllKeys"
    data={
        "bucket":bucket
    }
    response=get_local_service_response(path,data)
    # 使用逗号分隔字符串
    return response["data"]

# 通知管理员
def notifyMasters(content,imtypes:list=[]):
    path="/notifyMasters"
    data={
        "content":content,
        "imtypes":imtypes,
    }
    response=get_local_service_response(path,data)
    return response["code"]==200

# 当前系统咖啡码激活状态
def coffee():
    path="/coffee"
    data={}
    response=get_local_service_response(path,data)
    return response["code"]==200

# 京东、淘宝、拼多多转链推广
def spread(msg):
    path="/spread"
    data={
        "msg":msg
    }
    response=get_local_service_response(path,data)
    return response["data"]

class Sender:
    # 类的构造函数
    def __init__(self, senderID:int):
        self.senderID = senderID

    # 获取发送者路由
    def getRouterPath(self):
        path="/getRouterPath"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取路由参数
    def getRouterParams(self):
        path="/getRouterParams"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 获取路由方法
    def getRouterMethod(self):
        path="/getRouterMethod"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取路由请求头
    def getRouterHeaders(self):
        path="/getRouterHeaders"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取路由cookies
    def getRouterCookies(self):
        path="/getRouterCookies"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取请求体
    def getRouterBody(self):
        path="/getRouterBody"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 获取发送者渠道
    def getImtype(self):
        path="/getImtype"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取发送者ID
    def getUserID(self):
        path="/getUserID"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        # 去掉字符串两端的引号
        return response["data"]
    
    # 获取发送者昵称
    def getUserName(self):
        path="/getUserName"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 获取发送者头像
    def getUserAvatarUrl(self):
        path="/getUserAvatarUrl"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 获取发送者群号，返回值是整型
    def getChatID(self):
        path="/getChatID"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取发送者群名称
    def getChatName(self):
        path="/getChatName"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 是否管理员
    def isAdmin(self):
        path="/isAdmin"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取消息
    def getMessage(self):
        path="/getMessage"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取消息ID
    def getMessageID(self):
        path="/getMessageID"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 撤回消息
    def recallMessage(self,messageid):
        path="/recallMessage"
        data={
            "senderid":self.senderID,
            "messageid":messageid
        }
        get_local_service_response(path,data)

    # 模拟新消息输入，即将消息发送者的消息修改为新的内容，重新送往autMan内部处理
    def breakIn(self,content):
        path="/breakIn"
        data={
            "senderid":self.senderID,
            "content":content
        }
        get_local_service_response(path,data)
    
    # 获取匹配的文本参数
    def param(self,i):
        path="/param"
        data={
            "senderid":self.senderID,
            "index":i
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 回复文本消息，回复的发送消息的id，list类型
    def reply(self,text):
        path="/sendText"
        data={
            "senderid":self.senderID,
            "text":text,
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 回复图片消息
    def replyImage(self,imageUrl):
        path="/sendImage"
        data={
            "senderid":self.senderID,
            "imageurl":imageUrl
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 回复语音消息
    def replyVoice(self,voiceUrl):
        path="/sendVoice"
        data={
            "senderid":self.senderID,
            "voiceurl":voiceUrl
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 回复视频消息
    def replyVideo(self,videoUrl):
        path="/sendVideo"
        data={
            "senderid":self.senderID,
            "videourl":videoUrl
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 等待用户输入,timeout为超时时间，单位为毫秒,
    def listen(self,timeout:int):
        path="/listen"
        data={
            "senderid":self.senderID,
            "timeout":timeout
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 等待用户输入,timeout为超时时间，单位为毫秒,recallDuration为撤回用户输入的延迟时间，单位为毫秒，0是不撤回，forGroup为bool值true或false，是否接收群聊所有成员的输入
    def input(self,timeout:int,recallDuration:int,forGroup:bool):
        path="/input"
        data={
            "senderid":self.senderID,
            "timeout":timeout,
            "recallDuration":recallDuration,
            "forGroup":forGroup,
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 等待支付
    def waitPay(self,exitcode:str,timeout:int):
        path="/waitPay"
        data={
            "senderid":self.senderID,
            "exitcode":exitcode,
            "timeout":timeout # 超时时间，单位为毫秒
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 系统是否处于等待支付状态
    def atWaitPay(self):
        path="/atWaitPay"
        data={
            "senderid":self.senderID
        }
        response=get_local_service_response(path,data)
        return response["data"]

    # 添加好友至群聊
    def groupInviteIn(self,friend,group):
        path="/groupInviteIn"
        data={
            "senderid":self.senderID,
            "friend":friend,
            "group":group,
        }
        get_local_service_response(path,data)

    # 群聊踢人
    def groupKick(self,userid):
        path="/groupKick"
        data={
            "senderid":self.senderID,
            "userid":userid,
        }
        get_local_service_response(path,data)
    
    # 群聊禁言
    def groupBan(self,userid,timeout):
        path="/groupBan"
        data={
            "senderid":self.senderID,
            "userid":userid,
            "timeout":timeout,
        }
        get_local_service_response(path,data)
    
    # 群聊解除禁言
    def groupUnban(self,userid):
        path="/groupUnban"
        data={
            "senderid":self.senderID,
            "userid":userid,
        }
        get_local_service_response(path,data)
    
    # 群聊全员禁言
    def groupWholeBan(self):
        path="/groupWholeBan"
        data={
            "senderid":self.senderID,
        }
        get_local_service_response(path,data)
    
    # 群聊全员解禁
    def groupWholeUnban(self):
        path="/groupWholeUnban"
        data={
            "senderid":self.senderID,
        }
        get_local_service_response(path,data)
    
    # 群聊内发送公告
    def groupNoticeSend(self,notice):
        path="/groupNoticeSend"
        data={
            "senderid":self.senderID,
            "notice":notice,
        }
        get_local_service_response(path,data)

    # 获取当前处理流程的插件名
    def getPluginName(self):
        path="/getPluginName"
        data={
            "senderid":self.senderID,
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取当前处理流程的插件版本
    def getPluginVersion(self):
        path="/getPluginVersion"
        data={
            "senderid":self.senderID,
        }
        response=get_local_service_response(path,data)
        return response["data"]

# 定时指令的相关操作
class Cron:

    # 构造函数
    def __init__(self, cronID:int):
        self.cronID = cronID

    # 获取定时指令集合（json格式字符串）
    def getCrons(self):
        path="/croncmdsGet"
        data={}
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 获取某个定时指令的详细信息（json格式字符串）
    def getCronByID(self,id:int):
        path="/croncmdsGet"
        data={
            "id":id
        }
        response=get_local_service_response(path,data)
        return response["data"]
    
    # 添加定时，返回定时指令的ID
    def addCron(self,cron:str,cmd:str,isToSelf:bool,toOthers:str,memo:str):
        path="/croncmdsAdd"
        data={
            "cron":cron,
            "cmd":cmd,
            "isToSelf":isToSelf,
            "toOthers":toOthers,
            "memo":memo,
        }
        response=get_local_service_response(path,data)
        return response["data"]
    # 修改定时，返回ok或error
    def updateCron(self,id:int,cron:str,cmd:str,isToSelf:bool,toOthers:str,memo:str):
        path="/croncmdsUpd"
        data={
            "id":id,
            "cron":cron,
            "cmd":cmd,
            "isToSelf":isToSelf,
            "toOthers":toOthers,
            "memo":memo,
        }
        response=get_local_service_response(path,data)
        return response["data"]
    # 删除定时，返回ok或error
    def deleteCron(self,id:int):
        path="/croncmdsDel"
        data={
            "id":id
        }
        response=get_local_service_response(path,data)
        return response["data"]