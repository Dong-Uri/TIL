<template>
  <div id="app">
    <h1>My Vuetube</h1>
    <the-search-bar @input-change="onInputChange"></the-search-bar>
    <hr>
    <video-detail :detail="detail"></video-detail>
    <video-list :videos="videos" @click-detail="clickDetail"></video-list>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail
  },
  data: function () {
    return {
      inputValue: '',
      API_URL: 'https://www.googleapis.com/youtube/v3/search',
      API_KEY: 'AIzaSyAnsSUAW9lFNjuHeo_6AIS77v3_D-52EOs',
      videos: [],
      detail: '',
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText

      const params = {
        key: this.API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios({
        method : 'get',
        url : this.API_URL,
        params
      })
        .then((res) => {
          this.videos = res.data.items
        })
        .catch((err) => {
          console.log(err)
        })
    },
    clickDetail: function (video) {
      this.detail = video
    },
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
