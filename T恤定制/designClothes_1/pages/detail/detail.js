// pages/detail/detail.js
var app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    x: 20,
    y: 80,
    xz: 120,
    yz: 120,
    tempFilePath: null,
    num:1,
    hid:"true"
  },
  pushchose:function(){
    var hid = this.data.hid;
    if(hid){
      this.setData({hid:""})
    }
    else{
      this.setData({hid:"true"})
    }
    
  },
  /**
* 全部订单的跳转
*/
  detailadd: function (res) {
    wx.navigateTo({
      url: '../detailAdd/detailAdd',
    })
  },/************************************************* */
  buy:function(){
    wx.requestPayment({
      'timeStamp': '1490840662',
      'nonceStr': ' 	5K8264ILTKCH16CQ2502SI8ZNMTM67VS',
      'package': 'prepay_id=wx2017033010242291fcfe0db70013231072',
      'signType': 'MD5',
      'paySign': 'MD5(appId= wx2ed2ab5e74b37202&nonceStr=5K8264ILTKCH16CQ2502SI8ZNMTM67VS&package=prepay_id=wx2017033010242291fcfe0db70013231072&signType=MD5&timeStamp=1490840662&key=qazwsxedcrfvtgbyhnujmikolp111111) = 22D9B4E54AB1950F51E0649E8810ACD6',
      'success': function (res) {
        console.log(res)
      },
      'fail': function (res) {
        console.log(res)
      }
    })
  },
  minus:function(){
    var number = this.data.num;
    if(number>0){
      this.setData({ num: number - 1 });
    }
    else{
      this.setData({ num: 999 });
    }
    
  },
  add: function () {
    var number = this.data.num;
    if(number<999){
      this.setData({ num: number + 1 });
    }
    else{
      this.setData({num:0});
    }
    
  },
  setnum:function(res){
    console.log(res.detail.value)
    var number = res.detail.value;
    this.setData({num:number})
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(app)
    var data = app.globalData;
    var xp = data.x+230;
    this.setData({ x: xp, y: (data.y), xz: (data.xz/2), yz:( data.yz/2),
     tempFilePath: data.tempFilePath,a:data.a,b:data.b,c:data.c})
    console.log(this.data)
  
    var that = this;
    wx.getUserInfo({
      success: function (res) {

        var ur = res.userInfo.avatarUrl;
        console.log(ur)
        var nickName = res.userInfo.nickName;
        that.setData({ url: ur, name: nickName });
      },
    })
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