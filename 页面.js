function timestampToDate(timestamp) {
    // 创建一个新的Date对象
    var date = new Date(timestamp);

    // 获取日期的各个部分
    var year = date.getFullYear();
    var month = ("0" + (date.getMonth() + 1)).slice(-2); // 月份是从0开始的，所以需要加1
    var day = ("0" + date.getDate()).slice(-2);
    var hour = ("0" + date.getHours()).slice(-2);
    var minute = ("0" + date.getMinutes()).slice(-2);
    var second = ("0" + date.getSeconds()).slice(-2);

    // 返回格式化的日期字符串
    return year + "" + month + "" + day + "" + hour + "" + minute + "" + second;
}
var 北京时间=(Date.now())
log(timestampToDate(北京时间))

var temp = http.post("https://server.try8.cn/tool/cipher/aes/encrypt", {
    "encrypt_operation": "ecb",
    "encrypt_padding": "PKCS7",
    "encrypt_len": "256",
    "encrypt_key": "SFV2fb8D09jreH2Xdf4M0FGk5Di2DX2O",
    "encrypt_iv": "null",
    "encrypt_value": "exposureType=1&pageSize=20&pageIndex=1&ClientTime="+timestampToDate(北京时间),
    "encrypt_aad": ""
}, {
    "headers": {
        "Host": "server.try8.cn",
        "Connection": "keep-alive",
        "Content-Length": "217",
        "sec-ch-ua": "\"Chromium\";v=\"118\", \"Android WebView\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
        "sign": "eyJ1c2VyX2lkIjoiIiwidG9rZW4iOiIifQ==",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://try8.cn",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://try8.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
}).body.json();
var 加密=(temp.data.aes_encrypt);



var text="nS6Hp+98rvbD1w6+QnRlOFXw8KieYZZpU0DoR1JZtm9TfYKNTTLOZZvzqgiag/OBTGEctyzory0I\nyDu+X2p9ZOxyJabJUmFceF3AXwH31E0"


var temp = http.request("https://api.zzmdwl.cn/Tasks/Exposure/GetPageExposureList", {
    method: "POST",
    body:  加密,
    headers: {
      "channel": "jiandan",
        "pkgName": "com.cq.jdcover",
        "encryption": "1",
        "version": "3.0.0.8",
        "timeZoom": "GMT+08:00",
        "timeSpan": 北京时间,
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg2NzU2NDQsImV4cCI6MTcwODc2MjM0NCwiaWF0IjoxNzA4Njc1OTQ0fQ.kYcjKLus0bSlloRtXc8tMot7WqglSQmPnOeFW_Un6dU",
        "AchievementIds": "[27]",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Content-Length": "64",
        "Host": "api.zzmdwl.cn",
        "Connection": "Keep-Alive",
        "User-Agent": "http/3.12.13"
     }
}).body.json();
log(temp);


