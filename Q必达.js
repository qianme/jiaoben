const axios=require('axios')
// const sleep=require("sleep")


//Q必达入口：weixin://dl/business/?t=4bqyf17I6Fk
//抓包数据为：token的值，变量名为：QBD

https://github.com/qianme/jiaoben.git

const now=Date.now()

const tokens=process.env.QBD
const list=tokens.split('&')
for (var i=0;i<list.length;i++){
    var token=(list[i])
    sign(token,i)
}

//随机数
function getRandomDelay(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// //延迟
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function sign(token,){      //签到
    axios.post(`https://xcx.wanhuida888.com/ht/web/mine/signIn?t=${now}`,{},{
        'headers':{
    "host": "xcx.wanhuida888.com",
    "content-length": "2",
    "content-type": "application/json",
    "xweb_xhr": "1",
    "appid": "wx92e73ad679eee047",
    "source": "MINIAPP",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "token": token,
    "version": "108",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx92e73ad679eee047/72/page-frame.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9"
}
    }).then(async function (res){
        if (res.data.code==0){
            const deley=getRandomDelay(30000,35000);
            console.log(`第${i}个账号，签到任务：${res.data.msg}!!!,本次获得${res.data.data}积分`);
            await sleep(deley)
             WatchVideo(token,i)
        }else {
            const deley=getRandomDelay(10000,15000)
            console.log(`第${i}个账号，今日签到任务：${res.data.msg}`)
            await sleep(deley)
             WatchVideo(token,i)
        }

    })
}


function WatchVideo(token,i){      //签到看视频翻倍
    axios.post(`https://xcx.wanhuida888.com/ht/web/mine/doublePoint?t=${now}`,{},{
        'headers':{
    "host": "xcx.wanhuida888.com",
    "content-length": "2",
    "content-type": "application/json",
    "xweb_xhr": "1",
    "appid": "wx92e73ad679eee047",
    "source": "MINIAPP",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "token": token,
    "version": "108",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx92e73ad679eee047/72/page-frame.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9"
}
    }).then(async function (res){
        if (res.data.code == 0){
            const deley=getRandomDelay(30000,35000)
           console.log(`第${i}个账号，签到翻倍任务：${res.data.msg}！！,本次获得${res.data.data}积分`)
            await sleep(deley)
             WatchVideo(token,i)
        }else {
            const deley=getRandomDelay(10000,15000)
            console.log(`第${i}个账号，签到翻倍任务：${res.data.msg}`)
            await sleep(deley)
            video(token,i)
        }
    })
}


function video(token,i){    //看视频
    axios.post(`https://xcx.wanhuida888.com/ht/web/task/watchVideo?t=${now}`,{},{
        'headers':{
    "Host": "xcx.wanhuida888.com",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "charset": "utf-8",
    "sharecode": "8MFG4AH",
    "appid": "wx92e73ad679eee047",
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; LE2110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/3669 MicroMessenger/8.0.47.2560(0x28002F3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/json",
    "source": "MINIAPP",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "version": "108",
    "token": token,
    "Referer": "https://servicewechat.com/wx92e73ad679eee047/72/page-frame.html"
}
    }).then(async function (res){
        if (res.data.code == 0){
            const deley=getRandomDelay(30000,35000)
           console.log(`第${i}个账号，看视频任务：${res.data.msg}！！！,本次获得${res.data.data}积分`)
            await sleep(deley)
        }else {
            const deley=getRandomDelay(10000,15000)
            console.log(`第${i}个账号，看视频任务：${res.data.msg}`)
            await sleep(deley)
        }
        console.log(`任务已经完成，退出脚本，下次见~`)
    })
}




