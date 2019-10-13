var app = getApp();
var index = require("../index/index");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tempFilePath: ["ku_1.png", "ku_2.png", "ku_3.png", "ku_4.png", "ku_5.png",]
  },
  picClick:function(res){
    console.log(res.currentTarget.dataset.value)
    var tem = res.currentTarget.dataset.value;
    
    app.globalData.tempFilePath=tem;
    console.log(app.globalData.tempFilePath);
    wx.navigateBack({
      
    })
  },

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