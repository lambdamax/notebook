<template>
  <div>
    Detail
    <input type="text" v-model="val">
  </div>
</template>

<script>
import axios from 'axios'
// import Vue from 'vue'
export default {
  name: 'Detail',
  data () {
    return {
      val: ''
    }
  },
  props: ['id'],
  mounted () {
    console.log(this.$route)
    this.val = this.$route.params.id
    axios({
      url: `https://m.maizuo.com/gateway?filmId=${this.id}&k=4359832`,
      headers: {
        'X-Client-Info': '{"a": "3000", "ch": "1002", "v": "5.0.4", "e": "1597846521655347584860161", "bc": "310100"}',
        'X-Host': 'mall.film-ticket.film.list'
      }
    }).then(res => {
      console.log(res)
    })
  }
}
</script>

<style scoped>

</style>
