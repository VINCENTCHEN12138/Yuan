const {
  Url
} = require("../../utils/util")

const app = getApp()
// pages/My/index.js
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
    this.data.goodid = options.goodid
    wx.request({
      url: Url + "api/get_Goods?goodid=" + options.goodid,
      success: function (res) {
        this.setData({
          item: res.data.data
        })
      }.bind(this)
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },
  onClickButton: function (e) {
    switch (e.currentTarget.dataset.tag) {
      case "buy":
        wx.navigateTo({
          url: "../../pages/BuyShop/index?goodid=" + this.data.goodid
        })
        break;
      case "fav":
        wx.request({
          url: Url + "api/AddFavorites?userid=" + app.globalData.userid + "&goodid=" + this.data.goodid,
          success: function (res) {
            wx.showModal({
              title: '提示',
              content: '成功',
              success(res) {
                if (res.confirm) {} else if (res.cancel) {}
              }
            })
          }
        })
        break;
      case "addcart":

        wx.request({
          url: Url + "api/add_Shoppingcart/",
          method: 'POST',
          header: {
            "Content-type": "application/x-www-form-urlencoded"
          },
          data: {
            goodsid: this.data.goodid,
            userid: app.globalData.userid,
            amount: 1
          },
          success: function (data) {
            wx.showModal({
              title: '提示',
              content: '成功',
              success(res) {
                if (res.confirm) {} else if (res.cancel) {}
              }
            })
          }
        })
        break;
    }
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