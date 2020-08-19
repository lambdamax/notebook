<template>
  <div>
    Nowplaying
    <ul>
      <li v-for="data in datalist" :key="data.filmId" @click="handleClick(data.filmId)">{{ data.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

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

<style scoped>

</style>
