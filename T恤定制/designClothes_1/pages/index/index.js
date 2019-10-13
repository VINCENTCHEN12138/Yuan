var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    message:[
      {
        name: "T恤",
        value: ["女款17春 ", "男款17春", "女款16秋", "男款16秋", "女款莫代尔", "男款莫代尔"],
        color: ["白色", "灰色", "黑色", "橙色", "红色", "紫色"],
      },
      {
        name: "Polo衫",
        value: ["女款17春", "男款17春", "女款经典", "男款经典", "女款旗舰", "男款旗舰"],
        color: ["白色", "灰色", "黑色", "橙色", "红色", "紫色", "藏青色","墨绿色"],
      },
      
      
    ],
    indexs:0,
    chosedValue:null,
    borderchang:"hidden",
    hid:true,
    x:20,
    y:80,
    xz:120,
    yz:120,
    hidden:1,
    zhengfan:"pro",
    tempFilePath:"https://www.dexin365.com/static/txudingzhi201708/image/c_add.png",
    a:1,
    b:1,
    c:1,
  },
  /**
   * 点击隐藏显示
   */
  hidden_click:function(res){
    var hidden = this.data.hidden;
    console.log(this.data.hidden)
    if(hidden!=0){
      this.setData({hidden:0});
    }else{
      this.setData({ hidden: 1});
    }
  }, /*************************************************/
  /**
   * 选择图片
   */
  chosepic:function(){
    var that = this;
    wx.chooseImage({
      count: 1, 
      success: function(res) {
        console.log(res.tempFilePaths);
        var tempFilePaths = res.tempFilePaths;
        that.setData({ tempFilePath: tempFilePaths,
                        hid:null,
                        borderchang:"solid",
        });
      },
    })
  },/*********************************************** */
  /**
   * 改变背景图片的正反
   */
  changezhengfan:function(res){
    console.log(res.currentTarget.dataset.value);
    var num = res.currentTarget.dataset.value;
    if(num==0){
      
      this.setData({
        zhengfan: "pro",
        colors:["#4A4A4A", "#9B9B9B"],
        });
    }
    else{
      this.setData({ zhengfan: "con",
        colors: ["#9B9B9B", "#4A4A4A"],
         });
    }
    
  },/************************************************* */
  /***
   * 选择好的图片的关闭
   */
  butclose:function(res){
    console.log("close")
    var that = this;
    this.setData({ xz: 120, yz: 120 });
    that.setData({ tempFilePath: "../image/c_add.png",
                    hid:true,
                    borderchang: "hidden",

    });
  },/*************************************************** */
  /**
   * 素材按键的跳转
   */
  sucai:function(res){
    wx.navigateTo({
      url: '../logs/logs',
    })
  },/************************************************* */
  /**
   * 拖动事件
   *  *xp横坐标
   *  *yp纵坐标
   
  move:function(res){
    var xp = res.changedTouches[0].clientX-80;
    var yp = res.changedTouches[0].clientY-60;
    console.log(res.changedTouches[0]);
    this.setData({xz:xp,yz:yp});
  },*/
  /************************************************** */

  buttonClick1:function(res){
    console.log(res.currentTarget.dataset)
    var i = res.currentTarget.dataset.index;
    var indexs= this.data.indexs;
    if(i!=indexs){
      this.setData({ indexs: i ,valuecl:null,colorcl:null,a:((i+1))})
    }
    
  },
  buttonClick2: function (res) {
    console.log(res.currentTarget.dataset)
    var value = res.currentTarget.dataset.value;
    var i = res.currentTarget.dataset.index;
    this.setData({ valuecl: value, b: ((i + 1))})
  },
  buttonClick3: function (res) {
    console.log(res.currentTarget.dataset)
    var color = res.currentTarget.dataset.value;
    var i = res.currentTarget.dataset.index;
    var a = this.data.a;
    this.setData({ colorcl: color,c: (i + 1) })
    console.log(this.data.a)
  },
  /*********************************************** */
  /**
   * 完成定制按键
   */
  succe:function(res){
    var that=this;
    wx.showToast({
      title: '成功',
      success:function(res){
        console.log(res)
        console.log("提交")
        var data = app.globalData;
        data.x = that.data.x;
        data.y = that.data.y
        data.xz = that.data.xz;
        data.yz = that.data.yz;
        data.tempFilePath = that.data.tempFilePath;
        data.a = that.data.a;
        data.b = that.data.b;
        data.c = that.data.c;
        wx.navigateTo({
          url: '../detail/detail',
        })
      },
      fail:function(res){
        console.log("shibai")
      },
    })
  },/********************************************** */
  /**
   * 获得移动图片的坐标
   */
  mover:function(res){
    console.log("mover")
    var dx = res.changedTouches[0].clientX;
    var dy = res.changedTouches[0].clientY;
    console.log(res.changedTouches[0]);
    this.setData({x:dx,y:dy})
  },/******************************************** */
  /**
   * 缩放事件
   * 
   */
  butmove:function(res){
    console.log(res)
    var xp = res.changedTouches[0].pageX ;
    var yp = res.changedTouches[0].pageY ;
    console.log(res.changedTouches[0]);
    this.setData({ xz: xp, yz: yp });
  },
  /****************************************** */
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var dat = app.globalData.userInfo;
    
    console.log(app.globalData);
    wx.getUserInfo({
      success: function (res) {
        console.log(res)
        dat = res.userInfo;
        console.log(dat);
        
       /*
        var userInfo = res.userInfo
        var nickName = userInfo.nickName
        user = userInfo.avatarUrl
        var gender = userInfo.gender //性别 0：未知、1：男、2：女
        var province = userInfo.province
        var city = userInfo.city
        var country = userInfo.country
        console.log(user);
        console.log(app)
        */
      }
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
    var that = this;
    var tem = app.globalData.tempFilePath;
    if(tem==null){
      that.setData({ 
                      hid:true,
                      borderchang: "hidden",
                      
      });
    }else{
      that.setData({ tempFilePath: tem,
                      hid:null,
                      borderchang: "solid",
       });
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