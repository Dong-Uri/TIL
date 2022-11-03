<template>
  <div>
    <ul>
      <video-list-item v-for="(video, index) in videos" :key="index" :video="video" @click-detail="clickDetail">
      </video-list-item>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  name: 'VideoList',
  components: { VideoListItem },
  props: {
    videos: Array,
  },
  methods: {
    clickDetail: function (video) {
      this.$emit('click-detail', video)
      console.log(video)
    }
  },
}
</script>

<style>

</style>