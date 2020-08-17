<template>
  <div>
    sidebar
    <ul>
      <li v-for="data in datalist" :key="data">
        {{ data }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'sidebar',
  data () {
    return {
      datalist: ['111', '222', '333']
    }
  }
}
</script>

<!--scoped表示改style的作用域-->
<style lang="scss" scoped>
ul {
  li {
    background: blue;
  }
}
</style>
