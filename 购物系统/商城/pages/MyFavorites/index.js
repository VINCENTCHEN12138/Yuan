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
    wx.request({
      url: Url + "api/GetFavorites?userid=" + app.globalData.userid,
      success: function (res) {
        this.setData({
          items: res.data.gooods
        })
      }.bind(this)
    })
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },
  Buy: function (e) {
    let goodid = e.currentTarget.dataset.goodid
    wx.navigateTo({
      url: "../../pages/ShopInfo/index?goodid=" + goodid
    })
  },
  delete: function (e) {
    let index = e.currentTarget.dataset.index
    let goodid = e.currentTarget.dataset.goodid
    wx.request({
      url: Url + "api/DeleteFavorites?userid=" + app.globalData.userid + "&goodid=" + goodid,
      success: function (res) {
        this.data.items.splice(index, 1)
        this.setData({
          items: this.data.items
        })
      }.bind(this)
    })
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