"""FastAPI hello world 서버.

    python src/hello_server.py                  # http://127.0.0.1:8000
    python src/hello_server.py --port 9000      # 포트 바꾸기
"""

import argparse

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
    """명령행 옵션(--host, --port)을 읽어 run()을 호출한다."""
    parser = argparse.ArgumentParser(description="Hello World FastAPI 서버")
    parser.add_argument("--host", default="127.0.0.1", help="바인딩할 주소 (기본 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="포트 (기본 8000)")
    args = parser.parse_args(argv)
    run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
