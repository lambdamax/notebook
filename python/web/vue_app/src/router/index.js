import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Film from '@/views/Film'
import Detail from '@/views/detail'
import Comingsoon from '@/views/Film/Comingsoon'
import Nowplaying from '@/views/Film/Nowplaying'
import Cinema from '@/views/Cinema'
import Center from '@/views/Center'

Vue.use(VueRouter)

const routes = [
  {
    path: '/film',
    name: 'film',
    component: Film,
    children: [
      {
        path: 'nowplaying',
        name: 'nowplaying',
        component: Nowplaying
      },
      {
        path: 'comingsoon',
        name: 'comingsoon',
        component: Comingsoon
      },
      {
        path: '',
        redirect: '/film/nowplaying'
      }
    ]
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: Detail
  },
  {
    path: '/cinema',
    name: 'cinema',
    component: Cinema
  },
  {
    path: '/center',
    name: 'center',
    component: Center
  },
  {
    path: '*',
    name: 'redirect',
    redirect: '/film'
  }
]

const router = new VueRouter({
  // 非hash模式，没有#，会向后端发起请求
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

// 全局路由守卫
router.beforeEach((to, from, next) => {
  if (to.path === '/center') {
    alert('全局守卫')
  } else {
    next()
  }
})

export default router
