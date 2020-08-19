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
  }
}
</script>

<style scoped>

</style>
