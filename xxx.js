const axios = require('axios')

var bearer = "090a0b8582592fffc5ed414a3a68e9729702283b-00fd-4add-8890-a1be34df27a5"
var Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NWY5MzEwM2NiYzRlMmMxY2Y2MWQyY2QiLCJleHAiOjE3MTEzOTMyMDAsImlzcyI6Im1hcnZlbG91cy1vY2VhbiJ9.dgyywFdorIjYICxBKdxQK4YKtgcgK37qvpd4mlU1t4E"
var device = "20e2fdf35f949335892664fa86fecde92"
var bxsign = "Ss0Wvt5pRGVX84/4BQM9tpUqPBuAgd4QZmyhTHa1IWzziAfM4uPA5mWlw+UMVKS+dmp6E6tn25ViF0Z7C39cstyumB/8LSCAOlMWUn03otz1IQcQe2aNyjOdZLCzHrgLqB4GygaHLu6PVnuF6oCh2yIAhgQaQ/DoGbcKAVF0ud0="


user(device, Authorization)

function user(device, Authorization) {//主函数

    axios.get("https://gm.total123.cn/api/mine/info", {
        "headers": {
            "device-id": device,
            "Authorization": Authorization,
            "Host": "gm.total123.cn",
            "Connection": "Keep-Alive",
            "User-Agent": "http/4.9.3"
        }
    }).then(async function (res) {
        var data = (res.data.data.mine_task_list)
        console.log("目前有 " + data.length + " 个矿石")
        for (let i = 0; i < data.length; i++) {
            if (data[i].mine_type_text == "钻石") {
                const delay = getRandomDelay(30000, 35000);
                console.log(`等待 ${delay} 毫秒...`);
                await sleep(delay)
            } else {
                const delay = getRandomDelay(10000, 15000);
                console.log(`等待 ${delay} 毫秒...`);
                await sleep(delay)
            }
            var id = (data[i].mine_id)
            console.log("ID:" + id)
            // 使用示例

            fetchData(id, device, Authorization)//挖矿
            Treasure_chests(id, device, Authorization, bxsign, bearer)
            mon()

        }
    })


}
//----------------------------------------余额
function mon() {
    axios.get("https://flsdk.total123.cn/api/withdrawal/percent", {
        "headers": {
            "sign": "rIxoNSqO9ByXoNWtPLDZQydq1brwHwaL8dCAkV0JjMbYA+bMA9vgmS35Lxc+9RupXE0FsgtmCiaSviZSrckF8Se2nPBn16w1cdaysFnBh6/oN6n6YuHx26F5jcMDPd3JQ/12m+MgaWIjWKW812v4lDGMefsHVUYUevvFNjcBiRA=",
            "pkg": "com.heliangtec.gm",
            "appid": "FL_dd15r476766c",
            "profile": "release",
            "channel": "web",
            "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
            "version-code": "3",
            "ts": "1710697254561",
            "sdkVersionCode": "2",
            "bearer": "f62221144c0277e6a6689957d2d7f3a7fdc2b677-1190-45dc-ba7d-a96216108cbd",
            "Host": "flsdk.total123.cn",
            "Connection": "Keep-Alive",
            "User-Agent": "http/4.9.3"
        }
    }).then(function (res) {
        console.log("账号余额 :" + res.data.data.balance_text + " | 提现比例: " + res.data.data.withdraw_percent_text + " | 提现金额 : " + res.data.data.pre_withdraw_text);
    })
}


//----------------------------------------宝箱
function Treasure_chests(id, device, Authorization, bxsign, bearer) {
    axios.post("https://flsdk.total123.cn/api/task/finishAndReceive", {
        "id": "65c1f9dd71f62183cd32d419"
    }, {
        "headers": {
            "sign": bxsign,
            "pkg": "com.heliangtec.gm",
            "appid": "FL_dd15r476766c",
            "profile": "release",
            "channel": "web",
            "device-id": device,
            "version-code": "3",
            "ts": "1710695843072",
            "sdkVersionCode": "2",
            "bearer": bearer,
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "33",
            "Host": "flsdk.total123.cn",
            "Connection": "Keep-Alive",
            "User-Agent": "http/4.9.3"

        }
    }).then(function (res) {
        if (res.data.code == 200) {
            console.log(res.data.data.describe);
        } else {
            console.log(res.data.msg);

        }

    })
}


//----------------------------------------挖矿
function fetchData(id, device, Authorization) {
    axios.post("https://gm.total123.cn/api/mine/get", {
        "id": id
    }, {
        "headers": {
            "device-id": device,
            "Authorization": Authorization,
            "Host": "gm.total123.cn",
            "Connection": "Keep-Alive",
            "User-Agent": "http/4.9.3"
        }
    }).then(function (res) {
        console.log(res.data)
    })
}


// ---------------------------------------延迟
function getRandomDelay(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}