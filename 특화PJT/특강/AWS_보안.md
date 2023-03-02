(정리 도움받음)

#1

정보보호의 개념
정보보호의 개념
정보의 수집·가공·저장·검색· 송신 중에 정보의 훼손·변조 · 유출 등을 방지하기 위한 관리적·기술적 수단, 또는 그러한 수단으로 이루어지는 행위

기업에서 정보보호의 중요성 (wikipedia)
일자 기업명 사례 피해액
2018.6 코인레일 가상화폐유출 400억
2018.6 빗썸 가상화폐유출 350억
2019.4 네이버 개인정보유출 2200여명
2019.11 업비트 가상화폐유출 580억
기업에서 정보 보호의 대상
출입하는 모든 사람 + 유무형의 정보 자산

목차
사이트 보안
웹 서버 보안
웹 방화벽(WAF)
사이트 보안
파일 업로드 취약점
게시판 등의 첨부파일 기능을 이용해 허가되지 않은 파일들을 웹서버로 업로드할 수 있는 취약점 (php, jsp, asp, cgi, js, py 등)

파일 업로드 취약점 예방
파일 업로드 디렉토리 "실행" 권한 제거
허용되지 않은 확장자 업로드 제한

httpd.conf
<Directory "/usr/local/apache">
AllowOverride FileInfo
</Directory>

.htaccess
<FilesMatch "\.(ph|inc|lib)">
Order allow, deny
Deny from all
</FilesMatch>

AddType text/html html.htm.php .php3 -php4.phtml.phps in .c gㅑ -pl .shtml-jsp
XSS(Cross Site Scripting)
홈페이지 접속자의 권한 정보를 탈취하거나 악성코드 감염을 유발할 수 있는 취약점

XSS(Cross Site Scripting) 예방
XSS 필터 라이브러리 사용

X-XSS-Protection 응답 헤더 사용

문자열 치환(<>& "등을 < > & " 로 치환)

XSS Filter Library

ESAPI

XSS등 웹어플리케이션 시큐어
코딩 라이브러리
문자열 기반 유효성 검사
Lucyxss filter

자바 서블릿 기반 필터
XML 설정만으로 세팅 가능
SQL Injection
게시판 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB 데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발

SQL Injection 예방
시큐어 코딩('--# /\*\*/ 등 입력내용 필터링)
웹방화벽(Web Application Firewall, WAF) 구축

PreparedStatement : 값을 바인딩하는 시점에서 전달된 특수문자 쿼리 등을 필터링하여 sql injection을 막는다.

1 preparedStatement = "SELECT _ FROM users WHERE name = '" + userName + "';";
2
3 # If someone put
4' or '1'='1
5
6 # Result
7 SELECT _ FROM users WHERE name = '' OR '1'='1';
X

1 preparedStatement = "SELECT \* FROM users WHERE name = ?";
2 preparedStatement.setString(1, userName);
3
4 # If someone puts
5' or '1'='1
6
7 # Result
8 SQL FIND name : ' or '1'='1
O

웹 서버 보안
계정 관리
root 계정의 PATH 환경변수 설정
서비스 관리
계정관리
root 계정 원격 접속 제한

로그인 실패 임계값 설정

패스워드 복잡도 설정

Root 계정 원격 접속 제한
Telnet 원격접속 차단
1 vi /etc/securetty
2 pts/0~ pts/x 설정 제거
3
4 vi /etc/pam.d/login
5 # auth required /lib/security/pam_securetty.so #제거(주석제거)
6 auth required/lib/security/pam_securetty.so

SSH 원격접속 차단
1 vi /etc/ssh/sshd_config
2 "PermitRootLogin no" 설정
서비스 관리
Apache, Nginx 등 잘못된 보안 설정으로 발생할 수 있는 비인가자의 원격접 정보 노출 등을 제한하는 것을 목적으로 한다.

Directory Listing: 설정된 모든 Directory 옵션 지시자에서 Indexes 제거

#Directory Listing
Index of /
Name Last modified Size Description
secret/ 2017-01-27 15:40
priv/ 2017-01-27 15:41
edit/ 2017-01-27 15:40
dirl/ 2017-01-27 15:40
config.php 2017-01-27 15:40 11K
Apache/2.4.23 (Wm64) PHP/5.6.25 Server at localhost Port 80
#httpd.conf
1 <Directory />
2 #Options Indexes
3 AllowOverride None
4 Order allow, deny
5 Allow from all
6</Directory>
7
웹 방화벽(WAF)
L7(OSI 7 Layers)에서 보안 유지

SQL Injection, XSS 등 웹 공격 탐지, 차단

DDOS, IP 차단, Rate limit 등 규칙 생성

https://image-kr.bespinglobal.com/wp-content/uploads/2020/09/img_mssp-2.jpg

AWS 보안 가이드
목차
개요 - 클라우드 장점과 보안

사고 사례 - 클라우드 보안 사고 사례와 시사점

모범 사례 - 계정 보안 문제를 피하는 모범 사례

개요 - 클라우드 장점과 보안
클라우드의 장점
초기 선투자 비용 없음 : 고정 비용을 기반비용으로 대체, 미리 서버를 구매할 필요 없음

운영 비용 절감 : 사용한 만큼만 지불하며 규모의 경제로 인한 지속적인 비용 절감

탄력적인 운영 및 확장 : 필요 용량에 대한 예측 불필요, 수요에 맞춘 유연한 확장

속도 및 민첩성 : 수 분 만에 인프라 구축 가능, 빠르게 변화에 대응

비즈니스에만 집중 가능 : 혁신을 위한 다양한 실험 가능, 불필요한 인프라 관리 업무 제거

글로벌 확장 : 빠른 시간 내 글로벌 서비스 구현 가능

사고 사례 - 주요 사고 사례
계정 해킹
[Link] "이용료만 3억원,죽도록 후회해커에 털린 클라우드 개발자
[Link2] AWS-저에겐 2174만원이 없습니다. (해킹과금)
데이터(개인정보) 유출
[Link3] 관리부주의가 클라우드 보안에서 '약한 고리' 되지 않도록
복구 실패(랜섬웨어)
[Link4] [랜섬웨어①] "피해 기업 20%, 파산위기까지 몰려"
"이용료만 3억원, 죽도록 후회"…해커에 털린 클라우드 개발자

https://news.mt.co.kr/mtview.php?no=2022050915224197505

aws - 저에겐 2174만원이 없습니다. (해킹과금)

https://velog.io/@gmtmoney2357/aws-저에겐-2174만원이-없습니다.-해킹과금

AWS 환경에서 사용하는 멀티 팩터 인증(MFA)의 모든 것https://aws.amazon.com/ko/blogs/tech/...

AWS에서 멀티 팩터 인증(MFA) 사용https://docs.aws.amazon.com/ko_kr/IAM...

사고 사례-시사점
계정 보안에 대한 책임은 사용자 본인에게 있다

예방 + 리스크 관리 + 감지

예방

MFA 활성화

AWS Access Key 보호

리스크 관리

ROOT 사용자 보안강화

비용관련 알림 설정

감지

IAM 사용자를 통한 관리

모범 사례 - MFA 활성화
Multi-Factor Authentication

일반적으로 Authenticator app 사용

Google OTP, Twilio Authy, Microsoft Authenticator
암호 이외에 추가적인 인증 과정을 요구

모범 사례 - AWS Access Key 보호
AWS CLI API 사용시, 인증을 위해 사용되는 자격 증명

액세스 키 ID와 보안 액세스 키로 구성

AKIAIOSFODNN/EXAMPLE wlalrXUtnFEMI/K/MDENG/bPXRfICYEXAMPLEKEY

가이드
주기적인 Access Key 교체 및 미사용 Key 제거

어플리케이션별 최소 권한 적용

GitHub등에 Commit 시 주의

git-secrets등을 활용한 Access Key 암호화 및 보호

모범 사례 - ROOT 사용자 보안 강화
ROOT 사용자
AWS 계정 생성시 사용한 이메일주소와 패스워드로 인증하는 계정
모든권한을 지니고 있으며, 권한제약 설정이 불가능
가이드
평상시에는 미사용
Access Key 생성 금지
비밀번호 정책 강화
MFA 활성화
모범 사례 - IAM 사용자를 통한 관리
AWS Identity and Access Management

AWS 리소스에 대한 엑세스를 안전하게 제어할수 있는 서비스
사용자 및 그룹별 인증 및 권한 부여를 통하여, AWS 리소스에 대한 액세스를 안전하게 제어
가이드
개별/용도별 사용자 생성

그룹을 통한 권한관리

비밀번호 정책 강화

모범 사례비용 관련 알림 설정
이메일 정보 업데이트

자주쓰는 이메일로 설정 및 확인
Free Tier 한도 초과 경보 생성

Free Tier 한도초과시 메일이나 SMS 설정
월별/실시간 예상요금 경고 생성

Amazon CloudWatch를 이용한 월간 예상 AWS 요금 알림 설정
AWS Chatbot을 사용한 Slack에서 예산 알림 수신
참고 - 계정 침해시, 후속조치
AWS Support 센터에 Case 등록

AWS 가이드에 따라, 후속 조치

무단으로 생성된 비정상 리소스삭제
전체 사용자(Root 및 IAM 사용자) 암호 변경
모든 AWS Access Key 교체 및 삭제

#2

정보 보호 보안
정보 보호 보안의 개념
정보의 수집, 가공, 저장, 검색, 송신 중에 정보의 훼손, 변조, 유출 등을 방지하기 위한 관리적, 기술적 수단 또는 그러한 수단으로 이루어지는 행위

기업에서 정보 보호의 대상
✔ 출입하는 모든 사람 + 유무형의 정보 자산

정보 보호 대책
관리적 보호 대책: 제도, 보안 교육, 훈련, 보안 직무
물리적 보호 대책: 출입통제, 재난 방지
기술적 보호 대책: 네트워크 접근 통제, 보안 소프트웨어, 방화벽
사이트 보안
✔ 파일 업로드 취약점

✔ XSS (Cross Site Scripting)

✔ SQL Injection

파일 업로드 취약점
✔ 게시판 등의 첨부 파일 기능을 이용해 허가 되지 않은 파일들을 웹서버로 업로드 할 수 있는 취약점 (php, jsp, asp, cji, ji, py 등)

httpd.conf
<Directory "/usr/local/apache">
AllowOverride FileInfo
</Directory>
.htaccess
<FilesMatch "\.(ph|inc|lib)">
Order allow, deny
Deny from all
</FilesMatch>

AddType text/html html.htm.php .php3 -php4.phtml.phps in .c gㅑ -pl .shtml-jsp
예방
✔ 파일 업로드 디렉토리 "실행"권한 제거

✔ 허용되지 않은 확장자 업로드 제한

XSS
✔ 관리자가 아닌 일반 사용자가 악성 스크립트 삽입

✔ 홈페이지 접속자의 권한 정보를 탈취하거나 악성코드 감염을 유발할 수 있는 취약점

예방
✔ XSS 필터 라이브러리

ESAPI
Lucyxss filter
✔ X-XSS-Protection 응답 헤더 사용

✔ 문자열 치환 (<>&" 등을 < > & " 로 치환)

보조적인 방법으로 사용 (공격자가 해제 가능)
SQL Injection
✔ 게시판, 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발

✔ 굉장히 위험하다

예방
✔ 시큐어 코딩(' ; -- # /\* \*/ 등 입력내용 필터링)

PreparedStatement: 값을 바인딩하는 시점에서 전달된 특수문자 쿼리 등을 필터링하여 sql injection 예방
1 preparedStatement = "SELECT \* FROM users WHERE name = ?";
2 preparedStatement.setString(1, userName);
3
4 # If someone puts
5' or '1'='1
6
7 # Result
8 SQL FIND name : ' or '1'='1
✔ 웹 방화벽 구축

웹 서버 보안
✔ 계정관리

✔ root 계정의 PATH 환경변수 설정

✔ 서비스 관리

계정 관리
✔ root 계정 원격 접속 제한

root 계정 보안이 특히 중요하다!
Telnet 원격 접속 차단
SSH 원격 접속 차단
Telnet 원격접속 차단
1 vi /etc/securetty
2 pts/0~ pts/x 설정 제거
3
4 vi /etc/pam.d/login
5 # auth required /lib/security/pam_securetty.so #제거(주석제거)
6 auth required/lib/security/pam_securetty.so
SSH 원격접속 차단
1 vi /etc/ssh/sshd_config
2 "PermitRootLogin no" 설정
✔ 로그인 실패 임계값 설정

✔ 패스워드 복잡도 설정

public key
two factor 로그인 설정
root 계정의 PATH 환경변수 설정
✔ PATH에 디렉토리 경로보다 "."(현재 디렉토리)가 먼저 오면, 변조된 명령어 삽입으로 악의적 기능이 실행될 수 있음

서비스 관리
✔ Apache, Nginx 등 잘못된 보안 설정으로 발생할 수 있는 비인가자의 원격 접속, 정보 노출 등을 제한하는 것을 목적으로 한다

✔ Directory Listing: 설정된 모든 Directory 옵션 지시자에서 indexes 제거

#Directory Listing
Index of /
Name Last modified Size Description
secret/ 2017-01-27 15:40
priv/ 2017-01-27 15:41
edit/ 2017-01-27 15:40
dirl/ 2017-01-27 15:40
config.php 2017-01-27 15:40 11K
Apache/2.4.23 (Wm64) PHP/5.6.25 Server at localhost Port 80
#httpd.conf
1 <Directory />
2 #Options Indexes
3 AllowOverride None
4 Order allow, deny
5 Allow from all
6</Directory>
7
웹 방화벽(WAF)
✔ L7(OSI 7 Layers)에서 보안 유지

✔ SQL injection, XSS 등 웹 공격 탐지, 차단

✔ DDOS, IP차단, Rate limit 등 규칙 생성

✔ modsecurity

AWS 보안 가이드
클라우드의 장점과 보안
클라우드의 장점
✔ 초기 선투자 비용 x

✔ 운영 비용 절감

사용한 만큼만 비용만 낸다
그러나 해킹 발생 시? -> 어마어마한 비용 부과
✔ 탄력적인 운영 및 확장

✔ 속도 및 민첩성

수 분만에 인프라 구축 가능
빠르게 변화에 대응
✔ 비즈니스에만 집중 가능

✔ 글로벌 확장

✔ 접근성

사고 사례
✔ 계정해킹

✔ 데이터 유출

✔ 복구 실패(랜섬웨어)

시사점
✔ 계정 보안에 대한 책임은 사용자 본인에게 있다

✔ 예방

MFA 활성화
AWS access key 보호
✔ 리스크 관리

ROOT 사용자 보안 강화
IAM 사용자를 통한 관리
✔ 감지

비용 관련 알림 설정
모범 사례
MFA 활성화
✔ Multi Factor Authentication

✔ 일반적으로 Authentication App 사용

google OTP, Twilio Authy, Microsoft Authenticator
aws 환경에서 사용하는 MFA의 모든 것

aws에서 MFA 사용

AWS Access Key 보호
✔ AWS CLI나 API 사용시, 인증을 위해 사용되는 자격 증명

✔ access key id와 security access key로 구성

✔ 가이드

주기적인 access key 교체 및 미사용 key 제거
애플리케이션 별 최소 권한 적용
github등 commit 시 주의
git-secrets등을 활용한 access key 암호화 및 보호
AWS 액세스 키 관리를 위한 모범 사례

ROOT 사용자 보안 강화
✔ ROOT 사용자

AWS 계정 생성 시 사용한 이메일 주소와 패스워드로 인증하는 계정
모든 권한을 지니고 있으며, 권한 제약 설정이 불가능
해킹 시 피해가 막심하다!
✔ 가이드

평상시에는 미사용
Access Key 생성 금지
비밀번호 정책 강화
MFA 활성화
IAM 사용자를 통한 괸리
✔ AWS identity and Access Management

aws 리소스에 대한 엑세스를 안전하게 제어할 수 있는 서비스
사용자 및 그룹별 인증 및 권한 부여를 통하여, AWS 리소스에 대한 엑세스를 안전하게 제어
✔ 가이드

개별/용도별 사용자 생성
그룹을 통한 권란 관리
비밀번호 정책 강화
비용 관련 알림 설정
✔ 이메일 정보 업데이트

자주 쓰는 이메일로 설정 및 확인
✔ Free Tier 한도 초과 경보 생성

한도 초과 시 메일이나 SMS 설정
✔ 월별/실시간 예상 요금 경고 설정

Amazon CloudWatch를 이용한 월간 예상 AWS요금 알림 설정
AWS chatbot을 사용한 slack에서 예산 알림 수신
예상 AWS요금을 모니터링하기 위한 결제 겅보 생성

AWS 프리티어 사용량 추적

계정 침해 시 후속 조치
✔ AWS support 센터에 case 등록 (최우선!)

✔ AWS 가이드에 따라 후속 조치

무단으로 생성된 비정상 리소스 삭제
전체 사용자 (Root 및 IAM 사용자) 암호 변경
모든 AWS access key 교체 및 삭제
AWS 계정 보안 문제 해결 방법 및 꼭 지켜야 하는 보안 모범 사례

#3

정보보호 보안의 개념 / 웹보안

1. 정보보호 보안의 개념
   개념 : 정보의 수집, 가공, 저장, 검색, 송신 중 변조, 유출, 훼손 등을 방지하기 위한 관리적, 기술적 또는 그러한 수단으로 이루어지는 행위
   기업에서 정보 보호의 대상
   출입하는 모든 사람 + 유무형의 정보 자산
   정보보호 대책
   관리적 보호대책(제도, 교육, 훈련, 보안 직무)
   물리적 보호 대책(출입 통제, 재난방지)
   기술적 보호 대책(네트워크 접근통제, 보안 소프트웨어, 방화벽)
2. 웹보안 강화
   2-1. 사이트보안
   파일 업로드 취약점
   게시판 등의 첨부파일 기능을 이용해 허가되지 않은 파일들 웹서로 업로드 할 수 있는 취약점(php, jsp, asp, cgi, js, py 등)
   파일 업로드 디렉토리 "실행" 권한 제거
   허용되지 않은 확장자 업로드 제한
   XXS(Cross Site Scripting)
   홈페이지 접속자의 권한 정보를 탈취, 악성코드 감염을 유발할 수 있는 취약점
   XSS 필터 라이브러리 사용
   X-XSS-Protection 응답 헤더 사용(공격자가 옵션을 풀수 있으므로 보조적 수단)
   문자열 치환
   SQL Injection
   게시판, 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발
   시큐어 코딩('; -- /\* \*/' 등 입력내용 필터링)
   웹 방화벽 구축(Web Application FIrewall, WAF)
   PreparedStatement : 값을 바인딩 하는 시점에서 잔달된 특수 문자 쿼리등을 필터링하여 sql injection을 막는다.
   2-2. 웹 서버 보안
   계정 관리
   root계정 원격 접속 제한(Telnet 원격접속 차단, SSH 원격접속 차단)
   로그인 실패 임계값 설정
   패스워드 복잡도 설정
   root계정의 PATH환경변수 설정
   PATH에 디렉토리 경로보다 "."(현재 디렉토리)가 먼오면, 변조된 명령어 삽입으로 악의적인 기능이 실행될 수 있음
   vi /etc/profile 또는 vi /etc/environment

(before) PATH=.:$PATH:$HOME/bin
(After) PATH=:$PATH:$HOME/bin:.
서비스 관리
Apache, Ngnix 등 잘못된 보안 설정으로 발생할 수 있는 비인가자의 원격접속, 정보노출등을 제한하는 것을 목적으로 한다.
Directory Listing : 설정된 모든 Directory 옵션 지지자에서 Indexes 제거
2-3. 웹 방화벽(WAF)
L7(OSI 7 Layers)에서 보안 유지
SQL Injection, XSS 등 웹 공격 탐지, 차단
DDOS, IP 차단, Rate Limit 등 규칙 생성 3. AWS보안 가이드
3-1. 클라우드 장점과 보안
클라우드 장점
초기 선투자 비용 없음 : 고정비용 가변 비용으로 대체, 미리 서버 구매X
운영 비용절감 : 사용한 만큼 지불하여 규모의경제로 인한 지속적인 비용 절감
탄력적인 운영 및 확장 : 필요 용량에 대한 예측 불필요
속도 및 민첩성 : 수분만에 인프라 구축
비지니스에만 집중 가능 : 혁식을 위한 다양한 실험 가능, 불필요한 인프라 관레 업무 제거
글로벌 확장
3-2. 클라우드 보안사고 사레와 시사점
주요 사례
계정 해킹
데이터(개인정보) 유츌
복구 실패(랜섬웨어)
시사점 : 계정 보안에 대한 책임은 사용자 본인에게 있다
예방 : MFA 활성화, AWS Access Key 보호
리스크 관리 : ROOT 사용자 보안강화, IAM 사용자를 통한 관리
감지 : 비용 관련 알림 설정
3-3. 계정 보안 문제를 피하는 모범 사례
MFA
Multi-Factor Authentication
일반적으로 Authenticator app 사용 (Google OTP, Twilio Auty - 추천 : 백업정책 측명에서 편리하고 유용하다, Microsoft Authenticator)
AWS Access Key 보호
AWS CLI나 API사용시, 인증을 위해 사용되는 자격 증명
액세스 키 ID와 보안 액세스 키로 구성
가이드
주기적인 Access Key 교체 및 미사용 Key 제거
어플리케이션별 최소 권한 적용
GitHub등에 Commit시 주의
git-secrets등을 활용한 Access Key 암호화 및 보호
ROOT 사용자
AWS 계정 생성시 사용한 이메일 주소와 패스워드로 인증하는 계정
모든 권한을 지니고 있으며, 권한 제약 설정이 불가능
루트에서 엑세스 키 생성 금지
가이드
평상시에는 미사용
Access Key 생성 금지
비밀번호 정책 강화
MFA 활성화
IAM 사용자를 통한 관리
AWS Identity and Access Management
AWS 리소스에 대한 엑세스를 안전하게 제어할 수 있는 서비스
사용자 및 그룹별 인증 및 권한 부여를 통해, AWS 리소스에 대한 액세스를 안전하게 제어
가이드
개별/용도별 사용자 생성
그룹을 통한 권한 관리
비밀번호 정책 강화
비용관련 알림 설정
이메일 정보 업데이트(자주 쓰는 이메일로 설정 및 확인)
Free Tier 한도 초과 경보 생성(Free Tier 한도 초과시 메일이나 SMS 설정)
월별/실시간 예상 요금 경고 생성(Amazon CloudWatch, AWS Chatbot을 사용한 Slack에서 예산 알림 수신)
참고, 계정 침해시, 후속 조치
AWS Support 센터에 Case 등록
AWS 가이드에 따라 후속 조치
무단으로 생성된 비정상 리소스 삭제
전체 사용자(Root, IAM사용자) 암호 변경
모든 AWS Access Key 교체 및 삭제

#4

pushpin: 정보보호 보안의 개념
정보보호의 개념
정보의 수집·가공·저장·검색·송신 중에 정보의 훼손·변조·유출 등을 방지하기 위한 관리적·기술적 수단, 또는 그러한 수단으로 이루어지는 행위

기업에서 정보 보호의 대상
출입하는 모든 사람 + 유무형의 정보자산

정보보호 대책
관리적 보호 대책 : 제도, 보안교육, 훈련, 보안직무

물리적 보호 대책 : 출입통제, 재난방지

기술적 보호 대책 : (개발자) 네트워크 접근통제, 보안 소프트웨어, 방화벽

기업의 정보 자산 보호

:pushpin: 웹보안 강화
I. 사이트 보안
파일 업로드 취약점
게시판 등의 첨부파일 기능을 이용해 허가되지 않은 파일들을 웹서버로 업로드할 수 있는 취약점 (php, jsp, asp, cgi, js, py 등)
웹 쉘을 이용해서 홈페이지를 변조하거나 자료 유출을 할 수 있음
예방법

파일 업로드 디렉토리 “실행” 권한 제거
허용되지 않은 확장자 업로드 제한
XXS(Cross Site Scripting)
홈페이지 접속자의 권한 정보를 탈취하거나 악성코드 감염을 유발할 수 있는 취약점
게시판 본문에 스크립트를 삽입해 동작하게 되면 공격 가능
해커가 게시물을 올리고, 사용자나 관리자가 게시물을 클릭하면 세션을 탈취해서 악용함
피싱 사이트나 악성 코드를 감염시켜서 랜섬웨어나 악성 사이트로 연결시킴
예방법

XSS 필터 라이브러리 사용
분류 설명
ESAPI - XSS 등 웹 어플리케이션 시큐어 코딩 라이브러리 - 문자열 기반 유효성 검사
Lucyxss filter - 자바 서블릿 기반 필터 - XML 설정만으로 세팅 가능
Header set X-XSS-Protection "1; mode=block"
httpd.conf

add_header X-XSS-Protection "1; mode=block";
nginx.conf

X-XSS-Protection 응답 헤더 사용
문자열 치환(< > & 등을 &lt; &gt; &amp; &quot;로 치환)
SQL Injection
게시판, 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB 데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발
ex) 로그인, 회원가입의 아이디 입력 창에 password 구문을 무력화시키는 코드를 넣음

예방법

시큐어 코딩 (’ ; -- # /\* _/ 등 입력내용 필터링)
웹 방화벽(Web Application Firewall, WAF) 구축
PreparedStatement 사용
DB에 명령어를 던질 때 값을 바인딩하는 시점에서 전달된 특수문자 쿼리 등을 필터링하여 sql injection을 막는다.
preparedStatement = "SELECT _ FROM users WHERE name = '" + username + "';";

# If someone puts

' or '1'='1

# Result

SELECT _ FROM users WHERE name = '' OR '1'='1';
올바르지 않은 예
preparedStatement = "SELECT _ FROM users WHERE name = ?";
preparedStatement.setString(1, userName);

# If someone puts

' or '1'='1

# Result

SQL FIND name : ' or '1'='1
올바른 예
II. 웹 서버 보안
계정관리
root 계정 원격 접속 제한
vi /etc/securetty
pts/0 ~ pts/x 설정 제거

vi /ets/pam.d/login

auth required /lib/security/pam_securetty.so
vi /etc/ssh/sshd_config
"PermitRootLogin no" 설정
로그인 실패 임계값 설정
ex) 5번 이상 틀리면 계정 잠김
패스워드 복잡도 설정
ex) 영어 대소문자, 특수문자, 최소 글자수 만족
패스워드 설정보다 public key나 2-pattern authentication(2FA, ex. 모바일 코드 인증) 사용하면 좋음
root 계정의 PATH 환경변수 설정
PATH에 디렉토리 경로보다 “.”(현재 디렉토리)가 먼저 오면, 변조된 명령어 삽입으로 악의적인 기능이 실행될 수 있음
root path를 현재 디렉토리가 앞에 오게 바꿔놓으면 bin에서 명령어(ls, cat)가 실행되는 게 아니라 특정 디렉토리에서 악의적인 기능이 실행될 수 있음

# vi 편집기를 이용하여 root 계정의 설정파일(~/.profile과 /etc/profile) 열기

vi /etc/profile 또는 vi /etc/environment

(Before) PATH=.:$PATH:$HOME/bin
(After) PATH=$PATH:$HOME/bin:.
서비스 관리
Apache, Nginx 등 잘못된 보안 설정으로 발생할 수 있는 비인가자의 원격 접속, 정보 노출 등을 제한하는 것을 목적으로 한다.
Directory Listing: 설정된 모든 Directory 옵션 지시자에서 Indexed 제거
<Directory />
#Options Indexes
AllowOverride None
Order allow, deny
Allow from all
</Directory>
III. 웹 방화벽 (WAF)
L7(OSI 7 Layer)에서 보안 유지
SQL Injection, XSS 등 웹 공격 탐지, 차단
DDOS, IP 차단, Rate limit 등 규칙 생성
modsecurity

AWS WAF

:pushpin: AWS 보안 가이드
I. 개요 - 클라우드 장점과 보안
클라우드의 장점
초기 선투자 비용 없음
운영 비용 절감
내가 쓴 만큼 지불 (해커 입장에서는 무제한으로 사용 가능함)
탄력적인 운영 및 확장
속도 및 민첩성
빠르고 쉽게 구축 가능 (해커들에게도 쉬움)
비즈니스에만 집중 가능
글로벌 확장
⇒ 클라우드의 장점이 해커 입장에서도 장점이 되므로 주의해야 함

II. 사고 사례 - 클라우드 보안 사고 사례와 시사점
주요 사고 사례
계정 해킹
사례 1 사례 2
데이터(개인정보) 유출
링크
복구 실패(랜섬웨어)
링크
시사점
계정 보안에 대한 책임은 사용자 본인에게 있다

예방

MFA 활성화
AWS Access Key 보호
리스크 관리

ROOT 사용자 보안 강화
IAM 사용자를 통한 관리
감지

비용 관련 알림 설정
III. 모범 사례 - 계정 보안 문제를 피하는 모범 사례
MFA 활성화
Multi-Factor Authentication
일반적으로 Authenticator app 사용
Google OTP, Twilio Authy(추천), Microsoft Authenticator
참고 링크
AWS 환경에서 사용하는 멀티 팩터 인증(MFA)의 모든 것 AWS에서 멀티 팩터 인증(MFA) 사용
AWS Access Key 보호
AWS CLI나 API 사용 시, 인증을 위해 사용되는 자격 증명
액세스 키 ID와 보안 액세스 키로 구성
가이드
주기적인 Access Key 교체 및 미사용 Key 제거
어플리케이션 별 최소 권한 적용
GitHub 등에 Commit 시 주의
git-secrets 등을 활용한 Access Key 암호화 및 보호
참고 링크
AWS 액세스 키 관리를 위한 모범 사례
ROOT 사용자 보안 강화
AWS 계정 생성 시 사용한 이메일 주소와 패스워드로 인증하는 계정
모든 권한을 지니고 있으며, 권한 제약 설정이 불가능
가이드
평소에는 미사용 (IAM 계정 만들어서 사용)
ROOT에서는 Access Key 생성 금지
비밀번호 정책 강화
MFA 활성화
IAM 사용자를 통한 관리
AWS Identity and Access Management
AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 서비스
사용자 및 그룹별 인증 및 권한 부여를 통하여, AWS 리소스에 대한 액세스를 안전하게 제어
가이드
개별/용도별 사용자 생성
그룹을 통한 권한 관리
비밀번호 정책 강화
비용 관련 알림 설정
이메일 정보 업데이트
자주 쓰는 이메일로 설정 및 확인
Free Tier 한도 초과 경보 생성
Free Tier 한도 초과시 메일이나 SMS 설정
월별/실시간 예상 요금 경고 생성
Amazon CloudWatch를 이용한 월간 예상 AWS 요금 알림 생성
AWS Chatbot을 사용한 Slack에서 예산 알림 수신
참고 링크
예상 AWS 요금을 모니터링하기 위한 결제 경보 생성 AWS 프리 티어 사용량 추적 Amazon Chime 및 Slack에서 예산 알림 수신
계정 침해 시, 후속조치
AWS Support 센터에 Case 등록
AWS 가이드에 따라, 후속 조치
무단으로 생성된 비정상 리소스 삭제
전체 사용자(Root 및 IAM 사용자) 암호 변경
모든 AWS Access Key 교체 및 삭제
참고 링크
AWS 계정 보안 문제 해결 방법 및 꼭 지켜야 하는 보안 모범 사례
기타

S3 버킷 설정
시큐리티 설정
:pushpin: QnA
Q. AWS 크레딧을 최소화할 수 있는 방법

A. 인스턴스 타입 최신식을 사용, 사용하지 않을 때(밤에)는 Stop, AWS 무료 온라인 강의

Q. 기업마다 IAM 설정하는 전략

A. 일반적으로 Organization 정책이 따로 있음. 보안 체크리스트가 기업체마다 나와있음

Q. 삼성에서는 AWS 사용하는지

A. 비용, 효율 면에서 AWS 많이 사용함. 삼성이 굉장히 큰 고객임. 보안이 민감한 쪽에서는 On-premise 환경도 병행
