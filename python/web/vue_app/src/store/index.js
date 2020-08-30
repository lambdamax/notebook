import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 自定义共享状态
    isTabbarShow: true
  },
  mutations: {
    // 唯一可以修改状态的位置，用于监控
    HideTabbar (state, data) {
      console.log('HideTabbar')
      state.isTabbarShow = data
    },
    ShowTabbar (state, data) {
      console.log('ShowTabbar')
      state.isTabbarShow = data
    }
  },
  actions: {},
  modules: {}
})
