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
        # 말 이미지 경로 설정
        self.piece_images = {
            "r": "src/black/rook.webp",
            "n": "src/black/knight.webp",
            "b": "src/black/bishop.webp",
            "q": "src/black/queen.webp",
            "k": "src/black/king.webp",
            "p": "src/black/pawn.webp",
            "R": "src/white/rook.webp",
            "N": "src/white/knight.webp",
            "B": "src/white/bishop.webp",
            "Q": "src/white/queen.webp",
            "K": "src/white/king.webp",
            "P": "src/white/pawn.webp"
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
        # 체스판 상태를 GUI에 반영
        for row in range(8):
            for col in range(8):
                piece = self.main_window.board.piece_at(chess.square(col, 7 - row))
                button = self.buttons[(row, col)]
                if piece:
                    pixmap = QPixmap(self.piece_images[piece.symbol()])
                    scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)  # 이미지 크기 조정
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
            self.update_board()  # 사용자가 둔 수를 바로 반영
            # AI 차례
            self.main_window.make_ai_move()

class ChessButton(QPushButton):
    def __init__(self, row, col, chessboard):
        super().__init__()
        self.row = row
        self.col = col
        self.chessboard = chessboard
        self.setAcceptDrops(True)  # 드롭을 허용

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
            event.acceptProposedAction()  # 드래그를 허용

    def dropEvent(self, event):
        from_pos = event.mimeData().text().split(',')
        from_row = int(from_pos[0])
        from_col = int(from_pos[1])
        to_row = self.row
        to_col = self.col
        self.chessboard.handle_move(from_row, from_col, to_row, to_col)
        event.acceptProposedAction()  # 드롭을 허용

class ChesGo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChesGo")
        self.setGeometry(100, 100, 800, 800)

        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-sse41-popcnt.exe")

        self.chess_board_widget = ChessBoard(self)
        self.setCentralWidget(self.chess_board_widget)

    def make_ai_move(self):
        if not self.board.is_game_over():
            result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
            self.board.push(result.move)
            self.chess_board_widget.update_board()  # AI가 둔 수를 반영

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChesGo()
    window.show()
    sys.exit(app.exec_())
