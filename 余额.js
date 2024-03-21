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
    "encrypt_value": "cashOutType=0&ClientTime="+timestampToDate(北京时间),
    "encrypt_aad": ""
}, {
    "headers": {
        "sign": "eyJ1c2VyX2lkIjoiIiwidG9rZW4iOiIifQ==",
       }
}).body.json();
var 加密=(temp.data.aes_encrypt);


var temp = http.get("https://api.woaizhuanqian9.cn/SysBase/User/GetUserCashOutBasicInfo?KSystemWork="+加密, {
    "headers": {
        "encryption": "1",
        "timeSpan": 北京时间,
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoi5riF6aOOIiwiSWQiOiIxNDcxNTE5IiwiQWNjb3VudCI6IjE3NTcwODkxMTU2IiwiQXBwVXNlclJvbGVUeXBlIjoiMSIsIklzU2RrU2VydmljZSI6IjAiLCJuYmYiOjE3MDg3NjM2NDMsImV4cCI6MTcwODg1MDM0MywiaWF0IjoxNzA4NzYzOTQzfQ.HDo045jpJHtpD6d8w6uWVWN4VrC_xQ_eebU3Uz51_ss",
    }
}).body.json();
if(temp.StateCode==200){
    log(temp.InnerData.Commission)
}