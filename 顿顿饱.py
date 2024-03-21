# [title: 顿顿饱]
# [language: python]
# [price: 0] 优先级，数字越大表示优先级越高
# [service: 10086] 售后联系方式
# [disable:true] 禁用开关，true表示禁用，false表示可用
# [admin: true] 是否为管理员指令
# [rule: 饱] 匹配规则，多个规则时向下依次写多个
# [cron: 0 0 0 0 0] cron定时，支持5位域和6位域
# [priority: 0] 优先级，数字越大表示优先级越高
# [platform: qq,qb,wx,tb,tg,web,wxmp] 适用的平台
# [open_source: true]是否开源
# [icon: 图标url]图标链接地址，请使用48像素的正方形图标，支持http和https
# [version: 1.0.0]版本号
# [public: true] 是否发布？值为true或false，不设置则上传aut云时会自动设置为true，false时上传后不显示在市场中，但是搜索能搜索到，方便开发者测试
# [price: 0.01] 上架价格
# [description: 关于插件的描述] 使用方法尽量写具体
import middleware
import json
import requests

senderID = middleware.getSenderID()
sender = middleware.Sender(senderID)
userID = sender.getUserID()

# 以下代码用于适配
call = lambda param: {
    'version': lambda: {"sn": "9.9.9"},
    'machineId': lambda: "xxxxxx",
    'md5': md5,
    'uuid': genUuid
}[param]

if 'shipei' not in globals():
    def timeFmt(layout):
        if not layout:
            return ""
        layout = layout \
            .replace('yyyy', '2006') \
            .replace('MM', '01') \
            .replace('dd', '02') \
            .replace('HH', '15') \
            .replace('mm', '04') \
            .replace('ss', '05')
        return time.now().format(layout)


    shipei = "666"
    isAdmin = sender.isAdmin
    GetChatID = sender.getChatID
    GetMessageID = sender.getMessageId
    GetContent = sender.getContent
    GetUsername = sender.getUsername
    getTitle = lambda: "顿顿饱内测"
    getVersion = lambda: "v1.0.4"
    GetUserID = sender.getUserId
    ImType = sender.getPlatform
    GetImType = sender.getPlatform
    param = sender.param
    # Continue = sender.continue
    sendText = sender.reply
    bucketKeys = lambda name: Bucket(name).keys()
    bucketGet = lambda name, key: Bucket(name)[key]
    bucketSet = lambda name, key, value: exec(f"Bucket('{name}')[{key}] = {value}")
    bucketDel = lambda name, key: exec(f"Bucket('{name}').__delitem__({key})")
    get = lambda key: Bucket("otto")[key]
    set = lambda key, value: exec(f"Bucket('otto')[{key}] = {value}")
    input = lambda timeout: sender.listen(timeout).getContent() if sender.listen(timeout) else None
    Debug = print
    Logger = lambda: {
        "Debug": print,
        "Info": print,
        "Warn": print,
        "Error": print,
    }
    sleep = time.sleep

    _request = request


    def request(params, handle=None):
        if not params.get('json') and not params.get('dataType'):
            params['dataType'] = "text"
        if params.get('url') == "http://autman.birdbls.cn/api/version":
            return {
                "success": True,
                "data": [{"ver": "v0.0.0"}],
            }
        resp = _request(params)
        if handle:
            handle("", resp, resp.headers, resp.body)
            return
        return resp.body


    def push(params):
        adapter, _ = GetAdapter(params["imType"], params.get("bot_id", ""))
        if adapter:
            for meta in [["UserID", "user_id"], ["groupCode", "chat_id"]]:
                if params.get(meta[0]):
                    params[meta[1]] = params[meta[0]]
                    params.pop(meta[0])
            adapter.push(params)


    def breakIn(content):
        adapter, _ = GetAdapter(sender.getPlatform(), "")
        if adapter:
            adapter.receive({
                "content": content,
                "chat_id": sender.getChatId(),
                "chat_id": sender.getUserId()
            })


    sendImage = lambda file: strings.buildCQCode("image", {"file": file})
    sendVideo = lambda file: strings.buildCQCode("video", {"file": file})
    sendVideoMsg = sendVideo
    sendShareLinkMsg = lambda to_wxid, title, content, image, url: strings.buildCQCode("share", {"title": title,
                                                                                                 "content": content,
                                                                                                 "image": image,
                                                                                                 "url": url})
    notifyMasters = lambda: None

let
elmCKOfType = 'sm_elm_' + GetImType().upper()
authorizationCode = bucketGet('sm_elm_config', 'authorizationCode')
machineId = call("machineId")()

checkJS = False
try:
    importJs("gaia_青龙.js")
except Exception as err:
    checkJS = True


def main():
    if checkJS:
        if isAdmin():
            sendText("未加载gaia_青龙.js，请前往云插件下载该插件")
        return

    content = GetContent()
    imType = GetImType()

    if authorizationCode == "":
        sendText("内测插件，仅供授权用户使用")
        return
    if authorizationCode != call("md5")(machineId + "46883409"):
        sendText("授权码错误，内测插件，仅供授权用户使用")
        return

    if bucketGet('sm_elm_config', 'ddb_ql') == "":
        sendText("你忘记配置插件了，请去云插件-》我的  配置插件")
        return
    if bucketGet('sm_elm_config', 'ddb_host') == "":
        sendText("你忘记配置插件了，请去云插件-》我的  配置插件")
        return

    if imType == "croncmd" and content == '饿了么检测':
        containerName = bucketGet('sm_elm_config', 'ddb_ql')
        body = gaia_getEnvs("elmck", containerName)
        if body.code != 200:
            notifyMasters("获取不了青龙的elm的cookie，检测cookie失败")
            return
        ckData = body.data
        for i in range(len(ckData)):
            ck = ckData[i].value
            id = ckData[i].id
            if not ifValid(ck):
                userId = getUserID(ck)
                qq = bucketGet('sm_elm_QQ', userId)
                wx = bucketGet('sm_elm_WX', userId)
                if qq:
                    pushOverdue("qq", qq, userId)
                if wx:
                    pushOverdue("wx", wx, userId)
                body = gaiz_disableEnvToQL(id, containerName)
        return

    if content and ("cookie2=" in content and "SID=" in content):
        userId = getUserID(content)
        if not userId:
            sendText("非法COOKIE,自动退出程序")
            return

        body = get_elm_userData(content)
        if body.message in ["未登录", "未知错误"]:
            sendText('无效COOKIE，自动退出程序')
            return
        phone = body.mobile

        bucketSet(elmCKOfType, userId, GetUserID())
        bucketSet('sm_elm_CKDB', userId, content)

        vipData = bucketGet('sm_elm_vip', userId)
        if not vipData or vipData < (time.time()):
            sendText(f'[{phone[:3]}XXXX{phone[7:]}]登记成功\n快发送【elm代挂】完善代挂服务')
            return

        if subCKToQL(content):
            sendText(f'[{phone[:3]}XXXX{phone[7:]}]更新成功\n距离授权过期还有 {getDaysFromTimestamp(vipData)}')
            return

        sendText("上传服务器失败，请稍后再试")
        return

    if content in ['服务器密钥', '服务器秘钥']:
        host = bucketGet('sm_elm_config', 'ddb_host')
        if host and isAdmin():
            sendText(getEncrypt(host, "46883409"))
        else:
            sendText("未设置域名或公网地址，设置地址：aut后台->云插件->我的->顿顿饱插件->配置->奥特曼公网地址")
        return

    if content == '饿了么授权' and isAdmin():
        sendText("请发送对应ck或者userId值")
        msg = input(60000)
        if msg == 'q':
            sendText('退出成功')
            return
        if not msg:
            sendText('输入超时，自动退出程序')
            return

        userId = msg
        if len(msg) > 12:
            userId = getUserID(msg)
            if not userId:
                sendText('输入错误，自动退出程序')
                return

        sendText("请输入要授权的天数")
        day = input(60000)
        if day == 'q':
            sendText('退出成功')
            return
        if not day:
            sendText('输入超时，自动退出程序')
            return
        if not day.isdigit():
            sendText('输入错误，自动退出程序')
            return

        bucketSet('sm_elm_vip', userId, (time.time()) + int(day) * 24 * 60 * 60)

        sendText('授权成功')
        return


def getDaysFromTimestamp(timestamp):
    nowTimestamp = time.time()
    diffSeconds = timestamp - nowTimestamp
    days = diffSeconds // (60 * 60 * 24)
    hours = diffSeconds % (60 * 60 * 24) // (60 * 60)

    if days < 1:
        return f"{hours}小时"
    return f"{days}天"


def get_elm_userData(ck):
    body = request({
        "url": "https://restapi.ele.me/eus/v5/user_detail",
        "headers": {
            "cookie": ck,
        },
        "method": "get",
        "dataType": "json",
        "timeOut": 30000
    })
    return body


def ifValid(ck):
    body = get_elm_userData(ck)

    if not body:
        return False
    if body.get("message"):
        return False

    return True


def getUserID(ck):
    userIdRegex = r"USERID=(\d+)"
    userIdMatch = re.search(userIdRegex, ck)
    if not userIdMatch:
        return ""
    userId = userIdMatch.group(1)
    return userId


def getDecrypt(text, key):
    result = ""
    for i in range(0, len(text), 2):
        hexChar = text[i:i + 2]
        encryptedChar = int(hexChar, 16)
        keyChar = ord(key[int(i / 2) % len(key)])
        decryptedChar = (encryptedChar - keyChar + 256) % 256
        result += chr(decryptedChar)
    return result


def subCKToQL(ck):
    containerName = bucketGet('sm_elm_config', 'ddb_ql')
    userId = getUserID(ck)
    envData = {
        "name": "elmck",
        "env": ck,
        "identity": userId,
        "remarks": userId,
    }
    msg = gaia_subEnvToQL(envData, containerName)
    return msg.get("code") == 200


def pushOverdue(type, uid, userId):
    push(
        {
            "imType": type,
            "userID": uid,
            "content": '你的elm账号：' + userId + ",已过期，请速度更新。",
        }
    )


main()