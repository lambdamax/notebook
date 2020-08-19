<template>
  <nav>
    声明式导航
    <ul>
      <router-link :to="'/'+data" tag="li" active-class="myactive"
                   v-for="(data,index) in datalist" :key="index">
        <i class="mui-icon mui-icon-plus"></i>
        {{ data }}
      </router-link>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'tabbar',
  data () {
    return {
      datalist: ['film', 'cinema', 'center']
    }
  }
}
</script>

<style scoped>
.myactive {
  color: red;
}
</style>
