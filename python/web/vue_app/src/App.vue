<template>
  <div>
    hello vue
    <input type="text" ref="mytext">
    <button @click="handleAdd">add</button>

    <ul>
      <li v-for="data in datalist" :key="data">
        {{ data }}
      </li>
    </ul>

    <navbar>
      <button @click="isShow=!isShow">click</button>
    </navbar>
    <sidebar v-show="isShow"></sidebar>
  </div>
</template>

<script>
import navbar from '@/components/navbar'
import sidebar from '@/components/sidebar'
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
  components: {
    navbar: navbar,
    sidebar: sidebar
  }
}
</script>

<style lang="scss">
ul {
  li {
    background: yellow
  }
}
</style>
