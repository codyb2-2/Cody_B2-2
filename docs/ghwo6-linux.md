# B04-01 간단 학습 노트

1. **목표**: 서버가 1분마다 스스로 상태를 점검하고 로그로 남기게 만든다 (장애 원인 분석은 "감"이 아니라 로그로).
2. **SSH 보안**: `/etc/ssh/sshd_config`에서 `Port 20022`, `PermitRootLogin no` → `systemctl restart ssh`로 적용.
3. **방화벽(UFW)**: 기본 `deny incoming`, `ufw allow 20022/tcp`, `ufw allow 15034/tcp`만 허용. 포트 바꾸기 전에 먼저 열어야 접속이 안 끊긴다.
4. **계정/그룹**: `useradd`로 계정 생성, `usermod -aG`로 그룹 추가. `agent-common`(공유) / `agent-core`(핵심)으로 권한 분리.
5. **최소 권한 원칙**: agent-test는 common만 → 공유 폴더 O, api_keys 접근 X.
6. **권한 숫자**: `770` = 소유자·그룹 rwx, 기타 없음 / `750` = 그룹은 읽기·실행만 / `640` = 그룹 읽기만.
7. **디렉터리 x 권한**: 하위 폴더로 "지나가려면" 상위 디렉터리에 `x`가 필요 → `/home/agent-admin`에 `+x`.
8. **ACL**: 그룹 하나로 표현이 안 될 때 `setfacl -m u:agent-admin:rwx`로 특정 사용자에게 추가 권한. `getfacl`로 확인.
9. **환경변수**: 앱은 `AGENT_HOME`, `AGENT_PORT`, `AGENT_KEY_PATH` 등을 읽어 동작. `sudo -E`로 환경변수를 넘겨 실행.
10. **일반 계정 실행**: root로 앱을 띄우면 뚫렸을 때 피해가 전체로 번진다 → agent-dev로 실행.
11. **백그라운드 실행**: `nohup ... > app.log 2>&1 &` — 터미널이 닫혀도 계속 돌고, 출력·에러를 파일로.
12. **포트 확인**: `ss -tulnp | grep 15034`로 LISTEN 상태 확인.
13. **monitor.sh Health Check**: `pgrep`(프로세스), `ss`(포트) 실패 시 `exit 1` — 앱이 죽었으면 자원 수집은 의미 없음.
14. **자원 수집**: CPU는 `top -bn1`, 메모리는 `free`, 디스크는 `df /`에서 값 추출(`awk`).
15. **임계치 경고**: CPU>20%, MEM>10%, DISK>80% 이면 `[WARNING]` 출력 (UFW 꺼져 있으면 경고만, 종료 X).
16. **로그 포맷**: `[날짜 시간] PID:.. CPU:..% MEM:..% DISK_USED:..%` 한 줄씩 `>>`로 누적.
17. **로그 회전**: 10MB 넘으면 `monitor.log.1`, `.2` …로 밀어내 디스크가 꽉 차는 걸 막는다.
18. **cron**: `crontab -e -u agent-admin`에 `* * * * * 경로/monitor.sh` → 매분 실행. cron은 환경변수가 거의 없으니 절대경로 사용.
19. **증빙**: 설정만 하고 끝이 아니라 before/after 캡처, `tail -n 10 monitor.log`로 1분 간격 누적까지 보여줘야 한다.
20. **핵심 한 줄**: 보안(SSH·UFW) → 권한(그룹·ACL) → 실행(환경변수·일반계정) → 관제(monitor.sh) → 자동화(cron).
