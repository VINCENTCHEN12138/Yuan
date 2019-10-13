const {
  Url
} = require("../../utils/util")

const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: Url + "api/get_Shoppingcart/?userid=" + app.globalData.userid,
      success: function (res) {
        this.setData({
          items: res.data.data
        })
      }.bind(this)
    })
  },
  delete: function (e) {
    let id = e.currentTarget.dataset.id
    let index = e.currentTarget.dataset.index
    wx.request({
      url: Url + "api/delete_Shoppingcart/",
      method: "POST",
      data: {
        id: id
      },
      header: {
        "Content-type": "application/x-www-form-urlencoded"
      },
      success: function () {
        this.data.items.splice(index, 1)
        this.setData({
          items: this.data.items
        })
      }.bind(this)
    })
  },

  Getdata: function () {
    wx.request({
      url: Url + "api/get_Shoppingcart/?userid=" + app.globalData.userid,
      success: function (res) {
        this.setData({
          items: res.data.data
        })
      }.bind(this)
    })
  },
  onReady: function () {

  },
  Buy: function (e) {
    let goodid = e.currentTarget.dataset.goodid

    wx.navigateTo({
      url: "../../pages/ShopInfo/index?goodid=" + goodid
    })
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    this.Getdata()
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