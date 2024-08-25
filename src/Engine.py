# Engine.py

# ChesGo license
# 저작권(c) 2024 Lucy77m

# 본 소프트웨어는 오픈소스 소프트웨어로, 아래의 조건을 준수하는 경우에 한해 사용, 복제, 수정, 병합, 출판, 배포 및 2차 저작물을 생성할 수 있습니다.

# 소프트웨어의 모든 복제물, 수정물 또는 배포물에는 반드시 원 저작자인 "Lucy77m"와 ChessGo 프로젝트의 출처가 명시되어야 합니다. 출처 명시는 소스코드 내의 적절한 위치(파일 상단 주석 등)에 포함되어야 합니다.

# 상업적 또는 비상업적 용도로 본 소프트웨어를 사용할 수 있습니다.

# 본 소프트웨어는 "있는 그대로" 제공됩니다. 저작권자는 소프트웨어와 관련하여 명시적 또는 묵시적인 어떠한 보증도 제공하지 않으며, 이 소프트웨어의 사용으로 발생하는 모든 문제에 대한 책임은 사용자에게 있습니다.

# 저작권자는 본 라이선스의 조건을 변경할 권리를 가지고 있으며, 변경된 조건은 새로운 버전의 소프트웨어에만 적용됩니다.


# ChesGo 1.0

import chess.engine

class ChessEngine:
    def __init__(self, Engpth="stockfish/stockfish-windows-x86-64-sse41-popcnt.exe"):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(Engpth)

    def make_ai_move(self):
        if not self.board.is_game_over():
            result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
            self.board.push(result.move)
        return self.board

    def move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def get_board(self):
        return self.board
