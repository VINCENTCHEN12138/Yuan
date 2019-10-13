// pages/user/user.js
var app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    url:null,
    name:null,
  },
  /**
 * 订单的跳转
 */
  myorder: function (res) {
    wx.navigateTo({
      url: '../myorder/myorder',
    })
  },
  myorderpay: function (res) {
    wx.navigateTo({
      url: '../myorderpay/myorderpay',
    })
  },
  myordersend: function (res) {
    wx.navigateTo({
      url: '../myordersend/myordersend',
    })
  },
  myordertake: function (res) {
    wx.navigateTo({
      url: '../myordertake/myordertake',
    })
  },/************************************************* */
  /**
   * 收货地址的跳转
   */
  addresslist: function (res) {
    wx.navigateTo({
      url: '../addresslist/addresslist',
    })
  },
  /************************************************* */
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