# 📚 Git & GitHub 기초 학습 노트

> **작성자:** loader1017  
> **작성일:** 2026-10-19  
> **목적:** Git 기본 개념 정리 및 GitHub Push 실습용 문서  

---

## 1. Git 기본 주요 개념

* **Working Directory (작업 디렉터리)**: 실제 로컬 컴퓨터에서 파일 작업을 진행하는 공간
* **Staging Area (임시 저장소)**: `git add` 명령어를 통해 커밋 대상 파일들을 올려두는 공간
* **Repository (저장소)**: `git commit`을 통해 버전 관리 히스토리가 최종 기록되는 공간

---

## 2. 필수 커밋 컨벤션 (Commit Convention)

| 타입 (Type) | 설명 (Description) |
| :--- | :--- |
| `feat` | 새로운 기능 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 수정 (README, 주석 등) |
| `style` | 코드 포맷팅, 세미콜론 누락 등 (코드 변화 없음) |
| `refactor` | 코드 리팩토링 |
| `chore` | 빌드 업무 수정, 패키지 매니저 설정 등 |

---

## 3. 실습 중 배운 명령어

```bash
# 1. 파일 상태 확인
git status

# 2. 변경 사항 스테이징
git add <파일명>

# 3. 커밋 생성
git commit -m "docs: Git 기초 학습 노트 추가"

# 4. 원격 저장소로 푸시
git push origin <브랜치명>