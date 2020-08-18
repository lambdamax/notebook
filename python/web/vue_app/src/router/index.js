import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Film from '@/views/Film'
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
      }
    ]
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
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
