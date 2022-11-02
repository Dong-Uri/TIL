<template>
  <div class="border">
    <h1>새로운 컴포넌트 입니다.</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem/>
    <MyComponentItem/>
    <MyComponentItem/>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem.vue'

export default {
  name: 'MyComponent',
  // 2. 등록하기
  components: {
    MyComponentItem,
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>