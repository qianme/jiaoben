import requests
import re
import time
import hashlib


def main():
    url='http://26ce09aeaf7ad86f6ab11e138d12cf56.d9pft3.cloud/haobaobao/rtlink'
    headers={
        'Cookie': 'bbus=eyJpdiI6IlRJVVFFZStEdmhJQ1I2M1Z0Y2I0K0E9PSIsInZhbHVlIjoiaFVPcjl3bFExSzZYcDJPOHEyb0xuczhIc0UxQThleGticDFoMFhUR3VNK1VYUUdDWHFqN0xMQnNWQUdXUlFIWTN0eU05XC9UWjkxZHVlOXpaXC9XRUYzN09Ga29YalpoQUZtc2FJSHdNN3h3YjFwWFlDU1ZKOHBGdGI0RFlGbGdFZGZ6bHMxYkJLdzg0ZXNCNGdwXC9WNkwwbFg2eldsQ2Y0U1pQcXlyUHFFRUdDaEkwRmR5SzZJK043dE9YYk1Ic3FvRjVXemt2RjNhUGc3Zmt4NHNKUHZcL3F4K09LVWNHeXhYZTc5UzVTWXNtOGZSUTRpRXVMRmVDXC9ZR09xajU0TldyY1BWeG1MWjNsWWFGa1dHUUZUT1hQQkVHZ0FtZVBEUE15czBHN3BBdVR5WlwvY1F6OHRZUE04dUkya05SRCtpWitPZ2tFbW1tWGJyektvanpkRG10WkF5TDJDQWxsc24zXC9MalEwV3lNYlpHWkh1SDN2MmdrNzQ2SDlkRG53d3FNWHJ1enhOSWRaQ3ZUTkFRWHNkZ1REbXNEUzF3V0E0bFhUbytYWGQ2ZEluMko4THBoMmgxMWduRHBNTVdcL2lOdVpSelJlNmJYdXluS2VWWk1qNlh4OW8xaUdKTGR4cXlcL2VTSkNPSGN1ZnlnOHdBZ3VYUmtUNkVnY0VBc0tJWHhLQlBoZ0YrbDhpVlNJSEQ4MXpTQmZ2QnByUmlOXC9jWWJhZnI3MzZcL1NDSGJwV1RqeTljZTJcL253V2RrUTJIa3pPVk42RXVEQ3k3MlJocmJVWFwvdnZlNUtyZkxCU09tbTdsYkphYW1iOGphMzAwYytiMGI5MGRyblFyOU80VHFEREFxODg5MXV3ckFcL1RLWjdZU0lWaGJ6dDJTa3hrZEVPSDJcL2JBdVNWYnhcL0xGdjB6U0dTVTJoaUV2ckFCWWtpYVwvczZLOVFvWjU5d2pCaG1SQkc4NnpFSXVKXC9RPT0iLCJtYWMiOiI3NGVhNzdkZWUxMmZjNjQxYzNiNDM2ZWFjNDA2YzljZmZlMzZmM2Q1NTQyYTU5NjgyZGNkODNkOThkNzFiZmU5In0%253D',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2f) NetType/WIFI Language/zh_CN',
    }

    res = requests.get(url,headers=headers).json()
    link=res['data']['readlink']
    link_re=f'(.*)/rd'
    link_url=re.findall(link_re,link)[0]
    return link_url


def sign():
    host_re=f'http://(.*)'
    host = re.findall(host_re,main())[0]
    n=int(time.time()*1000)
    n = str(n)
    # s = host+n+'Lj*?Q3#pOviW'
    sign=hashlib.md5((host+n+'Lj*?Q3#pOviW').encode()).hexdigest()
    return sign

def read():
    host_re=f'http://(.*)'
    host = re.findall(host_re,main())[0]
    url=f'{main()}/haobaobao/getread?time={int(time.time())*1000}&mysign={sign()}'
    headers={
        'Cookie': 'bbusr=eyJpdiI6ImJBZlVDWjVcLzVPU0tqbGtIXC8ybkhDQT09IiwidmFsdWUiOiJyTGFhd3N6cW9Uak13b0ZtT2cyUE5jZFJsblwvQTU1VjR6XC80ZHN1S0UwQVwvM0xldEFFaURadUZlRTBYYzlQc1ZKNWpvZGM5QzFicnNQT3ZpOVNpaXNlbks1SXRqWUdMZktFb1wvd2thRWFhWXJaSnIyYzFycENFMG4xTGY1YWt4ekUiLCJtYWMiOiJmMTkwNjAyN2NiMDA4YzY5MzA1ZDVlYmI0MjM5NDEzYzQ5OGY3YzA1MGUzNWY0MWNmZWJiNjNlMGIzMDdiNWU4In0%253D',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2f) NetType/WIFI Language/zh_CN',
        'Host':host,
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
    res=requests.get(url,headers=headers).text
    print(res)
if __name__=="__main__":
    read()

# 26ce09aeaf7ad86f6ab11e138d12cf56
# 96af51a027435d8c464df6e13616b7ce