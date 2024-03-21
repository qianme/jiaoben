import requests
import time

#
# no = int(time.time()*1000000000)
# print(no)
# url='http://task-h5-api.188pi.com/api/Withdrawal/withdrawal'
# url='http://task-h5-api.188pi.com/api/Usertask/selectUserTaskRes'
url='http://task-h5-api.188pi.com/api/Usertask/complateArticle'
headers={
    # 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MDE2NjMzNjgsIm5iZiI6MTcwMTY2MzM2OCwiZXhwIjoxNzA4ODYzMzY4LCJkYXRhIjp7InVpZCI6IjYwNzAifX0.Zk1LFd4Jl0bMCjs1VG1GE1BGzUnIYPmYluidIj9lQSM',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MDE5NTMyMzAsIm5iZiI6MTcwMTk1MzIzMCwiZXhwIjoxNzAxOTU0NDMwLCJkYXRhIjp7InVpZCI6IjEzMDU2In19.FQigVMxfzv5kdxTrxVvdLUKPDfDBuqGD8ZH-zjMD6WU',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2f) NetType/WIFI Language/zh_CN',

}

# data={"no":no}

data={"encrypt":"ODJ5n3tTwVInMty2FBqAGytdivY+36qYB+hfTqJIKr+78bHaIFbHxZtYA3tkKXmmQCliQ7YTjbn0Cb/3dmpzUEeOqmKy1KySQWYVbPBKGJY=","times":1,"number":10,"read_links":""}
res=requests.post(url,headers=headers,data=data).json()
print(res)
