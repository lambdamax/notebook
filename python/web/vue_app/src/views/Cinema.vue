<template>
  <div>
    Cinema
  </div>
</template>

<script>
export default {
  name: 'Cinema',
  beforeRouteEnter (to, from, next) {
    alert('局部守卫')
  }
}
</script>

<style scoped>

</style>
