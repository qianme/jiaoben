import requests
import os

def daili():
    url='https://api.ttayu.com/task/dailyCheckInV2'
    headers={
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYXh4a2ouY29tIiwiYXVkIjoiY2F4eGtqLmNvbSIsImlhdCI6MTcwOTAzOTk3NCwibmJmIjoxNzA5MDM5OTc0LCJleHAiOjE3MTQyMjM5NzQsImV4dGVuZCI6eyJpZCI6Nzk2MjM0OSwibmFtZSI6Ilx1NjI2N1x1N2IxNFx1NzUzYlx1N2QyMFx1OTg5YyIsInByb2plY3QiOiJcdTRlZDZcdTkwNDcifX0.vPUP9HGgppKEme2KABkYHAxDkdKYiGq7_TMyHHA2Tq8'
    }
    res=requests.post(url,headers=headers).text
    print('')
#
# #发布动态
# def create():
#     url='https://api.ttayu.com/dynamic/create'
#     data={"address":"广州市","content":"ssssdr"}
#     headers={
#         'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYXh4a2ouY29tIiwiYXVkIjoiY2F4eGtqLmNvbSIsImlhdCI6MTcwOTAzOTk3NCwibmJmIjoxNzA5MDM5OTc0LCJleHAiOjE3MTQyMjM5NzQsImV4dGVuZCI6eyJpZCI6Nzk2MjM0OSwibmFtZSI6Ilx1NjI2N1x1N2IxNFx1NzUzYlx1N2QyMFx1OTg5YyIsInByb2plY3QiOiJcdTRlZDZcdTkwNDcifX0.vPUP9HGgppKEme2KABkYHAxDkdKYiGq7_TMyHHA2Tq8'
#     }
#     res=requests.post(url,headers=headers,data=data).text
#     print(res)
#
# #点赞
# def put():
#     url='https://api.ttayu.com/giveLike/put'
#     data={"like_id":"79134","to_user_id":"5845417","type":"DYNAMIC"}
#     headers={
#         'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYXh4a2ouY29tIiwiYXVkIjoiY2F4eGtqLmNvbSIsImlhdCI6MTcwOTAzOTk3NCwibmJmIjoxNzA5MDM5OTc0LCJleHAiOjE3MTQyMjM5NzQsImV4dGVuZCI6eyJpZCI6Nzk2MjM0OSwibmFtZSI6Ilx1NjI2N1x1N2IxNFx1NzUzYlx1N2QyMFx1OTg5YyIsInByb2plY3QiOiJcdTRlZDZcdTkwNDcifX0.vPUP9HGgppKEme2KABkYHAxDkdKYiGq7_TMyHHA2Tq8'
#     }
#     res=requests.post(url,headers=headers,data=data).json()
#     print(res)


def get(ck):
    url='https://api.ttayu.com/task/dailyTaskGet'
    headers={
        'authorization': ck
    }
    keys=['sign','dynamic_create','dynamic_give_like','dynamic_give_like','dynamic_give_like','dynamic_comment','dynamic_comment','voice_match','video_match',]#'invite_friend'
    for key in keys:
        data={'key':key}
        res=requests.post(url,headers=headers,data=data).json()
        if res['code']==0:
            if key =='sign':
                print('签到任务完成✔')
                print('签到奖励领取完成✔')
            elif key == 'dynamic_create':
                print('发布动态任务完成✔')
                print('发布动态签到奖励领取完成✔')
            elif key == 'dynamic_give_like':
                print('点赞任务完成✔')
                print('点赞签到奖励领取完成✔')
            elif key =='dynamic_comment':
                print('评论任务完成✔')
                print('评论奖励领取完成✔')
            elif key =='voice_match':
                print('语音任务完成✔')
                print('语音奖励领取完成✔')
            elif key == 'video_match':
                print('视频任务完成✔')
                print('视频签到奖励领取完成✔')
        elif res['code'] == 1:
            if key =='sign':
                print(f'签到奖励:{res["message"]}')
            elif key == 'dynamic_create':
                print(f'发布动态奖励:{res["message"]}')
            elif key == 'dynamic_give_like':
                print(f'点赞签到奖励:{res["message"]}')
            elif key =='dynamic_comment':
                print(f'评论奖励:{res["message"]}')
            elif key =='voice_match':
                print(f'语音奖励:{res["message"]}')
            elif key == 'video_match':
                print(f'视频签到奖励:{res["message"]}')
        else:
            print(res)


if __name__=="__main__":
    at=os.getenv('yuemo')
    cks=at.split('&')
    for ck in cks:
        get(ck)


#'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYXh4a2ouY29tIiwiYXVkIjoiY2F4eGtqLmNvbSIsImlhdCI6MTcwOTAzOTk3NCwibmJmIjoxNzA5MDM5OTc0LCJleHAiOjE3MTQyMjM5NzQsImV4dGVuZCI6eyJpZCI6Nzk2MjM0OSwibmFtZSI6Ilx1NjI2N1x1N2IxNFx1NzUzYlx1N2QyMFx1OTg5YyIsInByb2plY3QiOiJcdTRlZDZcdTkwNDcifX0.vPUP9HGgppKEme2KABkYHAxDkdKYiGq7_TMyHHA2Tq8'