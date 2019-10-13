const {
  Url
} = require("../../utils/util")

const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show: false,
    address: app.globalData.address
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      userInfo: app.globalData.userInfo
    })

  },
  onClose: function () {
    this.setData({
      show: false
    })
  },
  confirm: function () {
    let openid = app.globalData.openid
    let newaddress = []
    this.data.address.map((e, index) => {
      if (e.value) {
        newaddress.push(e)
      }
      return e
    })
    let address = newaddress
    wx.request({
      url: Url + '/api/ChangeAddress',
      data: {
        openid: openid,
        address: address
      }
    })
    this.setData({
      show: false
    })
  },
  onChange: function (e) {

    let index = e.currentTarget.dataset.index
    this.data.address[index].value = e.detail
    this.setData({
      address: this.data.address
    })
  },
  openpopup: function () {
    this.setData({
      show: true
    })
  },
  delete: function (e) {
    let index = e.currentTarget.dataset.index
    this.data.address.splice(index, 1)
    let openid = app.globalData.openid
    wx.request({
      url: Url + '/api/ChangeAddress',
      data: {
        openid: openid,
        address: this.data.address
      }
    })

    this.setData({
      address: this.data.address
    })
  },
  add: function () {
    if (this.data.address === '') {
      this.data.address = []
    }

    this.data.address.push({
      value: ""
    })
    this.setData({
      address: this.data.address
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
    this.setData({
      address: app.globalData.address
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