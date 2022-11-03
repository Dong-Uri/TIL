<template>
  <div id="list">
    <li @click="clickDetail">
      <img :src="video.snippet.thumbnails.medium.url" :alt="video.snippet.title" style="vertical-align:middle;margin-top:20px;">
      <span v-html="video.snippet.title" style="margin-top:20px;margin-left:18px;vertical-align:middle;"></span>
    </li>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    clickDetail: function () {
      this.$emit('click-detail', this.video)
    }
  },
}
</script>

<style>
#list {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: #2c3e50;
  }
</style>