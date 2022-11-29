- 데이터에 가치, 의미가 부여되면 정보

- AWS

  - 컴퓨팅, 스토리지, 데이터베이스와 같은 인프라 기술
  - 기계 학습 및 인공지능, 데이터 레이크 및 분석, 사물 인터넷
  - 위와같은 IT기술 제공

- 클라우드

  - IT 자원을 인터넷 연결을 통해 빌려씀
  - 프로그래밍 방식으로 인프라를 관리
  - 가상화 기술 기반

- AWS 사용 방법

  - Management Console
    - 사용이 간편하고 GUI라 보기쉬움, 직관적
  - AWS CLI
    - 진입장벽이 높음
  - AWS SDK

- CDN

  - 캐쉬서버
  - AWS 엣지 로케이션
    - AWS의 CDN

- 네트워크

  - IP주소
    - 인터넷에서 서로 통신하기 위해 부여하는 고유한 주소
    - `ping 사이트주소`로 IP주소 확인
    - [IP확인](https://www.ipipipip.net/)
    - IPv4
      - 총 32비트로 구성
      - 128비트를 사용하는 IPv6이 새로운 표준으로 제안됨
  - 라우터
    - 게이트웨이
      - 서브넷 마스크(255.255.255.0)를 &연산을 통해 같은 게이트웨이에 속해있는지 확인
      - 게이트웨이에 포함된 네트워크들이 서브 네트워크 (사설 네트워크, PN)
  - DNS
  - CIDR(Classless Inter Domain Routing)
    - VLSM (Variable Length Subnet Mask)

- 리눅스

  - 리눅스는 운영체제
  - 커널
  - 쉘
    - 명령어를 해석하여 커널에 전달
    - 시큐어쉘, 암호화된 쉘, SSH쉘, PuTTY
      - 대칭키(비밀키) AES
        - 하나의 키로 암호화와 복호화
      - 공개키(비대칭키)
        - 나만 가질수 있는 개인키를 가지고 공개키는 공개됨
        - 이를 통해 나만 정보를 받거나 나를 인증할 수 있음
        - 이런 식으로 PuTTY가 mykey.ppk의 개인키를 사용 (SSH 인증 방식)
  - 종류가 엄청 많지만 일단 RedHat 계열과 Debian 계열로 나뉨
  - 가장 유명한 Debian 계열의 Ubuntu
  - 명령어
    - mkdir: 폴더만들기 / rm : 파일지우기 / rmdir: 폴더지우기 / rm -r : recursive하게 지우기(폴더) / clear: 터미널 청소 / history 숫자: 명령어 입력 히스토리
    - 명령어에 관한 것은 `--help`로 찾아보거나 제타 위키 참조
    - cd로 이동
      - `.`은 현재, `..`은 부모, `/`는 루트, `~`는 사용자 폴더
    - `rpm -qa |grep 이름`
      - 설치되어있는지 확인
      - `|`는 앞의 명령어 결과를 뒤의 명령어로 연결하는 것
    - `sudo yum install -y 이름`
      - 설치
    - `sudo systemctl start 이름`
      - 실행
    - `ps -ef |grep 이름`
      - 작업관리자 같은거
      - 너무 많이 뜨므로 grep과 연결
  - httpd를 설치하여 실행하면 웹서버가 구동됨

- AWS

  - IAM
    - 루트 계정 내에 사용자 계정 설정 가능
  - Virtual Private Cloud (VPC)
    - 10.0.0.0/20
      - 마스크가 20자리까지
  - Amazon Elastic Compute Cloud (EC2)
    - 인스턴스 유형
    - 키 페어
    - 네트워크 설정
    - PuTTY(포터블)을 통해 실행
      - HOST Name에 퍼블릭 IPv4주소
      - Connection/SSH/Auth/Credentials에서 키 페어에서 받은 Private key file 등록
      - 첫 방문 Accept
      - login as에는 ec2-user 입력
    - 탄력적 IP 주소를 할당받아 연결하면 고정된 IP주소 사용 가능
      - 연결을 하지 않은채로 두면 과금될 수 있으니 주의!
  - Simple Storage Service (S3)
    - 파일

- FTP

  - FIleZilla 대표적인 클라이언트
    - 사이트 관리자
      - 새 사이트 myec2, 호스트 주소에 IP, 프로토콜은 SFTP, 로그온 유형은 키 파일, 키 파일은 key file 등록, 사용자명은 ec2-user

- ​sudo systemctl start mariadb
- ​sudo mysql_secure_installation
- ​mysql -uroot -pcloud
- ​show databases;
