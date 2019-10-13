const {
  Url
} = require("../../utils/util")

const app = getApp()
// pages/Order/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show: false,
    id: '',
    text: ""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  onClose: function () {
    this.setData({
      show: false
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  /* 确认收货 */
  success: function (e) {
    let id = e.currentTarget.dataset.id
    let index = e.currentTarget.dataset.index
    wx.request({
      url: Url + "api/ChangeOrder?id=" + id + "&status=2",
      success: function (res) {
        this.data.items[index].status = 2
        this.setData({
          items: this.data.items
        })
        wx.navigateTo({
          url: "../../pages/Evaluate/index?id=" + id
        })

      }.bind(this)
    })







  },

  evaluate: function (e) {
    let id = e.currentTarget.dataset.id
    this.data.id = id
    wx.navigateTo({
      url: "../../pages/Evaluate/index?id=" + id
    })

  },
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    let userid = app.globalData.userid
    wx.request({
      url: Url + "api/get_Orders/?userid=" + userid,
      success: function (res) {

        this.setData({
          items: res.data.data
        })

      }.bind(this)
    })
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