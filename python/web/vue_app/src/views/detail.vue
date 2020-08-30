<template>
  <div>
    Detail
    <input type="text" v-model="val">
  </div>
</template>

<script>
export default {
  name: 'Detail',
  data () {
    return {
      val: ''
    }
  },
  mounted () {
    console.log(this.$route)
    this.val = this.$route.params.id
    this.$store.commit('HideTabbar', false)
  },
  beforeDestroy () {
    this.$store.commit('ShowTabbar', true)
  }
}
</script>

<style scoped>

</style>
