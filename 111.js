const axios = require('axios');


const Cookie='PHPSESSID=7b0rav1l0aihealq58r3o386h7; udtauth3=f879Vp7MdFeOgBvlw4rKZ7x%2FEsG55%2B2BLUgqXsaBsmXHS0wlf5SRxK4dafdIsPa5xNXkXPeqDWiUJcSHGZtWjEBBVAEzPb%2BtaLb5VxaNck2QX4mTJkHli%2B9zB2x9ujQsabOAqlD%2BQ5FM6KV3001TPu2AdpyEL4Snl%2BiJU4XX4Dc'
axios.get('url=\'http://m365729.xedi8rkn.shop/tuijian',{'headers':{
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2c) NetType/4G Language/zh_CN",
        "Cookie": Cookie,
    }})
  .then(function (response) {
    // 处理成功情况
    console.log(response.data);})
  // })
  // .catch(function (error) {
  //   // 处理错误情况
  //   console.log(error);
  // })
  // .then(function () {
  //   // 总是会执行
  // });


for (var a = 0; a < 2; i++) {




    var temp = http.get("https://gm.total123.cn/api/mine/info", {
        "headers": {
            "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NWY3MjU1MmY1NDcwZjNjMzgwNTRlYjAiLCJleHAiOjE3MTEzMDY4MDAsImlzcyI6Im1hcnZlbG91cy1vY2VhbiJ9.iUU4uA_JPRAuR-oNMchGx6TDJ6oQ53bGLY3JMH7n8Uo",
            "Host": "gm.total123.cn",
            "Connection": "Keep-Alive",
            "User-Agent": "http/4.9.3"
        }
    }).body.json();
    var data = (temp.data.mine_task_list);
    log(data.length)
    for (var i = 0; i < data.length; i++) {
        if (data[i].mine_type_text == "钻石") {
            sleep(30000)
        } else {
            sleep(10000)
        }
        var id = (data[i].mine_id)
        log("ID:" + id)
        var temp = http.postJson("https://gm.total123.cn/api/mine/get", {
            "id": id
        }, {
            "headers": {
                "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NWY3MjU1MmY1NDcwZjNjMzgwNTRlYjAiLCJleHAiOjE3MTEzMDY4MDAsImlzcyI6Im1hcnZlbG91cy1vY2VhbiJ9.iUU4uA_JPRAuR-oNMchGx6TDJ6oQ53bGLY3JMH7n8Uo",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "24",
                "Host": "gm.total123.cn",
                "Connection": "Keep-Alive",
                "User-Agent": "http/4.9.3"
            }
        }).body.json();
        log(temp);
        var temp = http.postJson("https://flsdk.total123.cn/api/task/finishAndReceive", {
            "id": "65c1f9dd71f62183cd32d419"
        }, {
            "headers": {
                "sign": "EexVAtjjo9kYOqYYnYAtWZFB07rXKtcdkaC+XStQy1L5n3IdGFEH1BtghYLJs7+oIP+/0TnWVgWsmr7Se8zIGXyGoEG5Srbs6hD0Ow0G16fa7oEkZKB/qmiBrJf1le7br2gMCaQZUuQn5LdWg5Eqjibj7TRjgfo8Z6atgCOocJE=",
                "pkg": "com.heliangtec.gm",
                "appid": "FL_dd15r476766c",
                "profile": "release",
                "channel": "web",
                "device-id": "2df8e77516eba37aea41d7239e7f8b6d8",
                "version-code": "3",
                "ts": "1710695843072",
                "sdkVersionCode": "2",
                "bearer": "f62221144c0277e6a6689957d2d7f3a7fdc2b677-1190-45dc-ba7d-a96216108cbd",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "33",
                "Host": "flsdk.total123.cn",
                "Connection": "Keep-Alive",
                "User-Agent": "http/4.9.3"
            }
        }).body.json();
        log(temp)
        if (temp.code == 200) {
            log(temp.data.describe);
        } else {
            log(temp.msg);

        }
        var temp = http.get("https://flsdk.total123.cn/api/withdrawal/percent", {
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
        }).body.json();
        log("账号余额 :" + temp.data.balance_text + " | 提现比例: " + temp.data.withdraw_percent_text + " | 提现金额 : " + temp.data.pre_withdraw_text);
    }
}
