import requests
import json
import random
import time
import os



#变量名：tjn  格式：账号#密码

def add(token, id, userName, j):
    if j == 0:
        return print(f'账号{userName}本时段回帖奖励已满')
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'Tjnlt_token': token,
            'referer':f'https://forum.tongjiniao.com/postDetail?topicId={id}',
            'content-type': 'application/json'
        }
        c_url='https://forum.tongjiniao.com/api/common/getCaptcha?type=comment'
        c_data={}
        c_res=requests.post(c_url,headers=headers,data=c_data).json()['id']
        # print(c_res)
        a_url='https://forum.tongjiniao.com/api/common/checkCaptcha'
        a_data={"id":c_res,"data":{"bgImageWidth":295,"bgImageHeight":180,"sliderImageWidth":130,"sliderImageHeight":35,"startSlidingTime":"2024-03-03T17:38:17.908Z","endSlidingTime":"2024-03-03T17:38:33.460Z","trackList":[{"x":219,"y":90,"type":"click","t":8219},{"x":420,"y":16618,"type":"move","t":8519},{"x":418,"y":16618,"type":"move","t":8526},{"x":415,"y":16618,"type":"move","t":8534},{"x":414,"y":16618,"type":"move","t":8542},{"x":412,"y":16618,"type":"move","t":8548},{"x":411,"y":16618,"type":"move","t":8556},{"x":409,"y":16618,"type":"move","t":8578},{"x":408,"y":16618,"type":"move","t":8602},{"x":406,"y":16618,"type":"move","t":8608},{"x":405,"y":16618,"type":"move","t":8615},{"x":402,"y":16617,"type":"move","t":8624},{"x":400,"y":16617,"type":"move","t":8632},{"x":397,"y":16615,"type":"move","t":8638},{"x":396,"y":16615,"type":"move","t":8645},{"x":393,"y":16614,"type":"move","t":8654},{"x":391,"y":16614,"type":"move","t":8662},{"x":388,"y":16614,"type":"move","t":8668},{"x":385,"y":16614,"type":"move","t":8676},{"x":382,"y":16614,"type":"move","t":8684},{"x":378,"y":16614,"type":"move","t":8692},{"x":373,"y":16614,"type":"move","t":8697},{"x":370,"y":16612,"type":"move","t":8706},{"x":367,"y":16612,"type":"move","t":8714},{"x":363,"y":16612,"type":"move","t":8722},{"x":360,"y":16612,"type":"move","t":8728},{"x":358,"y":16612,"type":"move","t":8736},{"x":355,"y":16612,"type":"move","t":8743},{"x":352,"y":16612,"type":"move","t":8752},{"x":351,"y":16612,"type":"move","t":8758},{"x":349,"y":16613,"type":"move","t":8766},{"x":346,"y":16615,"type":"move","t":8774},{"x":343,"y":16616,"type":"move","t":8782},{"x":340,"y":16619,"type":"move","t":8788},{"x":337,"y":16622,"type":"move","t":8796},{"x":333,"y":16625,"type":"move","t":8804},{"x":330,"y":16628,"type":"move","t":8811},{"x":325,"y":16631,"type":"move","t":8818},{"x":322,"y":16634,"type":"move","t":8826},{"x":318,"y":16637,"type":"move","t":8834},{"x":315,"y":16639,"type":"move","t":8842},{"x":312,"y":16640,"type":"move","t":8847},{"x":309,"y":16642,"type":"move","t":8856},{"x":306,"y":16643,"type":"move","t":8864},{"x":304,"y":16643,"type":"move","t":8872},{"x":303,"y":16643,"type":"move","t":8886},{"x":301,"y":16643,"type":"move","t":8908},{"x":300,"y":16643,"type":"move","t":8924},{"x":298,"y":16643,"type":"move","t":8938},{"x":297,"y":16643,"type":"move","t":8945},{"x":294,"y":16643,"type":"move","t":8954},{"x":292,"y":16643,"type":"move","t":8961},{"x":288,"y":16643,"type":"move","t":8968},{"x":285,"y":16643,"type":"move","t":8976},{"x":280,"y":16643,"type":"move","t":8983},{"x":274,"y":16643,"type":"move","t":8992},{"x":270,"y":16643,"type":"move","t":8998},{"x":264,"y":16643,"type":"move","t":9006},{"x":259,"y":16642,"type":"move","t":9014},{"x":253,"y":16642,"type":"move","t":9022},{"x":249,"y":16641,"type":"move","t":9028},{"x":244,"y":16641,"type":"move","t":9036},{"x":240,"y":16639,"type":"move","t":9045},{"x":235,"y":16638,"type":"move","t":9052},{"x":232,"y":16638,"type":"move","t":9058},{"x":229,"y":16636,"type":"move","t":9066},{"x":228,"y":16635,"type":"move","t":9074},{"x":225,"y":16635,"type":"move","t":9082},{"x":223,"y":16635,"type":"move","t":9088},{"x":222,"y":16635,"type":"move","t":9095},{"x":220,"y":16635,"type":"move","t":9118},{"x":220,"y":16633,"type":"move","t":9148},{"x":220,"y":16632,"type":"move","t":9164},{"x":219,"y":16630,"type":"move","t":9179},{"x":217,"y":16630,"type":"move","t":9202},{"x":217,"y":16629,"type":"move","t":9298},{"x":217,"y":16627,"type":"move","t":9314},{"x":217,"y":16626,"type":"move","t":9327},{"x":217,"y":16624,"type":"move","t":9493},{"x":218,"y":16624,"type":"move","t":9508},{"x":218,"y":16623,"type":"move","t":9524},{"x":220,"y":16623,"type":"move","t":9530},{"x":220,"y":16621,"type":"move","t":9546},{"x":220,"y":16620,"type":"move","t":9560},{"x":220,"y":16618,"type":"move","t":9577},{"x":220,"y":16617,"type":"move","t":10099},{"x":221,"y":16617,"type":"move","t":10108},{"x":221,"y":16615,"type":"move","t":10124},{"x":221,"y":16614,"type":"move","t":10154},{"x":19,"y":86,"type":"click","t":11016},{"x":223,"y":16614,"type":"move","t":11458},{"x":224,"y":16614,"type":"move","t":11480},{"x":226,"y":16614,"type":"move","t":11488},{"x":227,"y":16614,"type":"move","t":11518},{"x":229,"y":16614,"type":"move","t":11540},{"x":230,"y":16614,"type":"move","t":11561},{"x":232,"y":16614,"type":"move","t":11578},{"x":233,"y":16614,"type":"move","t":11600},{"x":235,"y":16615,"type":"move","t":11622},{"x":236,"y":16615,"type":"move","t":11638},{"x":238,"y":16615,"type":"move","t":11646},{"x":238,"y":16616,"type":"move","t":11660},{"x":239,"y":16616,"type":"move","t":11668},{"x":239,"y":16618,"type":"move","t":11676},{"x":241,"y":16618,"type":"move","t":11690},{"x":242,"y":16618,"type":"move","t":11698},{"x":244,"y":16618,"type":"move","t":11706},{"x":245,"y":16618,"type":"move","t":11720},{"x":247,"y":16618,"type":"move","t":11728},{"x":248,"y":16618,"type":"move","t":11900},{"x":248,"y":16619,"type":"move","t":11908},{"x":250,"y":16619,"type":"move","t":11914},{"x":250,"y":16621,"type":"move","t":11922},{"x":251,"y":16622,"type":"move","t":11930},{"x":253,"y":16622,"type":"move","t":11938},{"x":254,"y":16622,"type":"move","t":11952},{"x":256,"y":16624,"type":"move","t":11959},{"x":257,"y":16625,"type":"move","t":11974},{"x":259,"y":16627,"type":"move","t":11990},{"x":260,"y":16627,"type":"move","t":11998},{"x":260,"y":16628,"type":"move","t":12003},{"x":262,"y":16630,"type":"move","t":12012},{"x":263,"y":16630,"type":"move","t":12020},{"x":263,"y":16631,"type":"move","t":12028},{"x":265,"y":16631,"type":"move","t":12034},{"x":266,"y":16633,"type":"move","t":12042},{"x":268,"y":16634,"type":"move","t":12050},{"x":269,"y":16634,"type":"move","t":12057},{"x":269,"y":16636,"type":"move","t":12064},{"x":271,"y":16637,"type":"move","t":12072},{"x":272,"y":16639,"type":"move","t":12080},{"x":274,"y":16640,"type":"move","t":12088},{"x":275,"y":16640,"type":"move","t":12094},{"x":275,"y":16642,"type":"move","t":12102},{"x":277,"y":16642,"type":"move","t":12109},{"x":278,"y":16643,"type":"move","t":12124},{"x":280,"y":16643,"type":"move","t":12148},{"x":281,"y":16643,"type":"move","t":12169},{"x":283,"y":16643,"type":"move","t":12282},{"x":284,"y":16643,"type":"move","t":12304},{"x":287,"y":16643,"type":"move","t":12312},{"x":290,"y":16643,"type":"move","t":12319},{"x":293,"y":16643,"type":"move","t":12328},{"x":298,"y":16642,"type":"move","t":12334},{"x":301,"y":16642,"type":"move","t":12341},{"x":305,"y":16639,"type":"move","t":12350},{"x":310,"y":16638,"type":"move","t":12358},{"x":316,"y":16635,"type":"move","t":12364},{"x":323,"y":16630,"type":"move","t":12372},{"x":329,"y":16627,"type":"move","t":12380},{"x":335,"y":16623,"type":"move","t":12388},{"x":341,"y":16620,"type":"move","t":12394},{"x":346,"y":16617,"type":"move","t":12402},{"x":350,"y":16612,"type":"move","t":12410},{"x":355,"y":16611,"type":"move","t":12418},{"x":358,"y":16608,"type":"move","t":12424},{"x":361,"y":16606,"type":"move","t":12432},{"x":362,"y":16605,"type":"move","t":12440},{"x":365,"y":16602,"type":"move","t":12448},{"x":368,"y":16600,"type":"move","t":12453},{"x":371,"y":16597,"type":"move","t":12462},{"x":373,"y":16596,"type":"move","t":12470},{"x":374,"y":16594,"type":"move","t":12478},{"x":376,"y":16593,"type":"move","t":12484},{"x":377,"y":16591,"type":"move","t":12491},{"x":377,"y":16590,"type":"move","t":12530},{"x":377,"y":16588,"type":"move","t":13315},{"x":376,"y":16588,"type":"move","t":13324},{"x":375,"y":16588,"type":"move","t":13340},{"x":375,"y":16587,"type":"move","t":13346},{"x":373,"y":16585,"type":"move","t":13362},{"x":372,"y":16585,"type":"move","t":13384},{"x":372,"y":16584,"type":"move","t":13400},{"x":370,"y":16584,"type":"move","t":13406},{"x":168,"y":56,"type":"click","t":14210},{"x":369,"y":16586,"type":"move","t":14344},{"x":366,"y":16591,"type":"move","t":14352},{"x":361,"y":16598,"type":"move","t":14360},{"x":357,"y":16606,"type":"move","t":14366},{"x":351,"y":16615,"type":"move","t":14374},{"x":346,"y":16621,"type":"move","t":14382},{"x":342,"y":16625,"type":"move","t":14390},{"x":339,"y":16630,"type":"move","t":14396},{"x":336,"y":16633,"type":"move","t":14404},{"x":334,"y":16634,"type":"move","t":14412},{"x":333,"y":16636,"type":"move","t":14420},{"x":331,"y":16636,"type":"move","t":14441},{"x":330,"y":16636,"type":"move","t":14456},{"x":328,"y":16636,"type":"move","t":14480},{"x":327,"y":16636,"type":"move","t":14554},{"x":325,"y":16636,"type":"move","t":14562},{"x":324,"y":16636,"type":"move","t":14568},{"x":322,"y":16636,"type":"move","t":14576},{"x":321,"y":16636,"type":"move","t":14584},{"x":318,"y":16636,"type":"move","t":14598},{"x":316,"y":16636,"type":"move","t":14606},{"x":315,"y":16636,"type":"move","t":14614},{"x":313,"y":16636,"type":"move","t":14622},{"x":312,"y":16636,"type":"move","t":14636},{"x":310,"y":16636,"type":"move","t":14644},{"x":309,"y":16636,"type":"move","t":14657},{"x":307,"y":16637,"type":"move","t":14748},{"x":306,"y":16637,"type":"move","t":14756},{"x":304,"y":16637,"type":"move","t":14764},{"x":303,"y":16637,"type":"move","t":14778},{"x":301,"y":16637,"type":"move","t":14802},{"x":300,"y":16637,"type":"move","t":14823},{"x":300,"y":16639,"type":"move","t":14854},{"x":298,"y":16639,"type":"move","t":14862},{"x":297,"y":16639,"type":"move","t":14876},{"x":295,"y":16639,"type":"move","t":14922},{"x":294,"y":16639,"type":"move","t":14944},{"x":292,"y":16639,"type":"move","t":14988},{"x":291,"y":16639,"type":"move","t":15012},{"x":289,"y":16639,"type":"move","t":15034},{"x":288,"y":16639,"type":"move","t":15048},{"x":288,"y":16640,"type":"move","t":15055},{"x":286,"y":16640,"type":"move","t":15072},{"x":286,"y":16642,"type":"move","t":15078},{"x":285,"y":16642,"type":"move","t":15086},{"x":283,"y":16642,"type":"move","t":15102},{"x":283,"y":16643,"type":"move","t":15108},{"x":282,"y":16643,"type":"move","t":15116},{"x":282,"y":16645,"type":"move","t":15124},{"x":280,"y":16645,"type":"move","t":15132},{"x":280,"y":16646,"type":"move","t":15138},{"x":279,"y":16646,"type":"move","t":15154},{"x":279,"y":16648,"type":"move","t":15162},{"x":277,"y":16648,"type":"move","t":15206},{"x":75,"y":120,"type":"click","t":15552}]}}
        a_res=requests.post(a_url,headers=headers,json=a_data).json()
        print(a_res)
        url = 'https://forum.tongjiniao.com/api/comment/addComment'
        data = {"captchaId":c_res,"content":"<p><span style=\"color: rgba(0, 0, 0, 0.85); background-color: rgb(255, 255, 255); font-size: 14px;\">我要成为仙鹤</span></p>","topicId":"1762380560497508352","signatureStatus":2}
        res = requests.post(url, headers=headers, json=data).json()
        # print(res)
        if res['code'] == 200:
            if '2' in res['data']:
                print(f'账号{userName}，本次回帖获取{res["data"]["2"]}')
            else:
                print('该文章已经回复过啦！')
        else:
            return print(res['msg'])


def topic(token, id, userName, k):
    if k == 0:
        return print(f'账号{userName}本时段点赞奖励已满')
    else:
        url1 = 'https://forum.tongjiniao.com/api/like/topic'
        data = {'topicId': id, 'status': 2}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'Tjnlt_token': token}
        res = requests.post(url1, json=data, headers=headers).json()
        if res['code'] == 200:
            if '2' in res['data']:
                print(f'账号{userName},本次回帖获取{res["data"]["2"]}')
            else:
                print('该文章已经点过赞了！')
        else:
            return print(res['msg'])


def look(token, id, userName, l):
    if l == 0:
        return print(f'账号{userName}本时段浏览奖励已满')
    else:
        url = f'https://forum.tongjiniao.com/api/topic/getTopicDetails/{id}'
        headers = {
            'tjnlt_token': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
        res = requests.get(url, headers=headers).json()
        if 'integral' in res['data']:
            print(f'账号{userName},本次浏览获取{res["data"]["integral"]}')
        else:
            return print('该文章浏览过啦！')


def id(token,userName, j, k, l):
    m = random.randint(0, 100)
    # print(n)
    url = f'https://forum.tongjiniao.com/api/home/getHome?pageNum={m}&pageSize=20&topicStatus=3'
    res = requests.get(url).json()
    rows = res['rows']
    rowz=random.sample(rows, 5)
    for row in rowz:
        id = row['id']
        add(token, id, userName, j)
        # time.sleep(1)
        # topic(token, id, userName, k)
        # time.sleep(1)
        # look(token, id, userName, k)
        # time.sleep(10)


def exchange(token,userName):
    url = 'https://www.tongjiniao.com/api/integral/exchange'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Cookie': 'Hm_lvt_ffdb7f977a0e08471755659fb4bf0e2e=1708251546; token2=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9...',
        # 添加其他必要的请求头
    }
    data = {"exchange_integral": 1000}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    if response.status_code == 200:
        print(f"{userName}{result['message']}".center(30,"💵"))
    else:
        print(f"{userName}兑换失败！状态码：{response.status_code}，结果：{result['message']}")


def Tasks(token,userName):
    url = 'https://forum.tongjiniao.com/api/home/getRemainingTasks'
    headers = {'tjnlt_token': token,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    res = requests.get(url, headers=headers).json()
    j = res['data']['2']
    k = res['data']['3']
    l = res['data']['4']
    print(f'账号{userName}查询成功\n'
          f'发帖(该时段剩{res["data"]["1"]}次)\n'
          f'回帖(该时段剩{j}次)\n'
          f'点赞帖子(该时段剩{k}次\n'
          f'浏览帖子(该时段剩{l}次)')
    if j == 0 and k == 0 and l == 0:

        return print('本时段所有奖励已领取'.center(30,'♥'))
    else:
        id(token, userName, j, k, l)



def check(token,userName):
    url='https://forum.tongjiniao.com/api/common/checkToken'
    headers={
        'tjnlt_token':token
    }
    res=requests.get(url,headers=headers).text
    # print(res)
    Tasks(token,userName)

def login(user,pswd):
    url = 'https://www.tongjiniao.com/api/login'
    #url='https://www.tongjiniao.com/login?url=https://forum.tongjiniao.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'referer': 'https://www.tongjiniao.com/login?url=https://forum.tongjiniao.com/'
    }
    data = {"username": user, "password": pswd}
    res = requests.post(url, headers=headers, data=data).json()
    token=res['data']['token']
    userName=res['data']['userName']
    check(token,userName)
    exchange(token,userName)
    # print(res)

if __name__ == '__main__':
    # tjnlist=os.getenv('tjn')
    tjnlist='nanxiafenglai#woaini1320'
    zhlist = tjnlist.split('&')
    # print(tokens)
    print(f'获取到{len(zhlist)}个账号')
    for zhs in zhlist:
        zh=zhs.split('#')
        user=zh[0]
        pswd=zh[1]
        login(user,pswd)
