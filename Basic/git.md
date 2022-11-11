# Git

***분산 버전 관리 프로그램***

- 중앙 집중식 버전 관리 (ex. 은행) ↔ 분산 버전 관리

- GitHub
    - Git을 사용하는 SNS
    - Git기반의 저장소 서비스와 이를 제공하는 서버 = 마이크로소프트

- GitLab
    - 마찬가지, 대신 서버를 내부적으로 저장 가능

- Repository
    - 특정 디렉토리를 버전 관리하는 저장소
    - git init 명령어로 로컬 저장소를 생성

- README.md를 생성해 버전 관리하며  Git 사용 → 특정 버전으로 남긴다 = **커밋**한다.

- 커밋은 3가지 영역을 바탕으로 동작 

    1. Working Directory
        -  내가 작업하고 있는 실제 디렉토리
    2. Staging Area
        - 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
    3. Repository
        - 커밋들이 저장되는 곳 (.git 디렉토리)

## Git 기본기

> 처음에는 WD에 *untracked* 상태
>
> →  **git add**
>
> SA에 트랙된 git을 올림 *staged* 상태
>
> → **git commit**
>
> R에 트랙된 git으로 commit 생성 *committed* 상태
>
> WD에서는 이젠 *modified* 상태가 됨
> 
- `git status`
    - 현재 git으로 관리되고 있는 파일들의 상태를 확인
- `git add`
    - git add . 으로 모든 파일 add 할 수 있음
- `git commit`
    - git commit만 하면 이상한거 뜸 (:q로 나가기)
    - git commit -m “쓰고 싶은 말 (ex. add readme.md, update a.txt)” 이런 식으로 커밋
- `git log`
    - 로그 보여줌
- `git diff A B`
    - A에 비해 B가 어떻게 변했는지 두 커밋 사이 변경 사항을 알려줌
    - commit 번호 앞자리 4개만 써도 가능함

- Local Repository (PC) ↔ Remote Repository (GitHub)

- push
    1. `git remote add origin {remote_repo}`
        - origin : <repo_name> 별명 (관례적)
        - {remote_repo} : github의 repo 주소
    2. `git push -u origin master`
         - git push A B : A로 B브랜치를 push
         - -u : 사용 이후에는 git push만 써도 사용 가능

- repo 생성시 README를 추가할때 defalut branch 이름을 바꿀수있다 (main → master)

- clone
    1. `git clone {remote_repo}`
    2. `git push origin master`
        - 클론시 알아서 새 폴더를 만드므로 미리 만들지 말자

- pull
    1. `git pull`
    2. 양 쪽 모두 변경 사항이 있을 경우 충돌 merge → 사항을 보고 수정 후 git push

- 주소 변경
    - `git remote -v`
        - 우선 현재 주소를 확인
    - `git remote set-url origin [새로운 rep 주소]`

- 브랜치명 변경
    - `git branch -m [변경전 이름] [새로운 이름]`

## Git user

- 사용자 정보 설정
    - `git config --global user.name '이름'`
    - `git config --global user.email '이메일'`
    - global을 local로 변경시 해당 장소에 대해서만 설정을 바꿀 수 있다.
    - `--unset`, `--unset-all` 옵션으로 정보 삭제
    - `git config --list`로 정보 확인

제어판에서 자격 증명 관리를 찾아 자격 삭제 후 재설정 가능

## .gitignore

- .gitignore 파일을 생성
- 안에 써놓은 파일은 git에서 무시함
- `[폴더명]/`, `[폴더명]/*`
    - 폴더와 안의 파일들을 무시함
- `*.확장자`
    - 특정 확장자들을 무시
- .gitkeep
    - 반대로 빈 폴더라도 git이 인식하도록 만들어주는 파일
- [gitignore.io](https://gitignore.io)
    - 운영체제, 개발환경, 언어에 따라 기본적인 .gitignore을 만들어주는 사이트
