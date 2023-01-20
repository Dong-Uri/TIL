- App.vue

  - `import { OpenVidu } from "openvidu-browser";`

    - openvidu-browser NPM 패키지 사용

  - ```js
    data() {
      return {
        // OpenVidu objects
        OV: undefined,
        session: undefined,
        mainStreamManager: undefined,
        publisher: undefined,
        subscribers: [],

        // Join form
        mySessionId: "SessionA",
        myUserName: "Participant" + Math.floor(Math.random() * 100),
      };
    },
    ```

    - `OV` object will allow us to get a `session` object, which is declared just after it. `mainStreamManager` is the main video of the page, which will display the publisher or one of the subscribers. `publisher` StreamManager object will be our own local webcam stream and `subscribers` StreamManager array will store the active streams of other users in the video-call. Finally, `mySessionId` and `myUserName` params simply represent the video-call and your participant's nickname, as you will see in a moment.
    - OV
      - OpenVidu 객체를 받을 변수
      - `this.OV = new OpenVidu();`
    - session
      - OV를 통해 initSession으로 session(방)을 init함
      - 생성된 session의 객체
      - `this.session = this.OV.initSession();`
    - mainStreamManager
      - publisher나 subscriber를 표시할 페이지의 메인 비디오
    - publisher
      - 소유한 로컬 웹캠 객체 == 내 웹캠?
    - subscribers
      - 다른 사용자의 활성 스트림을 저장한 배열
    - mySessionId, myUserName
      - 방제목, 닉네임
      - join form에서 입력됨

  - `joinSession()`

    - ```js
      // --- 1) Get an OpenVidu object ---
      this.OV = new OpenVidu()

      // --- 2) Init a session ---
      this.session = this.OV.initSession()
      ```

      - initialize a Session object

    - ```js
      // --- 3) Specify the actions when events take place in the session ---

      // On every new Stream received...
      this.session.on("streamCreated", ({ stream }) => {
        // Subscribe to the Stream to receive it. Second parameter is undefined
        // so OpenVidu doesn't create an HTML video by its own
        let subscriber = this.session.subscribe(stream, undefined)
        this.subscribers.push(subscriber)
      })

      // On every Stream destroyed...
      this.session.on("streamDestroyed", (event: StreamEvent) => {
        // Remove the stream from 'subscribers' array
        const index = this.subscribers.indexOf(stream.streamManager, 0)
        if (index >= 0) {
          this.subscribers.splice(index, 1)
        }
      })

      // On every asynchronous exception...
      this.session.on("exception", ({ exception }) => {
        console.warn(exception)
      })
      ```

      - streamCreated
        - for each new Stream received by the Session object, we subscribe to it and store the returned Subscriber object in our subscribers array. Method session.subscribe has undefined as second parameter so OpenVidu doesn't insert and HTML video element in the DOM on its own (we will use the video element contained in one of our child components). HTML template of App loops through subscribers array with an v-for directive, declaring a UserVideo for each subscriber. We feed them not really as Subscriber objects, but rather as their parent class StreamManager. This way we can reuse UserVideo to also display our Publisher object (that also inhertis from class StreamManager). user-video also declares the click event so we can update the main video player view when the user clicks on its Publisher or any Subscriber videos.
        - subscribers 배열에 Session 객체가 받는 새 Stream들에 대한 Subscriber 객체를 저장
      - streamDestroyed
        - for each Stream that has been destroyed from the Session object (which means a user has left the video-call), we remove the associated Subscriber from subscribers array, so Vue will automatically delete the required UserVideo from HTML. Each Stream object has a property streamManager that indicates which Subscriber or Publisher owns it (in the same way, each StreamManager object also has a reference to its Stream).
      - exception
        - event triggered by Session object when an asynchronous unexpected error takes place on the server-side

    - Token

      - 은 다음 기회에

      - ```js
        // --- 5) Get your own camera stream with the desired properties ---

        // Init a publisher passing undefined as targetElement (we don't want OpenVidu to insert a video
        // element: we will manage it on our own) and with the desired properties
        let publisher = this.OV.initPublisher(undefined, {
          audioSource: undefined, // The source of audio. If undefined default microphone
          videoSource: undefined, // The source of video. If undefined default webcam
          publishAudio: true, // Whether you want to start publishing with your audio unmuted or not
          publishVideo: true, // Whether you want to start publishing with your video enabled or not
          resolution: "640x480", // The resolution of your video
          frameRate: 30, // The frame rate of your video
          insertMode: "APPEND", // How the video is inserted in the target element 'video-container'
          mirror: false, // Whether to mirror your local video or not
        })

        // Set the main video in the page to display our webcam and store our Publisher
        this.mainStreamManager = publisher
        this.publisher = publisher
        ```

        - 토큰을 받고 session(방)에 접근할때 publisher를 선언함 (OV를 통해 initPublisher로)
        - 오디오, 비디오의 소스를 접근할 수 있을 듯? (아직 모르겠음)
        - publishing 할지 말지 정할 수 있음 (음소거, 카메라IO)
        - 의문

          - 그럼 음소거 할때마다 세션(방) 접속을 새로해야하나??

        - 홈술이의 mute
          - ```js
            <button
              class="btn mr-2"
              @click="clickMuteVideo"
            >
              <img
                src="@/assets/images/webcam.png"
                alt="webcam"
                v-if="publisher.stream.videoActive"
              >
              <img
                src="@/assets/images/webcam_off.png"
                alt="webcam_off"
                v-else
              >
            </button>
            ```
          - ```js
            clickMuteVideo({ state }) {
              if (state.publisher.stream.videoActive) {
                state.publisher.publishVideo(false)
              } else {
                state.publisher.publishVideo(true)
              }
            },
            ```
            - vuex state를 통해 publisher 접근하여 변경

- 기타사항

  - 프론트 프레임 / 위젯 나누기
  - ```js
    if (state.currentMode !== mode) {
      isPermitted = false
      Swal.fire({
        html: "현재 모드를 중단하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: "네",
        cancelButtonText: "아니요",
        icon: "warning",
      }).then((result) => {
        if (result.value) {
          dispatch("sendModeSignal", mode)
        }
      })
    }
    ```
    - Swal 뭔지 몰라도 편해보임
    - `import Swal from 'sweetalert2';`
