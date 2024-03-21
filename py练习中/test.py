import httpx
import re
import json
client = httpx.Client()

def login():
  url = 'https://www.juliangip.com/login/go'

  headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
  }

  data={
    "type":"password",
"username":15878265826,
"password":"woaini1320",
"sms_code":""
  }

  res = client.post(url=url,data=data,headers=headers).json()
  # print(res['message'])
  img()

def img():
  _url='https://turing.captcha.qcloud.com'
  # url='https://www.juliangip.com/users/'
  url = 'https://turing.captcha.qcloud.com/cap_union_prehandle?aid=2081343300&protocol=https&accver=1&showtype=popup&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTkuMC4wLjA%3D&noheader=1&fb=1&aged=0&enableAged=0&enableDarkMode=0&grayscale=1&clientype=2&cap_cd=&uid=&lang=zh-cn&entry_url=https%3A%2F%2Fwww.juliangip.com%2Fusers%2F&elder_captcha=0&js=%2Ftcaptcha-frame.22125576.js&login_appid=&wb=1&subsid=1&callback=_aq_495053&sess='
  headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
  }
  res = client.get(url=url,headers=headers).text
  d_re = f'_aq_495053\((.*)\)'
  d = re.findall(d_re,res)[0]
  d = json.loads(d)
  img = d['data']['dyn_show_info']['bg_elem_cfg']['img_url']
  img_url = f'{_url}{img}'
  img2 = d['data']['dyn_show_info']['sprite_url']
  img2_url=f'{_url}{img2}'
  ss=d['sess']
  #url(&quot;https://turing.captcha.qcloud.com/cap_union_new_getcapbysig?img_index=1&image=02790500006d65550000000bb5e479283119&sess=s0gzziyxt4MLQWO80AXuudUjCRjS4ATiryCH_Wa_tYZo4R7R-T1HEGQZlEWVSv8XkmBcDKOMmZPSYtIC1hVBlr68EkidVacoUzVVFOHaz1mEwxPo0NmlMDrMOCn3DH6uP-dRv7EaRpJTkTOqhq70oiBLRiAdIBjGoNldKul-IU1RcYVE3eeOyqNowGJhahJk4Xt3fE2ei2FF2NzlPE47ZmXUiTWvdTd8rxOVh7m2WXOmmnRHG3Efa1KggafnWwSNFmpifOtm_aGr9DSVqO62-tlNmQR326UWAOiNPLjfUjNd89NrF9ABjC0gxrPVSwVso-AEbsXSSIsoWQHYyrulifYHWJ-2IUXxSVvdf06_FZFCGZhTR8lNHzpw**&quot;)
  # print(img2_url)
  body={'sess':ss,
    "eks": "0R6LuABzaUXix7aFJBH9YusrYPrvrECwnFkCcZsWlAeh5nBq7stHY2uSnZrRZr43hDkVgfQ62YwQ5R2lB8QTkIACAyww39z0af1mo+fRiBrharuL/PnPxh+wEgC+XuPmOGzLO/PGDElgi45q0pwn60cGyCINuGyNkgx7UiwSTVt0dHBVFHrGA7hvg23qyPxzbkDWUPm+1HEQDG8/MVorX9S7AGb48JZjTLYmOox329E=",
  }
  resp = client.post('https://turing.captcha.qcloud.com/cap_union_new_verify',files={'SlidingImage': img2_url,'BackImage':img_url},data=body).json()
  # ss=

  # data = {}
  # res_free = client.post('https://www.juliangip.com/users/getFree',)
  print(resp)
login()


#https://turing.captcha.qcloud.com

