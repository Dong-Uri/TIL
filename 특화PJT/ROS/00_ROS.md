- ROS

  - Robot Operation System
  - 로봇 소프트웨어를 개발하기 위한 소프트웨어 프레임워크
  - 노드간 통신을 기반으로 전체 시스템 구동
  - 메시지 기록 재생 기능으로 반복적인 실험 가능, 알고리즘 개발에 용이

- ROS Tools

  - Rviz
    - 센서 데이터 등의 데이터 시각화 도구
  - RQT
    - QT 기반 GUI 응용 개발 도구

- ROS 용어

  - ROS Master
    - 노드와 노드 사이의 연결과 통신을 위한 서버
    - 마스터가 없으면 ROS 노드 간 Message, Topic 등의 통신을 할 수 없음
    - `roscore`로 실행
  - ROS Node
    - ROS에서 실행되는 최소 단위 프로세스(프로그램)
    - ROS에서는 하나의 목적에 하나의 노드를 개발하는 것을 추천
  - ROS Message
    - 노드와 노드 간의 데이터를 주고 받는 양식
    - ROS에서는 메시지를 통해 노드 간 데이터를 주고 받음
  - ROS Package
    - ROS 소프트웨어의 기본 단위
    - 패키지는 노드, 라이브러리, 환경설정 파일 들을 통합하는 최소의 빌드 단위이며, 배포 단위
  - ROS Topic
    - 단방향의 연속적인 메시지 송수신 방식
    - 메시지를 송신하기 위해 토픽으로 마스터에 등록하여 메시지를 보냄
    - 비동기 통신, Publisher, Subscriber, 지속적으로 발생하는 송수신
  - ROS Service
    - 양 방향의 일회성 송수신 방식
    - 동기 통신, Client, Server, 클라이언트 요청 후 서버에서 응답
  - ROS Publish
    - Topic에 원하는 메시지를 담아 송신하는 것
  - ROS Publisher
    - Publish를 수행하기 위해 Topic을 포함한 자신의 정보를 마스터에 등록하고, Subscriber Node에 Message를 보냄
    - 하나의 노드에 여러 개의 Publisher를 선언 할 수 있음
  - ROS Subscribe
    - Topic의 내용에 해당하는 Message를 수신하는 것
  - ROS Subscriber
    - Subscribe를 수행하기 위해 Topic을 포함한 자신의 정보를 마스터에 등록하고, 수신하고자 하는 Topic의 정보를 Master로부터 받음
    - 하나의 노드에 여러 개의 Subscriber를 선안 할 수 있음

- ROS Workspace

  - src
    - Catkin 패키지의 소스 코드를 포함하는 공간
  - build
    - Catkin 패키지를 빌드하기 위해 Cmake가 호출되는 공간
  - devel
    - 패키지를 시스템에 설치하기 전, 개발 과정에 쓰이는 실행 파일과 라이브러리들이 저장되는 공간

- ROS 명령어

  - ROS 쉘 명령어
    - roscd
      - 지정한 ROS 패키지의 디렉토리 위치로 이동
    - rosls
      - ROS 패키지의 파일 목록 확인
  - ROS 정보 명령어
    - rostopic
      - ROS 토픽 정보 확인
    - roservice
      - ROS 서비스 정보 확인
    - rosnode
      - ROS 노드 정보 확인
    - rosbag
      - ROS 메시지 기록, 재생
    - rosmsg
      - ROS 메시지 파일 정보 확인
    - rossrv
      - ROS 서비스 파일 정보 확인
    - rosversion
      - ROS 패키지 및 릴리즈 버전 정보 확인
  - ROS 실행 명령어
    - roscore
      - 마스터 노드 실행
    - rosrun
      - 노드 실행
    - roslaunch
      - 여러 노드 실행 및 실행 옵션 설정
    - rosclean
      - Ros log file 검사 및 삭제
  - ROS catkin 명령어
    - catkin_create_pkg
      - Catkin 빌드 시스템으로 패키지 자동 생성
    - catkin_make
      - Catkin 빌드 시스템에 기반을 둔 빌드
    - catkin_init_workspace
      - Catkin 빌드 시스템 작업 폴더 초기화

- Package 생성

  - 워크 스페이스 생성
    - `mkdir -p catkin_ws/src`
    - `cd catkin_ws`
    - `catkin_make`
  - 패키지 생성 및 빌드
    - `cd ~/`
    - `cd catkin_ws/src`
    - `catkin_create_pkg <패키지명> rospy std_msgs`
      - rospy는 의존성을 만드는 것
    - `cd <패키지명> && mkdir scripts`
    - `cd ~/catkin_ws`
    - `catkin_make`
  - catkin 환경 변수 선언
    - `source ~/catkin_ws/devel/setup.bash`
      - 항상 해주어야 함
  - catkin 패키지 재구축
    - `rospack profile`

- script 실행

  - 각자 터미널에서 실행
  - 마스터 노드 실행
    - `roscore`
  - script 실행
    - `roscd <패키지명>/scripts`
    - `chmod +x <script명>`
      - 코드의 실행 권한을 바꿈
    - `rosrun <패키지명> <script명>`

- launch 실행

  - 실행해야할 노드가 여러 개 있을때 유용하게 사용
  - 마스터 노드(roscore)가 실행되어 있지 않을 경우 자동 실행
  - XML 형식으로 기록

  ```
  <launch>
    <node pkg="패키지명" type="노드가 포함된 소스파일 명" name="노드이름"/>
    <include file="같이 실행할 .launch의 파일 경로"/>
  </launch>
  ```

  - `roslaunch <패키지명> <launch명>`

- ROS catkin 명령어

  - `catkin_create_pkg`
    - Catkin 빌드 시스템으로 패키지 자동 생성
  - `catkin_make`
    - Catkin 빌드 시스템에 기반을 둔 빌드
  - `catkin_init_workspace`
    - Catkin 빌드 시스템 작업 폴더 초기화
