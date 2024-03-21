import requests
import json
import time
import hashlib
# now=int(time.time()*1000)

code='read'
appId='c5cce09750f3398185984b47fba010ab'
currentTimeMillis=int(time.time()*1000)#'1708325979007'
# contentId='8e2975cdc42a4d19b9e5b46ba4df3064'
siteId='b496650d5db94435a690db7326131dc9'
time=int(time.time()*1000)+520#'1708325979708'
versionName='4.2.2'
userId='ad13c03af19b42b0a1a98035126889b5'
platform='android'
# print(time)


def sign(contentId):
	#a=str(now) + str(now+294) + '1b32a9bb306846e0badd070065836c24' + '4.2.2' +id + 'ad13c03af19b42b0a1a98035126889b5' + 'android'+'b496650d5db94435a690db7326131dc9'+'c5cce09750f3398185984b47fba010ab'+"read"
	a=str(currentTimeMillis) + str(time) + '1b32a9bb306846e0badd070065836c24' + versionName + contentId + userId + platform + siteId + appId + code
	#a=str(currentTimeMillis) + str(time) + "1b32a9bb306846e0badd070065836c24" + versionName + appId + "android" + siteId +  contentId + userId +"read"
	# print(a)
	md=hashlib.md5(a.encode())
	md5=md.hexdigest()
	# print(now)
	# print(md5)
	# xx(contentId,md5)
	read(contentId,md5)



def xx(contentId,md5):
	url='https://app.media.ywcity.cn/contentapi/api/content/addPraise'
	data={
	'appId':'c5cce09750f3398185984b47fba010ab',
	'currentTimeMillis':currentTimeMillis,
	'siteId':'b496650d5db94435a690db7326131dc9',
	'id':contentId,
	'versionName':'4.2.2',
	'userId':'ad13c03af19b42b0a1a98035126889b5',
	'platform':'android',
	'signature':md5
	}
	res=requests.post(url,json=data).json()
	print(res)

def read(contentId,md5):
	url='https://app.media.ywcity.cn/integralapi/api/integral/event/add'
	data={
	'code':'read',
	'appId':appId,
	'currentTimeMillis':currentTimeMillis,
	'contentId':contentId,
	'siteId':siteId,
	'time':time,
	'versionName':versionName,
	'userId':userId,
	'platform':platform,
	'signature':md5
	}
	headers={
		"Content-Type": "application/x-www-form-urlencoded",
		"Content-Length": "300",
		"Host": "app.media.ywcity.cn",
		"Connection": "Keep-Alive",
		"User-Agent": "okhttp/4.10.0"
	}

	# print(data)
	res=requests.post(url,json=data,headers=headers).json()
	print(res)
	
	
def id():
	url='https://mkapi.xinhuamm.net/coinApi/clapi/content/getHighContentList'
	data={}
	headers={
	'token':'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZWI1MzQxMzkwZTE0MDkwODAyNjJlY2UwNGZhMmNlYSIsInN1YiI6IntcImFwcElkXCI6XCIzYWUzOWUzMjI5OWM0ZGFmYWNiNTQwNDRlYzRkYjYzMFwiLFwiY3NcIjpcIjBkNDdmZWQ4NjkyNjRhNmM5YjgwODNiNDY5Nzg3MzU2XCIsXCJkZWxpdmVyXCI6XCJ7XFxcInNpdGVJZFxcXCI6XFxcImI0OTY2NTBkNWRiOTQ0MzVhNjkwZGI3MzI2MTMxZGM5XFxcIn1cIixcImlkXCI6XCI3YzY3NThhMDFlNmQ0ZGExOWIwM2I4YzY3ZTU3ZmNhOVwiLFwiaXNUZW1wb3JhcnlcIjowLFwiaXNWaXNpdG9yXCI6MCxcImxlZXNzQ29kZVwiOlwiYWl5aXd1XCIsXCJsZXNzZWVJZFwiOlwiY2Q1OGMxOGIzMDcyNDI3OWI3Y2E4ZjVjYTNlOTRmZTNcIixcIm5hbWVcIjpcIuS8muWRmGExRzg0bTlKTE1cIixcInBob25lXCI6XCIxNTg3ODI2NTgyNlwiLFwicG9pbnRzXCI6OTAsXCJwb3J0cmFpdFwiOlwiXCIsXCJ0aGlyZElkXCI6XCJhZDEzYzAzYWYxOWI0MmIwYTFhOTgwMzUxMjY4ODliNVwiLFwidGltZVN0YW1wXCI6MTcwODI5NzcyMzU1MyxcInVzXCI6XCI1ZDFjMzA0MjJkMjg0MzRjOGNhMDMxMmNlYjEyZWM3M1wiLFwidXNlclR5cGVcIjpcIjFcIn0iLCJpc3MiOiJ1c2VyIiwiaWF0IjoxNzA4Mjk3NzIzLCJleHAiOjE3MDg5MDI1MjN9.ZxXoPklPBZAsRpqZDr271pQqxwxqIA7ZUoXwDTagyJg'
	}
	res=requests.post(url,json=data,headers=headers).json()
	list=res['list']
	#print(list)
	for ids in list:
		id=ids['contentId']
		# print(ids)
		sign(id)
	
id()

