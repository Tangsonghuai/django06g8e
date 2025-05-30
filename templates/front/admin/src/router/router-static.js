import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import yonghushangpin from '@/views/modules/yonghushangpin/list'
    import shangpinxinxi from '@/views/modules/shangpinxinxi/list'
    import storeup from '@/views/modules/storeup/list'
    import discusshuodongshangpin from '@/views/modules/discusshuodongshangpin/list'
    import discussyonghushangpin from '@/views/modules/discussyonghushangpin/list'
    import tousufankui from '@/views/modules/tousufankui/list'
    import shangpinfenlei from '@/views/modules/shangpinfenlei/list'
    import yonghu from '@/views/modules/yonghu/list'
    import chat from '@/views/modules/chat/list'
    import discussshangpinxinxi from '@/views/modules/discussshangpinxinxi/list'
    import orders from '@/views/modules/orders/list'
    import tuihuohuanhuo from '@/views/modules/tuihuohuanhuo/list'
    import discussgonggaoxinxi from '@/views/modules/discussgonggaoxinxi/list'
    import gonggaoxinxi from '@/views/modules/gonggaoxinxi/list'
    import config from '@/views/modules/config/list'
    import huodongshangpin from '@/views/modules/huodongshangpin/list'


//2.配置路由   注意：名字
const routes = [{
    path: '/index',
    name: '首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '首页',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '新闻资讯',
        component: news
      }
      ,{
	path: '/yonghushangpin',
        name: '用户商品',
        component: yonghushangpin
      }
      ,{
	path: '/shangpinxinxi',
        name: '商品信息',
        component: shangpinxinxi
      }
      ,{
	path: '/storeup',
        name: '我的收藏',
        component: storeup
      }
      ,{
	path: '/discusshuodongshangpin',
        name: '活动商品评论',
        component: discusshuodongshangpin
      }
      ,{
	path: '/discussyonghushangpin',
        name: '用户商品评论',
        component: discussyonghushangpin
      }
      ,{
	path: '/tousufankui',
        name: '投诉反馈',
        component: tousufankui
      }
      ,{
	path: '/shangpinfenlei',
        name: '商品分类',
        component: shangpinfenlei
      }
      ,{
	path: '/yonghu',
        name: '用户',
        component: yonghu
      }
      ,{
	path: '/chat',
        name: '客服管理',
        component: chat
      }
      ,{
	path: '/discussshangpinxinxi',
        name: '商品信息评论',
        component: discussshangpinxinxi
      }
      ,{
        path: '/orders/:status',
        name: '订单管理',
        component: orders
      }
      ,{
	path: '/tuihuohuanhuo',
        name: '退货换货',
        component: tuihuohuanhuo
      }
      ,{
	path: '/discussgonggaoxinxi',
        name: '公告信息评论',
        component: discussgonggaoxinxi
      }
      ,{
	path: '/gonggaoxinxi',
        name: '公告信息',
        component: gonggaoxinxi
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/huodongshangpin',
        name: '活动商品',
        component: huodongshangpin
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: '首页',
    redirect: '/index'
  }, /*默认跳转路由*/
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'history',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})

export default router;
