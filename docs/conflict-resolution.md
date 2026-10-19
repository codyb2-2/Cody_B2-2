# Conflict Resolution Log

## 충돌 기록 #1

### 참여자
- 작성자: rlawnsxo8709 (PR #8 `feature/rlawnsxo8709-queue-note`, 큐 노트)
- 상대: rlawnsxo8709 (PR #6 `feature/rlawnsxo8709-stack-note`, 스택 노트, loader1017이 먼저 병합)

### 상황(What happened)
- PR #6과 PR #8은 둘 다 같은 main(`8f9e422`)에서 출발했고, README `- 목차/목록:` 바로 아래 같은 자리에 서로 다른 링크를 한 줄씩 넣었다.
- 2026-10-19 PR #6이 먼저 main에 병합(`7c250a0`)되자 PR #8이 `This branch has conflicts`(CONFLICTING) 상태가 됐다.
- 같은 위치에 서로 다른 줄이 들어오면 Git은 어느 쪽을 남길지 정하지 못하고 사람에게 맡긴다.

### 충돌 내용(Conflict markers)
```txt
- 목차/목록:
<<<<<<< HEAD
  - [큐(Queue)](docs/queue.md) - rlawnsxo8709
=======
  - [스택(Stack)](docs/stack.md) - rlawnsxo8709
>>>>>>> origin/main
```
- `<<<<<<< HEAD` ~ `=======`: 지금 브랜치(PR #8)의 내용
- `=======` ~ `>>>>>>> origin/main`: 합치려는 main(PR #6 병합 후)의 내용

### 해결 과정(How)
1. `git fetch origin` 후 `git switch feature/rlawnsxo8709-queue-note`
2. `git merge origin/main` → `CONFLICT (content): Merge conflict in README.md`
3. 두 노트 링크가 모두 필요하므로 마커 세 줄을 지우고 두 줄을 다 남겼다. 먼저 병합된 스택을 위에 두었다.
4. `git grep -n -e '<<<<<<<' -e '>>>>>>>'`로 마커가 남지 않은 것을 확인하고 `git add README.md` → `git commit`(`ebaec5b`)
5. `git push origin feature/rlawnsxo8709-queue-note`. 이미 올린 커밋은 그대로 두고 병합 커밋만 더해서 force-push는 하지 않았다.

### 결과(Outcome)
```md
- 목차/목록:
  - [스택(Stack)](docs/stack.md) - rlawnsxo8709
  - [큐(Queue)](docs/queue.md) - rlawnsxo8709
```
- PR #8이 다시 병합 가능한 상태가 됐다.

### 배운 점(Learnings)
- 여러 PR이 같은 파일의 같은 자리를 고치면 나중에 병합되는 PR에서 충돌이 난다. 목차처럼 모두가 한 줄씩 추가하는 곳은 특히 충돌이 잦다.
- 충돌은 "어느 쪽을 버릴까"가 아니라 "합친 결과가 무엇이어야 하나"로 판단한다. 이번에는 둘 다 필요해서 둘 다 남겼다.
- rebase 대신 main을 병합해서 해결하면 이미 올린 커밋이 바뀌지 않아 리뷰 기록이 유지된다.

## 충돌 기록 #2

### 참여자
- 해결: ghwo6 (GitHub 웹 화면에서 충돌 해결, `30c9d73`)
- 검토·보완·기록: rlawnsxo8709 (PR #20 작성자, 빠진 줄 복구 `12bba90`, 이 기록 작성)
- 상대 PR: rlawnsxo8709의 PR #18 `feature/rlawnsxo8709-readme-team-info` (팀명 추가, ghwo6이 먼저 병합)

### 상황(What happened)
- PR #18과 PR #20은 둘 다 같은 main(`0c4d28f`)에서 출발했다.
- PR #18은 README `## 팀 소개` 바로 아래, `- 팀원:` 줄 위에 `- 팀명: Cody_B2-2`를 **새로 넣었고**, PR #20은 그 `- 팀원:` 줄을 **고쳤다**.
- 2026-10-19 PR #18이 먼저 병합(`4ff4557`)되자 PR #20이 CONFLICTING 상태가 됐다.
- 기록 #1은 같은 자리에 서로 다른 줄을 "넣어서" 난 충돌이었다. 이번에는 한쪽은 줄을 넣고 다른 쪽은 바로 붙은 줄을 고쳤다. 고친 줄이 달라도 사이에 바뀌지 않은 줄이 없으면 Git은 같은 hunk로 보고 충돌을 낸다.

### 충돌 내용(Conflict markers)
```txt
## 팀 소개
<<<<<<< HEAD
- 팀원: 1기_김준태(rlawnsxo8709), 1기_류성은(loader1017), 2기_김호재(ghwo6)
=======
- 팀명: Cody_B2-2
- 팀원: 1기_김준태, 1기_류성은, 2기 김호재
>>>>>>> origin/main
```
- `<<<<<<< HEAD` ~ `=======`: PR #20 브랜치의 내용. 팀명 줄은 없고 팀원 줄만 새 표기다.
- `=======` ~ `>>>>>>> origin/main`: main(PR #18 병합 후)의 내용. 팀명 줄이 있고 팀원 줄은 예전 표기다.

### 해결 과정(How)
1. ghwo6이 GitHub 웹 화면의 충돌 해결 기능으로 위쪽(PR #20) 블록을 남기고 병합 커밋 `30c9d73 Merge branch 'main' into feature/rlawnsxo8709-readme-members`를 만들었다.
2. 같은 시각에 rlawnsxo8709도 로컬에서 `git merge origin/main`으로 같은 충돌을 재현해 두 블록을 합쳐 해결했는데, push가 거부됐다.
   ```txt
   ! [rejected]  feature/rlawnsxo8709-readme-members -> feature/rlawnsxo8709-readme-members (fetch first)
   ```
   원격 브랜치에 이미 ghwo6의 해결 커밋이 있었기 때문이다. 남의 커밋을 지우게 되므로 force-push는 하지 않았다.
3. `git fetch` 후 `git diff origin/main origin/feature/rlawnsxo8709-readme-members -- README.md`로 ghwo6 해결본을 확인하니 `- 팀명: Cody_B2-2` 줄이 지워져 있었다. 위쪽 블록만 고르면서 PR #18의 변경이 빠진 것이다.
   ```diff
    ## 팀 소개
   -- 팀명: Cody_B2-2
   -- 팀원: 1기_김준태, 1기_류성은, 2기 김호재
   +- 팀원: 1기_김준태(rlawnsxo8709), 1기_류성은(loader1017), 2기_김호재(ghwo6)
   ```
4. 로컬 해결본은 버리고 원격 브랜치(`30c9d73`)를 기준으로 다시 맞춘 뒤, 빠진 팀명 줄만 되살리는 커밋 `12bba90 fix: 충돌 해결 중 빠진 README 팀명 줄 복구`를 올렸다.

### 결과(Outcome)
```md
## 팀 소개
- 팀명: Cody_B2-2
- 팀원: 1기_김준태(rlawnsxo8709), 1기_류성은(loader1017), 2기_김호재(ghwo6)
```
- 해결 후 main과의 차이는 `- 팀원:` 1줄 수정뿐이다. PR #18의 팀명과 PR #20의 표기 통일이 둘 다 남았다.

### 배운 점(Learnings)
- 다른 줄을 고쳐도 서로 붙어 있으면 충돌이 난다. 충돌은 "같은 줄"이 아니라 "같은 hunk" 단위로 생긴다.
- 웹 화면에서 한쪽 블록을 통째로 고르면 다른 쪽 변경이 조용히 사라질 수 있다. 줄마다 어느 쪽 변경이 필요한지 따로 판단하고, 해결 뒤에는 `git diff origin/main <브랜치>`로 의도한 변경만 남았는지 확인한다.
- 충돌은 PR 작성자가 해결하기로 하거나, 해결하는 사람이 PR에 먼저 알린다. 두 사람이 동시에 고치면 한쪽 push가 거부된다. 그때 force-push로 덮지 말고 원격 결과 위에 이어서 고친다.
