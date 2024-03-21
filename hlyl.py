import requests
import time


timestamp=int(time.time()*1000)
def  xx():
    data={"gameLevel":1,
          "gameType":1,
          "gameResult":1,
          "playType":1,
          "gameUseTotalTime":142007,
          "recordId":2025227,
          "encryption":"4B84DA47D31D5ED5C8D14CBE9507F5D0",
          "uniqueCode":"o8SsY5B5_R1_vmrw3t49tQqXuSYI1709555859061321057",
          "screenshot":"https://prod-wx-public-web-1302259445.cos.ap-beijing.myqcloud.com/wx-camp-180-02-prod/tmp_b59198bfebd2e4d3a920d39ab6ac01545d49ad9b159f8d83.jpg",
          "clickNum":14,
          "endTime":f'{timestamp}-1',
          "openId":"o8SsY5B5_R1_vmrw3t49tQqXuSYI"
          }
    headers={'token':'eyJ1c2VySWQiOjY1OTMwLCJ0aW1lc3RhbXAiOjE3MDk1NTU1MDAxMDJ9.9b96f55ef0da849bde3be71efd1ebfec',
             'signature':'rYBnZwb4OWYh1DWk4b1PJNalKbXfw/j6wg4f47AFFnT3T+UpCOu4POyHrg4UGpiXQS7tQYgBiXV9QbMj5g2e7+jpoUxbUBas3Fa/JH6o+TAvcQ7SZSGitxWLO1btE9pPknE5VPaxdZBLgBbtx6vXHtAkaoPmso1V2/EX44NiQ1Y3zT+Djds2+CLqtflPnhsPlVTcmOBvgQANoW2pi0uDJMrcazO4AfIbyc5b0q8RrYKMaUDkO3ofPKZe9UXdHbnU9lzNapgSDokPGs4X53R1YbawVvvbHKNSY4hD2jJAr3OdsL840P1tkxU+X1pmNTP9svjngmz7ywRt8BtN7Ug7qA==',
             'timestamp': f"{timestamp}",
             'uniquecode': f'{timestamp}&102030'}
    url='https://wx-camp-180-02-applet-api.mscampapi.digitalyili.com/play/game/game/end/get/prize'
    res=requests.post(url,headers=headers,json=data).text
    print(res)

xx()