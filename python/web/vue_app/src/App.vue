<template>
  <div>
    hello vue
    <input type="text" ref="mytext">
    <button @click="handleAdd">add</button>

    <ul>
      <li v-for="(data,index) in datalist" :key="index">
        {{ data }}
      </li>
    </ul>

    <navbar>
      <button @click="isShow=!isShow">click</button>
    </navbar>
    <sidebar v-show="isShow"></sidebar>
    <!--    路由容器-->
    <router-view></router-view>

    <tabbar v-show="$store.state.isTabbarShow"></tabbar>
  </div>
</template>

<script>
import navbar from '@/components/navbar'
import sidebar from '@/components/sidebar'
import tabbar from '@/components/tabbar'
import axios from 'axios'
// 全局组件
// import Vue from 'vue'
// Vue.component('navbar', navbar)
// Vue.component('sidebar', sidebar)

export default {
  data () {
    return {
      datalist: [],
      isShow: true
    }
  },
  methods: {
    handleAdd () {
      this.datalist.push(this.$refs.mytext.value)
    }
  },
  mounted () {
    axios.get('/ajax/movieOnInfoList?token=').then(res => {
      console.log(res.data)
    })
  },
  components: {
    navbar: navbar,
    sidebar: sidebar,
    tabbar: tabbar
  }
}
</script>

<style lang="scss" scoped>
ul {
  li {
    background: yellow
  }
}
</style>
