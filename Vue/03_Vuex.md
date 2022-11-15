- State Management

  - 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음

- Centralized Store

  - 중앙 저장소(store)에 데이터를 모아서 상태 관리

- Vuex

  - Vue의 반응성을 효율적으로 사용하는 상태 관리 기능 제공
  - `vue add vuex`
  - `src/store/index.js`가 생성됨
  - Vuex 인스턴스
    - State
      - vue 인스턴스의 data에 해당
      - 중앙에서 관리하는 모든 상태 정보
      - 개별 component는 state에서 데이터를 가져와서 사용
      - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
      - `$store.state`로 state 데이터에 접근
    - Mutations
      - 실제로 state를 변경하는 유일한 방법
      - vue 인스턴스의 methods에 해당하지만 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함
      - 첫 번째 인자로 state를 받으며, component 혹은 Actions에서 `commit()`메서드로 호출됨
    - Actions
      - 비동기 작업을 포함할 수 있음 (외부 API와의 소통 등)
      - state를 직접 변경하지 않고 `commit()`메서드로 Mutations를 호출해서 state를 변경
      - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음
      - component에서 `dispatch()`메서드에 의해 호출됨
    - Getters
      - vue 인스턴스의 computed에 해당
      - state를 활용하여 계산된 값을 얻고자 할 때 사용
      - computed와 마찬가지로 getters의 결과는 캐시(cache) 됨
      - 첫번째 인자로 state, 두번째 인자로 getter를 받음
  - 모든 데이터를 state에 넣어야 하는 것은 아님
