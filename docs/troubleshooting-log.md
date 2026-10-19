# Troubleshooting Log

## 시나리오: amend
### 참여자
- ghwo6 (내가 공부한 노트를 예제에 포함하였다.)
### 상황
-
### 시도한 명령/절차
-
### 결과
-
### 왜 이 방법을 선택했는가(Why)
-

## 시나리오: reset --soft
### 참여자
- rlawnsxo8709 (실습 수행, 기록 작성)
### 상황
- 이 문서에 stash 기록을 쓰다가 참여자 한 줄만 쓴 상태에서 너무 일찍 커밋했다(`1fef59b docs: stash 시나리오 참여자 기록`).
- reset --soft 기록까지 다 쓴 뒤 커밋 하나로 남기려던 계획이었고, 아직 push 전이었다.
### 시도한 명령/절차
```bash
git log --oneline -2
# 1fef59b docs: stash 시나리오 참여자 기록
# d922112 docs: README 및 CONTRIBUTING 가이드 문서 작성

git reset --soft HEAD~1     # 커밋만 한 단계 되돌리고 변경 내용은 staged로 남긴다

git log --oneline -2
# d922112 docs: README 및 CONTRIBUTING 가이드 문서 작성
# 0c1ca56 Merge pull request #8 from codyb2-2/feature/rlawnsxo8709-queue-note

git status -s
# M  docs/troubleshooting-log.md   ← 왼쪽 M: staged 상태로 그대로 남아 있다
```
### 결과
- `1fef59b`가 브랜치 히스토리에서 빠지고, 고친 내용은 staged 상태로 남았다. 이어서 나머지 기록을 쓰고 커밋 하나로 다시 만들었다.
- 취소한 커밋은 `git reflog`에 `1fef59b HEAD@{1}: commit: ...`으로 남아 있어 필요하면 되돌릴 수 있다.
### 왜 이 방법을 선택했는가(Why)
- push 전의 로컬 커밋이라 히스토리를 바꿔도 다른 팀원에게 영향이 없다.
- `--soft`는 커밋만 취소하고 작업 내용은 그대로 둔다. `--mixed`(기본값)는 unstaged로, `--hard`는 변경까지 지워서 작업을 잃을 수 있다.
- 이미 push한 커밋이었다면 reset 대신 `git revert`로 취소해야 한다.

## 시나리오: revert
### 참여자
-
### 상황
-
### 시도한 명령/절차
-
### 결과
-
### 왜 이 방법을 선택했는가(Why)
-

## 시나리오: stash / stash pop
### 참여자
- rlawnsxo8709 (실습 수행, 기록 작성)
### 상황
- 이 브랜치(`feature/loader1017-docs-update`)에서 이 문서를 쓰는 중에, main에 병합된 최신 README 목차를 확인하려고 main으로 바꿔야 했다.
- 쓰다 만 내용을 커밋하고 싶지 않았고, 수정한 채로 브랜치를 바꾸면 변경이 다른 브랜치로 따라가 섞일 수 있었다.
### 시도한 명령/절차
```bash
git status -s
#  M docs/troubleshooting-log.md

git stash push -m "트러블슈팅 기록 작성 중"
# Saved working directory and index state On feature/loader1017-docs-update: 트러블슈팅 기록 작성 중
git status -s                # 출력 없음: 작업 트리가 깨끗해졌다
git stash list
# stash@{0}: On feature/loader1017-docs-update: 트러블슈팅 기록 작성 중

git switch main
git pull --ff-only origin main   # 8f9e422..542e896 Fast-forward, README 목차 확인

git switch feature/loader1017-docs-update
git stash pop
# Dropped refs/stash@{0} (1246121a...)
git status -s
#  M docs/troubleshooting-log.md   ← 쓰던 내용이 그대로 돌아왔다
git stash list               # 출력 없음: pop 하면 꺼낸 stash는 목록에서 지워진다
```
### 결과
- 쓰다 만 내용을 커밋 없이 보관하고 main을 확인한 뒤, 원래 브랜치로 돌아와 그대로 되살렸다. 충돌 없이 끝났다.
### 왜 이 방법을 선택했는가(Why)
- 임시 커밋을 만들면 히스토리에 의미 없는 커밋이 남는다. stash는 히스토리를 건드리지 않고 작업을 잠시 치워 둔다.
- `-m`으로 이름을 붙여 두면 stash가 여러 개일 때 `git stash list`에서 구분할 수 있다.
- `pop`은 꺼내면서 목록에서 지우고, `apply`는 목록에 남겨 둔다. 다시 쓸 일이 없어서 `pop`을 썼다.
