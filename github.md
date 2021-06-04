# github 시작하기

## github에 remote repo 생성

간단하게 github에서 저장소 생성



## 서명 설정

`git config --global user.name '이름'`

`git config --global user.email '이메일'`

**확인 방법**

`git config --global user.name`

`git config --global user.email`



## 화살표 이름 지정

git bash에서 `git remote `명령어를 통해서 연결 생성 및 이름 지정

> **만약 이름을 수정하고 싶을 때는 **
>
> `git remote rename 전name 새name` 으로 수정가능
>
> 더 많은 명령어를 찾으려면 `git remote -h`를 통해서 명령어 확인가능

다음 명령어를 통해서 깃허브와 로컬 컴퓨터와 연결

`git remote add 연결name github주소`

`git remote -v`을 통해 현재 연결된 화살표 이름을 확인 할수 있다.

> **만약 연결을 삭제하고 싶다면**
>
> `git remote remove 연결name` 을 통해 연결을 삭제할 수 있다.



## 업로드

`git push 연결name 브랜치name` 명령어를 통해서 업로드

> **만약 github 아이디가 두개여서 충돌이 났을 경우** 
>
> `git config --global user.email 새이메일` 명령어를 통해서 깃허브를 초기화한다
>
> 다른방법으로는 윈도우 자격증명관리자에서 github를 삭제한다.



### 프로젝트를 혼자 할때

- 컴퓨터 1에서 업로드를 통해 github에 프로젝트를 만들었을 경우

- 컴퓨터 2에서 github로 들어가서 clone 을 통해 주소를 복사한다

- git bash에서 `git clone 복사한 주소 (폴더명 기본값은 깃허브 프로젝트 이름이다)` 명령어를 통해서 코드를 받아온다.

- 코드를 수정한 후에 컴퓨터 2에서 업로드를 한다.

- 컴퓨터 1에서 업로드한 데이터를 받기 위해서

  `git pull 연결name 브랜치name(기본은 master)` 을 통해 데이터를 가져온다.



## 협업할 때

- github에서 프로젝트를 생성한다.

  **주의**

  `push` 명령어를 사용할 시 브랜치name을 master를 가져오면 안된다.

- `clone`과 `push`,`pull`명령어를 통해서 개별 컴퓨터에 데이터를 가져온다

  **여기서 개별 컴퓨터에서 master를 가져오되 수정은 다른 브랜치를 따서 수정한다**

- 데이터를 다시 받을 때는 개별 컴퓨터에서 master로 `switch`한 후에 pull을 받는다

  > ex) 
  >
  > `git switch master`
  >
  > `git pull origin master`
  >
  > `git branch -d 브랜치name`