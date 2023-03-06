- Network setting

  - `roslaunch rosbridge_server rosbridge_websoket.launch`
  - IP 입력 후 Connect

- 시뮬레이터 메시지

  - 토픽 메시지

    - `/ctrl_cmd`
      - Ego 차량을 제어하기 위한 메시지
      - `CtrlCmd`
    - `/Object_topic`
      - 사용자가 배치한 주변 NPC 차량들에 대한 정보를 나타내는 메시지
      - `ObjectStatusList`
    - `/CollisionData`
      - Ego 차량과의 충돌 데이터를 나타내는 메시지
      - `CollisionData`

  - 서비스 메시지

    - `/Service_MoraiEventCmd`
      - 기어, 제어 모드 등의 이벤트 제어 요청 메시지
      - `MoraiEventCmdSrv`
    - `/Service_MoraiVehicleSpec`
      - 차량 스펙 호출 메시지
      - `MoraiVehicleSpecSrv`

  - 데이터 출력
    - `rostopic echo /<메시지명>`
  - 데이터 입력
    - `rostopic pub /<메시지topic명> /<메시지type명> "{메시지내용}"`

- Python script

  ```
  #!/usr/bin/env python

  import rospy
  from morai_msgs.msg import CtrlCmd

  class s_drive():
      def __init__(self):
          rospy.init_node('s_drive', anonymous=True)
          cmd_pub = rospy.Publisher('/ctrl_cmd', CtrlCmd, queue_size=1)
          rate = rospy.Rate(30)
          cmd = CtrlCmd()
          cmd.longlCmdType = 2
          cmd.velocity = 10
          steering_cmd =  [-0.2, 0.2]
          cmd_cnts = 50

          while not rospy.is_shutdown():
              for i in range(2):
                  cmd.steering = steering_cmd[i]
                  rospy.loginfo(cmd)
                  for _ in range(cmd_cnts):
                      cmd_pub.publish(cmd)
                      rate.sleep()

  if __name__ == '__main__':
      try:
          s_d = s_drive()
      except rospy.ROSInterruptException:
          pass
  ```

  - `!/usr/bin/env python`
    - env는 환경 변수에서 지정한 언어의 위치를 찾아 실행
    - ROS에서 Python을 실행하기 위한 명령어
  - `improt rospy`
    - 노드 작성을 python으로 작성하기 위한 필수 라이브러리
    - rospy를 통해 rostopics, service, parameters를 python으로 접근 가능하게 함
  - `from morai_msgs.msg import CtrlCmd`
    - 시뮬레이터 메시지를 가져옴
    - Morai_msg/CtrlCmd를 사용
  - `rospy.init_node('s_drive', anonymous=True)`
    - 프로세스에 대한 노드를 초기화
    - ros master와 통신을 시작하기 위해 rospy에 사용하는 코드는 고유한 이름을 알려주어야 함
  - `rospy.Publisher(topic_name, msg_class, queue_size)`
