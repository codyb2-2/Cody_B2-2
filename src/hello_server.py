"""FastAPI hello world 서버.

    python src/hello_server.py                  # http://127.0.0.1:8000
    python src/hello_server.py --port 9000      # 포트 바꾸기
    HOST=0.0.0.0 PORT=9000 python src/hello_server.py   # 환경 변수로 바꾸기 (옵션이 있으면 옵션이 우선)
"""

import argparse
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Hello Server")


@app.get("/")
def hello() -> dict[str, str]:
    """루트 경로에서 인사 메시지를 돌려준다."""
    return {"message": "Hello, World!"}


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn으로 서버를 띄운다. Ctrl+C로 멈춘다."""
    uvicorn.run(app, host=host, port=port)


def main(argv: list[str] | None = None) -> None:
    """명령행 옵션(--host, --port)을 읽어 run()을 호출한다. 옵션이 없으면 HOST, PORT 환경 변수를 쓴다."""
    parser = argparse.ArgumentParser(description="Hello World FastAPI 서버")
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"),
                        help="바인딩할 주소 (기본: HOST 환경 변수, 없으면 127.0.0.1)")
    parser.add_argument("--port", type=int, default=os.environ.get("PORT", "8000"),
                        help="포트 (기본: PORT 환경 변수, 없으면 8000)")
    args = parser.parse_args(argv)
    run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
