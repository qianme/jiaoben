import requests
import time

ts=int(time.time()*1000)

def info():
    res=requests.get("https://gm.total123.cn/api/mine/info",headers={
              "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
              "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NWY3MjU1MmY1NDcwZjNjMzgwNTRlYjAiLCJleHAiOjE3MTEzMDY4MDAsImlzcyI6Im1hcnZlbG91cy1vY2VhbiJ9.iUU4uA_JPRAuR-oNMchGx6TDJ6oQ53bGLY3JMH7n8Uo",
              "Host": "gm.total123.cn",
              "Connection": "Keep-Alive",
              "User-Agent": "http/4.9.3"
          }).json()
    print(res)
    mine_task_list=res['data']['mine_task_list']
    i=0
    while i<=len(mine_task_list):
        if mine_task_list[i]['mine_type_text']=='钻石':
            time.sleep(3)
        else:
            time.sleep(3)
        id=mine_task_list[i]['mine_id']
        return id
'''{
  code: 200,
  data: {
    level: 4,
    rule_text: '',
    ad_place1_taskGroup_id: '65beed6921b4a2f3744ba519',
    ad_place2_taskGroup_id: '65beed6921b4a2f3744ba519',
    dhb_task_id: '65c1a566cfef6800c1ecb330',
    treasureBox_taskGroup_id: '65beed6921b4a2f3744ba519',
    big_task_id: '65bef11321b4a2f3744ba52c',
    treasureBowl_task_id: '65c1f9dd71f62183cd32d419',
    mine_task_list: [ [Object], [Object], [Object], [Object], [Object] ],
    ad_place_list: [],
    red_packet_list_task_group_id: ''
  },
  msg: '成功'
}
{'code': 200,
 'data': {
 'level': 4, 
 'rule_text': '',
  'ad_place1_taskGroup_id'
  : '65beed6921b4a2f3744ba519',
   'ad_place2_taskGroup_id': '65beed6921b4a2f3744ba519',
    'dhb_task_id': '65c1a566cfef6800c1ecb330', 
    'treasureBox_taskGroup_id': '65beed6921b4a2f3744ba519',
     'big_task_id': '65bef11321b4a2f3744ba52c',
      'treasureBowl_task_id': '65c1f9dd71f62183cd32d419',
       'mine_task_list': [{'mine_id': '1073227178708996',
        'type_id': '10011', 'task_id': '', 'img_url': '', 'mine_type_text': ''}, {'mine_id': '1073227178708997', 'type_id': '10011', 'task_id': '', 'img_url': '', 'mine_type_text': ''}, {'mine_id': '1073227178708998', 'type_id': '10011', 'task_id': '', 'img_url': '', 'mine_type_text': ''}, {'mine_id': '1073227178708999', 'type_id': '10011', 'task_id': '', 'img_url': '', 'mine_type_text': ''}, {'mine_id': '1073227178709000', 'type_id': '10011', 'task_id': '', 'img_url': '', 'mine_type_text': ''}], 'ad_place_list': [], 'red_packet_list_task_group_id': ''}, 'msg': '成功'}

'''
# info()

def get():
    res=requests.post('https://gm.total123.cn/api/mine/get',json={'id':info()},headers={
              "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
              "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NWY3MjU1MmY1NDcwZjNjMzgwNTRlYjAiLCJleHAiOjE3MTEzMDY4MDAsImlzcyI6Im1hcnZlbG91cy1vY2VhbiJ9.iUU4uA_JPRAuR-oNMchGx6TDJ6oQ53bGLY3JMH7n8Uo",
              "Content-Type": "application/json; charset=UTF-8",
              "Content-Length": "24",
              "Host": "gm.total123.cn",
              "Connection": "Keep-Alive",
              "User-Agent": "http/4.9.3"
          }).json()
    print(res)

def task():
    res=requests.post("https://flsdk.total123.cn/api/task/finishAndReceive",json={"id": "65c1f9dd71f62183cd32d419"},headers={
              "sign": "EexVAtjjo9kYOqYYnYAtWZFB07rXKtcdkaC+XStQy1L5n3IdGFEH1BtghYLJs7+oIP+/0TnWVgWsmr7Se8zIGXyGoEG5Srbs6hD0Ow0G16fa7oEkZKB/qmiBrJf1le7br2gMCaQZUuQn5LdWg5Eqjibj7TRjgfo8Z6atgCOocJE=",
              "pkg": "com.heliangtec.gm",
              "appid": "FL_dd15r476766c",
              "profile": "release",
              "channel": "web",
              "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
              "version-code": "3",
              "ts": str(ts),
              "sdkVersionCode": '2',
              "bearer": "f62221144c0277e6a6689957d2d7f3a7fdc2b677-1190-45dc-ba7d-a96216108cbd",
              "Content-Type": "application/json; charset=UTF-8",
              "Content-Length": "33",
              "Host": "flsdk.total123.cn",
              "Connection": "Keep-Alive",
              "User-Agent": "http/4.9.3"
          }).json()
    print(res)
# get()
def precent():
    res=requests.get("https://flsdk.total123.cn/api/withdrawal/percent",headers={
              "sign": "rIxoNSqO9ByXoNWtPLDZQydq1brwHwaL8dCAkV0JjMbYA+bMA9vgmS35Lxc+9RupXE0FsgtmCiaSviZSrckF8Se2nPBn16w1cdaysFnBh6/oN6n6YuHx26F5jcMDPd3JQ/12m+MgaWIjWKW812v4lDGMefsHVUYUevvFNjcBiRA=",
              "pkg": "com.heliangtec.gm",
              "appid": "FL_dd15r476766c",
              "profile": "release",
              "channel": "web",
              "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
              "version-code": "3",
              "ts": "1710697254561",
              "sdkVersionCode": "2",
              "bearer": "f62221144c0277e6a6689957d2d7f3a7fdc2b677-1190-45dc-ba7d-a96216108cbd",
              "Host": "flsdk.total123.cn",
              "Connection": "Keep-Alive",
              "User-Agent": "http/4.9.3"
          }).json()
    print(res)
# get()
task()
# precent()