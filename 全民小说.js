const axios=require('axios')


// 获取当前时间戳（毫秒）
const timestamp = Date.now();

// 将时间戳转换为10位数
const t = Math.floor(timestamp / 1000);

// const data=JSON.stringify({'type':'day','finish_ad_ids':'1526',"_t":`${t}`,"_c":'50719'})
function ii(){
    axios.post('https://www.duokan.com/soushu/user/award/vip/info',{'type':'day','finish_ad_ids':1526,"_t":t,"_c":50719},{
       'headers':{
    "host": "www.duokan.com",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": `mi_version=V12.5.2.0.QEACNXM;_m=1;platform=android;app_id=DkFree;build=730050000;channel=Y6WBAG;first_version=730050000;version_name=7.30.5;device_model=MI%208;device_name=dipper;os_version=10;os_sdk=29;manufacturer=Xiaomi;random_id=de4391639fb66e0ad0415a3d5a6cf49c;reg_id=IHzbd5i1K87wt%2BBHTmvaCdCmMbzb5Z88OG01twpNhLF82Ta8jUHuSEJS%2BpVnnqk%2F;personalise_rec=1;store_pref=;user_type=0;fiction_level=0_1;_t=${t};_c=50719;p=DK105de4391639fb66e0ad0415a3d5a6cf49c;token=DECPiv7mAF5WJpza6At0_pLEk0U9PJLl3lg-BS7sxu8jV08GJgQ6E2UXewej435cF3AJeMRo88GEj79A8ykKTCyiaIo2hgtOWho57djvwco.;`,
    "accept-encoding": "gzip,deflate",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; MI 8 MIUI/V12.5.2.0.QEACNXM)",
    "content-length": "50"
}
    }).then(function (res){
        console.log(res.data)
    })
}
ii()

// const http2 = require('http2');
//
// const client = http2.connect('https://www.duokan.com/soushu/user/award/vip/info');
//
// const req = client.request({
//   ':path': '/your/post/endpoint',
//   ':method': 'POST',
//   'content-type': 'application/json' // 设置请求头
// });
//
// let postData = JSON.stringify({ 'type':'day','finish_ad_ids':'1526',"_t":`${t}`,"_c":'50719'}); // 构造要发送的数据
// req.write(postData); // 将数据写入请求
//
// req.on('response', (headers, flags) => {
//   // 监听响应头
//   console.log(headers);
// });
//
// let responseData = '';
// req.on('data', (chunk) => {
//   responseData += chunk;
// });
//
// req.on('end', () => {
//   // 监听请求结束
//   console.log(responseData);
//   client.close();
// });
//
// req.on('error', (err) => {
//   // 监听请求错误
//   console.error(err);
// });
//
// req.end(); // 结束请求