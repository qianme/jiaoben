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
var 北京时间 = (Date.now())
// log(timestampToDate(北京时间))

///密码的key=q7LxfQk7EBcaJIWB5QzE85vekGJP7FXa
//密码要求url编码
var 账号="13194929316"
var 密码="my123456"
// log(encodeURIComponent(加密("q7LxfQk7EBcaJIWB5QzE85vekGJP7FXa",密码)))
//Ut0eaqXR1i3%2FaPRmeV3Thg%3D%3D
//Ut0eaqXR1i3%2FaPRmeV3Thg%3D%3D

var 算法 = '{"account":"17570891156","deviceId":"262f4677ade11232","password":"'+encodeURIComponent(加密("q7LxfQk7EBcaJIWB5QzE85vekGJP7FXa",密码))+'%0A","ClientTime":' + timestampToDate(北京时间) + '}'
log(算法)



var temp = http.request("https://api.zzmdwl.cn/SysBase/Account/SingInNormal", {
    method: "POST",
    body: 加密("SFV2fb8D09jreH2Xdf4M0FGk5Di2DX2O",算法),
    headers: {
        "channel": "jiandan",
        "pkgName": "com.cq.jdcover",
        "encryption": "1",
        "timeZoom": "GMT+08:00",
        "timeSpan": 北京时间,
    }
}).body.json();
log(temp);






function 加密(key, 内容) {
    var temp = http.post("https://server.try8.cn/tool/cipher/aes/encrypt", {
        "encrypt_operation": "ecb",
        "encrypt_padding": "PKCS7",
        "encrypt_len": "256",
        "encrypt_key": key,
        "encrypt_iv": "null",
        "encrypt_value": 内容,
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
    var 加密 = (temp.data.aes_encrypt);
    return 加密


}