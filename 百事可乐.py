import httpx
import os

"""
抓包关键词：draw
变量名:bskl
变量格式:token#备注  
"""
#组队
def Team(token,name):
	url='https://pepcoinbhhpre.pepcoinbypepsico.com.cn/mp/getMyTeam'
	headers={'token':f"{token}"}
	res=httpx.get(url,headers=headers).text
	print(res)
	print(name)

#抽奖
def draw(token,name):
	try:
		j = 1
		while j < 8:
			url='https://pepcoinbhhpre.pepcoinbypepsico.com.cn/mp/draw'
			headers={'token':f'{token}'}
			res=httpx.get(url,headers=headers).json()
			if 'data' not in res:
				print(f"{name},{res['msg']},抽奖结束")
				break
			elif 'data' in res:
				print(f'{name},第{j}次抽中:{res["data"]["name"]}')
				j+=1
	except:
		print('程序发生异常')



# bskl=os.getenv('bskl')
bskl='5d5a72bdee65ff556fe440eb2e0bcdcab7f5c933909ca8e2fad8ed67b2f0a7e5,oKW2E4tZ90OjIah-dL022tISZY6Q#小黑'
tokens=bskl.split('&')
for token1 in tokens:
	token=token1.split("#")
	Team(token[0],token[1])



