// pages/buy/buy.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },
  buy:function(){
    wx.requestPayment(
      {
        'timeStamp': '1490840662',
        'nonceStr': '5K8264ILTKCH16CQ2502SI8ZNMTM67VS',
        'package': 'prepay_id=wx2017033010242291fcfe0db70013231072',
        'signType': 'MD5',
        'paySign': 'paySign = MD5(appId=wx7c6aec10bfe052ad&nonceStr=5K8264ILTKCH16CQ2502SI8ZNMTM67VS&package=prepay_id=wx2017033010242291fcfe0db70013231072&signType=MD5&timeStamp=1490840662&key=qazwsxedcrfvtgbyhnujmikolp111111) = 22D9B4E54AB1950F51E0649E8810ACD6',
        'success': function (res) {
          console.log(res)
         },
        'fail': function (res) { 
          console.log(res)
        },
        'complete': function (res) {
          console.log(res)
         }
      }) 
  },
  /* 微信支付 */
  wxpay: function () {
    var that = this
    //登陆获取code  
    wx.login({
      success: function (res) {
        console.log(res.code)
        //获取openid  
        that.getOpenId(res.code)
      }
    });
  },

  /* 获取openId */
  getOpenId: function (code) {
    var that = this
    wx.request({
      url: "https://api.weixin.qq.com/sns/jscode2session?appid=wxbd5a8270399d41d9&secret=d8aac26a5a9c16266d1a23851ebb7d9b&js_code=" + code + "&grant_type=authorization_code",
      method: 'GET',
      success: function (res) {
        //统一支付签名  
        var appid = '';//appid    
        var body = '';//商户名  
        var mch_id = '';//商户号    
        var nonce_str = that.randomString;//随机字符串，不长于32位。    
        var notify_url = '';//通知地址  
        var spbill_create_ip = '';//ip  
        // var total_fee = parseInt(that.data.wxPayMoney) * 100;  
        var total_fee = 100;
        var trade_type = "JSAPI";
        var key = '';
        var unifiedPayment = 'appid=' + appid + '&body=' + body + '&mch_id=' + mch_id + '&nonce_str=' + nonce_str + '¬ify_url=' + notify_url + '&openid=' + res.data.openid + '&out_trade_no=' + that.data.paySn + '&spbill_create_ip=' + spbill_create_ip + '&total_fee=' + total_fee + '&trade_type=' + trade_type + '&key=' + key
        var sign = MD5.MD5(unifiedPayment).toUpperCase()
        console.log(sign)

        //封装统一支付xml参数  
        var formData = "<xml>"
        formData += "<appid>" + appid + "</appid>"
        formData += "<body>" + body + "</body>"
        formData += "<mch_id>" + mch_id + "</mch_id>"
        formData += "<nonce_str>" + nonce_str + "</nonce_str>"
        formData += "<notify_url>" + notify_url + "</notify_url>"
        formData += "<openid>" + res.data.openid + "</openid>"
        formData += "<out_trade_no>" + that.data.paySn + "</out_trade_no>"
        formData += "<spbill_create_ip>" + spbill_create_ip + "</spbill_create_ip>"
        formData += "<total_fee>" + total_fee + "</total_fee>"
        formData += "<trade_type>" + trade_type + "</trade_type>"
        formData += "<sign>" + sign + "</sign>"
        formData += "</xml>"

        //统一支付  
        wx.request({
          url: 'https://api.mch.weixin.qq.com/pay/unifiedorder',
          method: 'POST',
          head: 'application/x-www-form-urlencoded',
          data: formData, // 设置请求的 header  
          success: function (res) {
            console.log(res.data)

            var result_code = that.getXMLNodeValue('result_code', res.data.toString("utf-8"))
            var resultCode = result_code.split('[')[2].split(']')[0]
            if (resultCode == 'FAIL') {
              var err_code_des = that.getXMLNodeValue('err_code_des', res.data.toString("utf-8"))
              var errDes = err_code_des.split('[')[2].split(']')[0]
              wx.navigateBack({
                delta: 1, // 回退前 delta(默认为1) 页面  
                success: function (res) {
                  wx.showToast({
                    title: errDes,
                    icon: 'success',
                    duration: 2000
                  })
                },

              })
            } else {
              //发起支付  
              var prepay_id = that.getXMLNodeValue('prepay_id', res.data.toString("utf-8"))
              var tmp = prepay_id.split('[')
              var tmp1 = tmp[2].split(']')
              //签名    
              var key = '';
              var appId = '';
              var timeStamp = that.createTimeStamp();
              var nonceStr = that.randomString();
              var stringSignTemp = "appId=&nonceStr=" + nonceStr + "&package=prepay_id=" + tmp1[0] + "&signType=MD5&timeStamp=" + timeStamp + "&key="
              var sign = MD5.MD5(stringSignTemp).toUpperCase()
              console.log(sign)
              var param = { "timeStamp": timeStamp, "package": 'prepay_id=' + tmp1[0], "paySign": sign, "signType": "MD5", "nonceStr": nonceStr }
              that.pay(param)
            }



          },

        })
      },
      fail: function () {
        // fail  
      },
      complete: function () {
        // complete  
      }
    })
  },
  /* 随机数 */
  randomString: function () {
    var chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';    /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
    var maxPos = chars.length;
    var pwd = '';
    for (var i = 0; i < 32; i++) {
      pwd += chars.charAt(Math.floor(Math.random() * maxPos));
    }
    return pwd;
  },
  /* 获取prepay_id */
  getXMLNodeValue: function (node_name, xml) {
    var tmp = xml.split("<" + node_name + ">")
    var _tmp = tmp[1].split("</" + node_name + ">")
    return _tmp[0]
  },

  /* 时间戳产生函数   */
  createTimeStamp: function () {
    return parseInt(new Date().getTime() / 1000) + ''
  },
  /* 支付   */
  pay: function (param) {
    wx.requestPayment({
      timeStamp: param.timeStamp,
      nonceStr: param.nonceStr,
      package: param.package,
      signType: param.signType,
      paySign: param.paySign,
      success: function (res) {
        // success  
        console.log(res)
        wx.navigateBack({
          delta: 1, // 回退前 delta(默认为1) 页面  
          success: function (res) {
            wx.showToast({
              title: '支付成功',
              icon: 'success',
              duration: 2000
            })
          },
          fail: function () {
            // fail  
          },
          complete: function () {
            // complete  
          }
        })
      },
      fail: function () {
        // fail  
        console.log("支付失败")
      },
      complete: function () {
        // complete  
        console.log("pay complete")
      }
    })
  } ,

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})