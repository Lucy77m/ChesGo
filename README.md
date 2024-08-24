![ChessGo](https://github.com/user-attachments/assets/43687ad5-b9a0-43e8-ae75-8ca0a51491bf)

# What is this

Python으로 만든 Stockfish 16.1 기반 체스봇입니다. PyQt5와 python-chess 라이브러리를 사용하였습니다.

# How it works

프로그램을 실행할 시 `ChessGo`라는 인스턴스가 생성되어 윈도우가 띄워집니다. 사용자가 기물을 드래그 앤 드롭으로 이동시키면 `chessbton` 클래스가 이를 처리하고, `ChessBoard`의 `hdmove()` 함수가 호출되어 Stockfish 엔진에 사용자의 수를 반영합니다. 사용자 수가 반영된 후, `make_ai_move()`가 호출돼 엔진이 수를 둡니다.

# Usage

- 파이썬이 설치되어 있어야 합니다. (최신 버전 권장)
1. [Stockfish를 다운받습니다.](https://stockfishchess.org/)
2. Stockfish 폴더를 `src` 폴더 안에 넣습니다.
3. 엔진 파일의 경로를 바꿉니다. (125줄)
4. 실행

아 라면먹고싶다

