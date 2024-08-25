# ChesGo license
# 저작권(c) 2024 Lucy77m

# 본 소프트웨어는 오픈소스 소프트웨어로, 아래의 조건을 준수하는 경우에 한해 사용, 복제, 수정, 병합, 출판, 배포 및 2차 저작물을 생성할 수 있습니다.

# 소프트웨어의 모든 복제물, 수정물 또는 배포물에는 반드시 원 저작자인 "Lucy77m"와 ChessGo 프로젝트의 출처가 명시되어야 합니다. 출처 명시는 소스코드 내의 적절한 위치(파일 상단 주석 등)에 포함되어야 합니다.

# 상업적 또는 비상업적 용도로 본 소프트웨어를 사용할 수 있습니다.

# 본 소프트웨어는 "있는 그대로" 제공됩니다. 저작권자는 소프트웨어와 관련하여 명시적 또는 묵시적인 어떠한 보증도 제공하지 않으며, 이 소프트웨어의 사용으로 발생하는 모든 문제에 대한 책임은 사용자에게 있습니다.

# 저작권자는 본 라이선스의 조건을 변경할 권리를 가지고 있으며, 변경된 조건은 새로운 버전의 소프트웨어에만 적용됩니다.




# ChesGo 1.0
# Main Engine

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QDrag
from PyQt5.QtCore import pyqtSlot, Qt, QMimeData
import chess
import chess.engine

class ChessBoard(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.main_window = main_window
        self.selected_piece = None
        self.buttons = {}
        self.initialize_board()

    def initialize_board(self):
        self.piece_images = {
            "r": "img/black/rook.webp",
            "n": "img/black/knight.webp",
            "b": "img/black/bishop.webp",
            "q": "img/black/queen.webp",
            "k": "img/black/king.webp",
            "p": "img/black/pawn.webp",
            "R": "img/white/rook.webp",
            "N": "img/white/knight.webp",
            "B": "img/white/bishop.webp",
            "Q": "img/white/queen.webp",
            "K": "img/white/king.webp",
            "P": "img/white/pawn.webp"
        }

        for row in range(8):
            for col in range(8):
                button = ChessButton(row, col, self)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                color = "white" if (row + col) % 2 == 0 else "gray"
                button.setStyleSheet(f"background-color: {color};")
                self.layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

        self.update_board()

    def update_board(self):
        # GUI Update
        for row in range(8):
            for col in range(8):
                piece = self.main_window.board.piece_at(chess.square(col, 7 - row))
                button = self.buttons[(row, col)]
                if piece:
                    pixmap = QPixmap(self.piece_images[piece.symbol()])
                    scaled_pixmap = pixmap.scaled(70, 70, Qt.KeepAspectRatio)  
                    icon = QIcon(scaled_pixmap)
                    button.setIcon(icon)
                    button.setIconSize(scaled_pixmap.size())
                else:
                    button.setIcon(QIcon())

    def handle_move(self, from_row, from_col, to_row, to_col):
        from_square = chess.square(from_col, 7 - from_row)
        to_square = chess.square(to_col, 7 - to_row)
        move = chess.Move(from_square, to_square)

        if move in self.main_window.board.legal_moves:
            self.main_window.board.push(move)
            self.update_board()  
            self.main_window.make_ai_move()
            self.update_board()

class ChessButton(QPushButton):
    def __init__(self, row, col, chessboard):
        super().__init__()
        self.row = row
        self.col = col
        self.chessboard = chessboard
        self.setAcceptDrops(True) 

    def mousePressEvent(self, event):
        if self.icon():
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(f"{self.row},{self.col}")
            drag.setMimeData(mime_data)
            drag.setPixmap(self.icon().pixmap(self.iconSize()))
            drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction() 

    def dropEvent(self, event):
        from_pos = event.mimeData().text().split(',')
        from_row = int(from_pos[0])
        from_col = int(from_pos[1])
        to_row = self.row
        to_col = self.col
        self.chessboard.handle_move(from_row, from_col, to_row, to_col)
        event.acceptProposedAction()  

class ChessGo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChessGo")
        self.setGeometry(100, 100, 800, 800)

        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish path here")

        self.chess_board_widget = ChessBoard(self)
        self.setCentralWidget(self.chess_board_widget)

    def make_ai_move(self):
        if not self.board.is_game_over():
            result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
            self.board.push(result.move)
            self.chess_board_widget.update_board() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGo()
    window.show()
    sys.exit(app.exec_())
