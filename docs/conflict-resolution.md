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
