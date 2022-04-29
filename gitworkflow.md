# FeatureBranch Workflow

(저장소의 소유권이 있는 경우)



## 한 사람(진아)이 repository를 만들기

협업 할 사람들을 colaborator로 지정하고 각각의 협업할 사람들(민준, 홍지, 인표)은 clone을 받는다.

위 사람들은 master branch에서 작업을 진행하는 것이 아니라 새로운 branch를 만들어 작업한다.

(master의 경우에는 병합하여 앞으로 나갈때 사용)



## 우리가 신경 쓸 부분

(동시에 같은 파일을 수정하지 않게 서로 소통하기!)

1. branch를 각각 만들기

   **git switch -c (각자가 만든 브렌치 이름 ex. feature/login)**

2. 작업하기

3. 작업이 끝난 후 push 하기

   **git add .**

   **git commit -m "오늘의 작업 끝"**

   **git push origin (각자가 만든 브렌치 이름 ex. feature/login)**

4.  Master Branch 가 updated 된 후 

5. 마스터 브렌치로 돌아가기

   **git switch master** 

​		**git pull origin master**

6. 내가 만든 브렌치 삭제해주기

   **git branch -d  (각자가 만든 브렌치 이름 ex. feature/login)**

## 진아누나가 추가로 신경써야 할 부분

1. 우리(홍지, 민준, 인표)가 각자의 branch에서 push 한것들을 **"compare & pull request"**

​	commit 된 부분과 file changed 부분을 통해 확인

​	Merge하고 Merge한 branch는 delete branch 버튼 눌러주기

-> Master Branch가 updated