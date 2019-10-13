//app.js
App({
  onLaunch: function() {
    //调用API从本地缓存中获取数据
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
  },


  globalData: {
    x: 20,
    y: 80,
    xz: 200,
    yz: 200,
    tempFilePath: "../image/c_add.png",
    userInfo: null,
    tempFilePath:null,
  }
})
