![LogoYell](https://github.com/user-attachments/assets/d8f06ca8-48c4-4d48-8a10-04ddad0d598b)

# What is this

Python으로 만든 Stockfish 16.1 기반 **오픈소스** 체스봇입니다. PyQt5와 python-chess 라이브러리를 사용하였습니다.

# How it works

프로그램을 실행할 시 `ChessGo`라는 인스턴스가 생성되어 윈도우가 띄워집니다. 사용자가 기물을 드래그 앤 드롭으로 이동시키면 `chessbutton` 클래스가 이를 처리하고, `ChessBoard`의 `handle_move()` 함수가 호출되어 Stockfish 엔진에 사용자의 수를 반영합니다. 사용자 수가 반영된 후, `make_ai_move()`가 호출돼 엔진이 수를 둡니다.

# Usage

- 파이썬이 설치되어 있어야 합니다. (최신 버전 권장)
1. [Stockfish를 다운받습니다.](https://stockfishchess.org/)
2. Stockfish 폴더를 `src` 폴더 안에 넣습니다.
3. Engine.py의 엔진 파일의 경로를 바꿉니다. (22번째 줄)
4. src 폴더안에 있는 `install.bat`을 실행합니다.
5. `python main.py`라는 구문을 실행합니다. (cmd에서 실행시 cd src후 구문을 실행해야 오류가 나지 않습니다.)

# Versions
## 1.0.0
* 최초 출시

# photos
![image](https://github.com/user-attachments/assets/136b281f-01d1-4ce6-9593-f8a33661dc3a)

![image](https://github.com/user-attachments/assets/9b180a5a-7205-45ea-93d7-8c1f5a7eb740)


###### 로고는 포토샵으로 제작하였습니다.
