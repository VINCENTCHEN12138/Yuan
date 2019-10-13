const {
  Url
} = require("../../utils/util")
const app = getApp()
// pages/BuyShop/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    radio: 0,
    num: "1"
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.data.goodid = options.goodid
    this.data.userid = app.globalData.userid
    wx.request({
      url: Url + "api/get_Goods?goodid=" + options.goodid,
      success: function (res) {

        this.setData({
          item: res.data.data,
          address: app.globalData.address
        })

      }.bind(this)
    })
  },
  onSubmit: function () {
    let address = this.data.address[this.data.radio].value
    let userid = app.globalData.userid
    let goodid = this.data.goodid
    let amount = this.data.num
    let ordernum = Number(Math.round(Math.random() * 10))
    wx.request({
      url: Url + "api/add_Orders/",
      method: "POST",
      data: {
        userid: userid,
        goodsid: goodid,
        amount: amount,
        ordernum: ordernum,
        status: 1,
        addressid: address,
        expressidnum: 1
      },
      header: {
        "Content-type": "application/x-www-form-urlencoded"
      },
      success: function (res) {
        wx.showModal({
          title: '提示',
          content: '成功',
          success: function (res) {
            if (res.confirm) {
              wx.navigateBack()
            } else if (res.cancel) {
              console.log('用户点击取消')
            }
          }
        })

      }
    })


  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onClick: function (e) {
    let name = e.currentTarget.dataset.name
    this.setData({
      radio: name
    })
  },
  onChange: function (e) {
    this.setData({
      radio: e.detail
    })
  },
  onReady: function () {

  },
  onChange2: function (e) {
    this.setData({
      num: e.detail
    })
  },
  /**
   * 生命周期函数--监听页面显示
   */
  addaddress: function () {
    wx.switchTab({
      url: "../../pages/My/index?tag=add"
    })
  },
  onShow: function () {
    wx.request({
      url: Url + "api/get_Goods?goodid=" + this.data.goodid,
      success: function (res) {

        this.setData({
          item: res.data.data,
          address: app.globalData.address
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