<template>
  <div>
    Nowplaying
    <ul>
      <li v-for="data in datalist" :key="data.filmId" @click="handleClick(data.filmId)">
        <img :src="data.poster" :alt="data.name">
        <p>{{ data.name }}</p>
        <p>观众评分：{{ data.grade }}</p>
        <p>主演：{{ data.actors | actorfilter }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

Vue.filter('actorfilter', function (data) {
  return data.map(item => item.name).join(' ')
})

export default {
  name: 'Nowplaying',
  data () {
    return {
      datalist: []
    }
  },
  mounted () {
    axios({
      url: 'https://m.maizuo.com/gateway?cityId=310100&pageNum=1&pageSize=10&type=1&k=2748784',
      headers: {
        'X-Client-Info': '{"a": "3000", "ch": "1002", "v": "5.0.4", "e": "1597846521655347584860161", "bc": "310100"}',
        'X-Host': 'mall.film-ticket.film.list'
      }
    }).then(res => {
      console.log(res)
      this.datalist = res.data.data.films
    })
  },
  beforeDestroy () {
    // 解绑事件
  },
  methods: {
    handleClick (id) {
      // console.log(id)
      // 编程式导航``
      // this.$router.push(`/detail/${id}`)
      // 编程式导航-名字跳转
      this.$router.push({ name: 'detail', params: { id: id } })
    }
  }
}
</script>

<style lang="scss" scoped>
ul {
  li {
    overflow: hidden;

    img {
      float: left;
    }
  }
}
</style>
