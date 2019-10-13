// pages/detailAdd/detailAdd.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },
  buy: function () {
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
  /**
     * 创建收货地址的跳转
     */
  addressnew: function (res) {
    wx.navigateTo({
      url: '../addressnew/addressnew',
    })
  },/************************************************* */
  /**
     * 地址管理的跳转
     */
  addresslist: function (res) {
    wx.navigateTo({
      url: '../addresslist/addresslist',
    })
  },/************************************************* */
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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