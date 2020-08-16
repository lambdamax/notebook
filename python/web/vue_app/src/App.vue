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
  </div>
</template>

<script>
export default {
  data() {
    return {
      datalist: []
    }
  },
  methods: {
    handleAdd() {
      this.datalist.push(this.$refs.mytext.value)
    }
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
