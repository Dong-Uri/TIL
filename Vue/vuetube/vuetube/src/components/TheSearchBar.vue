<template>
  <div>
    <input type="text" @keyup.enter="onInputKeyword" v-model="search">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data: function () {
    return {
      search: null,
    }
  },
  methods: {
    onInputKeyword(event) {
      this.$emit('input-change', event.target.value)
      this.search = null
    }
  }
}
</script>

<style>

</style>