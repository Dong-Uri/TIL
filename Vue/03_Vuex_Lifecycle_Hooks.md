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
        - 바로 접근하기 보다 computed에 정의 후 접근하는 것을 권장
    - Actions
      - 비동기 작업을 포함할 수 있음 (외부 API와의 소통 등)
      - component에서 `dispatch(A, B)`메서드에 의해 호출됨
        - A는 호출하고자 하는 actions 함수, B는 넘겨주는 데이터(payload)
      - 첫 번째 인자는 context 객체
        - 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음
        - context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
        - dispatch()를 사용해 다른 action도 호출 가능
        - 단, actions에서 state를 직접 조작하는 것은 삼가야 함
      - 두 번째 인자는 payload
        - 넘겨준 데이터를 받아서 사용
      - state를 직접 변경하지 않고 `commit()`메서드로 Mutations를 호출해서 state를 변경
    - Mutations
      - 실제로 state를 변경하는 유일한 방법
      - vue 인스턴스의 methods에 해당하지만 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함
      - component 혹은 Actions에서 `commit(A, B)`메서드로 호출됨
        - A는 호출하고자 하는 mutations 함수, B는 payload
      - 첫 번째 인자는 state, 두 번째 인자는 payload
    - Getters
      - vue 인스턴스의 computed에 해당
      - state를 활용하여 계산된 값을 얻고자 할 때 사용
      - computed와 마찬가지로 getters의 결과는 캐시(cache) 됨
      - 첫 번째 인자는 state, 두 번째 인자는 getter를 받음
      - getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장
  - 모든 데이터를 state에 넣어야 하는 것은 아님

- Lifecycle Hooks

  - 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
  - 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
  - created
    - Vue instance가 생성된 후 호출됨
    - data, computed 등의 설정이 완료된 상태
    - 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
    - mount되지 않아 DOM 요소에 접근할 수 없으므로 동작하지 않음
  - mounted
    - Vue instance 요소가 mount된 후 호출됨
    - mount된 요소를 조작할 수 있음
  - updated
    - 데이터가 변경되어 DOM에 변화룰 줄 때 호출됨
