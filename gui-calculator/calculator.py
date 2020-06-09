import sys
from typing import Dict, Generator, Tuple
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, \
    QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons: Dict[str, QPushButton] = {}
        self.setWindowTitle('Calculator')
        self.setFixedSize(450, 500)
        self._central_widget: QWidget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self.arrangement: QVBoxLayout = QVBoxLayout()
        self._central_widget.setLayout(self.arrangement)
        self._make_display()
        self._make_buttons()
        self.style_sheet: str = open('./style.css').read()
        self.setStyleSheet(self.style_sheet)

    def _make_display(self):
        self.display: QLineEdit = QLineEdit('0')
        self.display.setFixedSize(400, 65)
        font = self.display.font()
        font.setPointSize(28)
        self.display.setFont(font)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.arrangement.addWidget(self.display)

    def _make_buttons(self):
        size = 70
        chars: str = '789+456-123/)0[*.+='
        buttons_layout: QGridLayout = QGridLayout()
        positions: Generator[Tuple[int, int]] = (divmod(num, 4) for num in range(20))

        for pos, symbol in zip(positions, chars):
            button: QPushButton = QPushButton(symbol)
            button.setFixedSize(size, size)
            button.setFont(QFont("Consolas", 13))
            buttons_layout.addWidget(button, *pos)
            self.buttons[symbol] = button

        self.arrangement.addLayout(buttons_layout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        self.display.text()

    def clearDisplay(self):
        self.setDisplayText('0')


def main():
    app: QApplication = QApplication(sys.argv)
    window: Calculator = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
