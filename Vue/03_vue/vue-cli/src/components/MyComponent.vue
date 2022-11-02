<template>
  <div class="border">
    <h1>새로운 컴포넌트 입니다.</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem
      static-props="MyComponent에서 보낸 정적 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
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
  },
  data: function () {
    return {
      dynamicProps: 'MyComponent에서 보낸 동적 데이터',
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('emit 이벤트를 받음')
      console.log(childData)
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>