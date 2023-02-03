(정리 도움받음)

#1

학습 목표
✔AWS 배포를 위해 필요한 구조를 학습해본다
✔ 웹서버를 운영하기 위한 기술 스택들을 알아본다
✔ 자주하는 실수에 대해서 알아본다
✔ 배운 것들을 우리 팀 서버 배포 시에 활용해본다

NGINX
✔High performance load balancer, web server, API gateway & reverse proxy
✔비동기 방식이기 때문에 매우 높은 성능
✔'정적인 파일(주로 프론트엔드 파일들)을 서비스할 때 뛰어난 성능(vs 톰캣)
✔load balancer API gateway 용도로도 사용 가능
✔ DDOS 공격 방어도 가능하다!

프론트앤드와 백엔드의 분기
✔/ 로 들어오는 요청은 프론트엔드의 라우터로
✔/api 로 들어오는 요청은 백엔드로 보낸다
✔Webserver로서의 역할
✔API gateway로서의 역할

server {
listen 80 default_server;
listen [::]:80 default_server;

################# Frontend 설정 #############################
root /var/www/html/dist; #Front 빌드 파일 위치
index index.html index.htm # index 파일명
server*name *; #서버 도메인

    location {
    try_files Suri Suri/ /index.html;
    }

############################################################

################ Backend Proxy 설정 ########################
location /api {  
 proxy_pass http://localhost:8399/api/;
proxy_redirect off;
charset utf-8;

    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-NginX-Proxy true;
    }

}
npm run serve (X)

npm run build (o)

CORS
✔ Cross-Origin Resource Sharing(CORS)
✔ 도메인, 포트, 프로토콜이 다를 때 발생한다
✔ nginx의 설정을 기억해보자!
✔ https://domain-a.com의 프론트 엔드 JavaScript 코드가
XMLHttpRequest를 사용하여
https://domain-b.com/data.json을 요청하는 경우

배포 구조(FE를 볼륨으로)
서버를 사오는 중입니다.
AWS의 AutoScaling도 답이 아니었다.
수강신청 전쟁…

우리는 왜 Docker를 쓰는가?
✔빠르게 필요한 서버를 증설할 수 있다
✔기존에는 VM을 증설하는 방식을 사용했음
✔ VM이 부팅되는 1분이면 서비스 전체가 중지되기에 충분한 시간
✔운영체제를 부팅해야 하는 기존의 방식보다 빠름
✔이미지를 만들어두면 찍어내기만 하면 되는 배포의 편의성(w/ k8s) (java 버전을 잘못 깔았어요.. node가 이 버전이 아닌데?!) - 수동 배포에서 문제가 발생할 수 있다.

어디까지 도커화 해야할까?
✔ 프론트엔드/백엔드는 필수적
✔ 배포의 효율성/편의성을 생각해보자
✔ DB/Jenkins/nginx는 선택적

nginx도 따로 docker에서 띄울 수 있다. DB는 회사마다 다르다.
✔ DB를 이미지화해서 새로 배포할 일이 많이 있을까? 옮긴다면 데이터는?
✔ 빌드 서버를 병렬적으로 추가 증설하는 경우는?

임의의 포트를 쓰면 안되는 이유?
twosome.co.kr.7009

사이트에 연결할 수 없음

✔ 투ㅇ플레이스가 접속이 안됐던 이유는?
✔ ISP(SKT, KT, LGU등등)에 따라서 닫혀 있는 포트가 존재
✔ 어느 곳에서는 되고, 어느곳에서는 안되는 서비스라면?
✔ 고객은 포트가 막혔을 거라는 생각을 하지 못하고 그냥 이탈한다

배포 구조
gitlab → jenkins
✔개발자가 gitlab의 특정 브랜치(develop or master)에 머지를 하면 이벤트가 트리거되어 Jenkins에서 빌드를 시작한다
✔ 빌드가 완료되면 도커 이미지가 제작되어 배포된다
✔ 동일한 도커 이미지로 제작, 배포되기 때문에 동일성이 보장된다

충돌나는 경우 웹서버포트, 젠킨스 모두 8080 - 포트 변경 필요

써트봇 이용하면 좋다

배포 구조
SSL (→ TLS)
✔ 회원 가입 시에 비밀 번호 등의 개인 정보가 전송되고, 수시로 유출되어서는 안되는 정보들이 오가기 때문에 암호화가 필요하다
✔ 매번 데이터를 암호화해서 전송하기 어렵기 때문에 TLS(Transport Layer Security)를 사용한다
✔ 이론적으로는 TLS을 활용한 통신은 안전하다고 볼 수 있다
✔ WebRTC를 위해서는 SSL 인증서 설치가 필요!

Cert Bot
✔ https확산을 위해서 시작된 비영리 프로젝트(Let's encrypt)
✔ 상용프로그램을 제작할 때는 보통 신뢰할 수 있는 ROOT 인증서
✔ 발급자로부터 SSL 인증서를 구매해서 사용한다
✔ SSAFY 프로젝트의 경우에는 Cert Bot을 이용해서 무료 인증서를 발급받아서 사용하면 좋다
✔ Cert Bot nginx에 자동으로 설정을 추가해준다!

사용자 계정 만들기
✔ 각 프로그램들을 실행할 때는 프로그램에 맞는 권한을 가진 사용자 계정을 만들어서 실행한다
✔ ubuntu 계정이나 심지어 root 계정으로 실행하는 경우에는 해커의 공격 명령이 그 계정의 권한으로 실행되기 때문에 매우 위험하다
✔ 사용자 계정으로 실행하는 경우 해커의 공격을 받더라도 피해를 최소화할 수 있다
