// pages/Evaluate/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    text: ""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.data.id = options.id
  },

  change: function (e) {
    this.setData({
      text: e.detail
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
  success: function () {
    let orderid = this.data.orderid
    let text = this.data.text
    if (this.data.text) {
      wx.request({
        url: "http://127.0.0.1:8000/api/ChangeOrder?id=" + this.data.id + "&status=3",
        success: function (res) {
          wx.request({
            url: "http://127.0.0.1:8000/api/AddEvaluate?orderid=" + orderid + "&text=" + text,
            success: function (res) {
              wx.switchTab({
                url: "../../pages/Index/index"
              })
            }
          })
        }
      })

    }

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