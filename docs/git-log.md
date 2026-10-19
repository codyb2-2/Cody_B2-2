# Git 히스토리 증빙

- 명령: `git log --oneline --graph --all`
- 기준: 원격 저장소 `codyb2-2/Cody_B2-2`를 새로 클론한 직후 (2026-10-19 19:28:31 KST)
- 이 시점에 병합 전이던 브랜치: `feature/rlawnsxo8709-readme-team-info`(PR #18), `feature/rlawnsxo8709-readme-members`(PR #20)

```text
* 6174312 docs: README 팀원 표기를 통일하고 GitHub 아이디 병기
| * 9932864 docs: README 팀 소개에 팀명 추가
|/  
*   0c4d28f Merge pull request #15 from codyb2-2/feature/loader1017-docs-and-notes
|\  
| * e484d37 docs: Git 학습노트 추가 및 README 수정
|/  
*   964c6a7 Merge pull request #14 from codyb2-2/feature/ghwo6-linux-note
|\  
| *   3ba23a3 Merge branch 'main' into feature/ghwo6-linux-note
| |\  
| |/  
|/|   
* |   9383a89 Merge pull request #11 from codyb2-2/feature/loader1017-docs-update
|\ \  
| * \   8f7ade6 Merge branch 'feature/loader1017-docs-update' of github.com:codyb2-2/Cody_B2-2 into feature/loader1017-docs-update
| |\ \  
| | * | 7d36d0a docs: git revert 트러블슈팅 일지 작성
| | * | 806e6a7 chore: .gitignore 파일 추가 및 README 수정
| | * |   92b38e6 Merge remote-tracking branch 'origin/feature/loader1017-docs-update'
| | |\ \  
| | | * | d4741bb docs: 트러블슈팅 reset --soft, stash 시나리오 실습 기록 작성
| | * | | 9e6113c temp: 잘못된 텍스트 추가
| | |/ /  
| * | | bec8ba9 ADD:CONTRIBUTING.md에 브랜치 네이밍 규칙에 보인예시 추가함
| * | | 04bb6b8 docs: 트러블슈팅 reset --soft, stash 시나리오 실습 기록 작성
| |/ /  
| * | d922112 docs: README 및 CONTRIBUTING 가이드 문서 작성
* | |   542e896 Merge pull request #10 from codyb2-2/feature/ghwo6-linux-note
|\ \ \  
| |/ /  
|/| |   
* | |   0c1ca56 Merge pull request #8 from codyb2-2/feature/rlawnsxo8709-queue-note
|\ \ \  
| * | | 7c411e5 docs: README 목차 충돌 해결 과정을 conflict-resolution 기록 #1에 작성
| * | |   ebaec5b merge: main 반영, README 목차 충돌 해결(스택·큐 링크 모두 유지)
| |\ \ \  
| |/ / /  
|/| | |   
| * | | b41fd34 docs: 큐 학습 노트 추가와 README 목차 등록
| | | * 6c4d6f7 troubleshooting-log.md에 본인 시나리오 추가함
| | | * 9c9a1f7 FIX:rlawnsxo8709의견을 반영해 제목이 명확하게 수정함
| | | * 62c0e99 docs:파이썬 학습 노트 추가함(김호재)
| | |/  
| | * 3704ab9 fix:ghwo6-linux.md를 잘못된 폴더로 올려서 docs/로 이동하였습니다.
| | * d09b902 docs:리눅스 학습 노트 추가함(김호재)
| |/  
|/|   
* |   7c250a0 Merge pull request #6 from codyb2-2/feature/rlawnsxo8709-stack-note
|\ \  
| * | 30ba468 docs: 스택 학습 노트 추가와 README 목차 등록
| |/  
* |   62696f5 Merge pull request #3 from codyb2-2/feature/loader1017-remove-team
|\ \  
| |/  
|/|   
| * b3ac2b5 chore: 과제 성격상  불필요한 team 폴더 삭제
|/  
| * 2c092e3 feat: HOST, PORT 환경 변수로 서버 주소와 포트를 바꿀 수 있게 수정
| * 74d2ab6 chore: 서버 실행에 필요한 의존성 목록 추가
| * b2715e5 feat: FastAPI hello world 서버와 run 실행 함수 추가
|/  
* 8f9e422 docs: add initial project structure and document skeletons
* 8247401 Delete README.md
* daebd27 Initial commit
```

## 읽는 법

- `*`는 커밋, `|\`는 두 갈래가 합쳐진 병합 지점, `|/`는 브랜치가 갈라진 지점이다.
- main의 첫 부모(`git log --first-parent main`)를 따라가면 초기 구조 커밋 3개 뒤로는 `Merge pull request #n`만 이어진다. main에 직접 push하지 않고 PR로만 병합했다는 뜻이다.
- 충돌을 해결한 병합 커밋: `ebaec5b`(PR #8, README 목차, 기록 #1), `3ba23a3`(PR #14, `docs/troubleshooting-log.md`)
