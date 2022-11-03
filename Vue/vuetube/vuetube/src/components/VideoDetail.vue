<template>
  <div>
    <iframe width="800" height="450" :src="'https://www.youtube.com/embed/'+detail.id.videoId" :title="detail.snippet.title"></iframe>
    <h1 v-html="detail.snippet.title"></h1>
    <h3 v-html="detail.snippet.channelTitle"></h3>
    <p v-html="detail.snippet.description"></p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    detail: Object,
  },
}
</script>

<style>

</style>