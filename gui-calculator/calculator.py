import sys
from typing import Dict, Generator, Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, \
    QLineEdit, QPushButton, QVBoxLayout, QWidget, QGraphicsOpacityEffect




class CalcUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons: Dict[str, QPushButton] = {}
        self.operations = {'+', '-', '\u00f7', '\u00d7', '%'}
        self.special_charcs = {'C', '=', '\u232B'}
        self.opacity_effect = QGraphicsOpacityEffect()
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
        self.display.setFont(QFont("Arial", 27))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.arrangement.addWidget(self.display)

    def _make_buttons(self):
        size = 70
        chars: str = '789+456-123\u00f7.0\u232B\u00d7=C%'
        font: QFont = QFont("Consolas", 13)
        buttons_layout: QGridLayout = QGridLayout()
        positions: Generator[Tuple[int, int]] = (divmod(num, 4) for num in range(20))
        span = [0, 0]
        styles = {**{oper: ('red', '#e1e6ff') for oper in self.operations},
                  **{spec: ('yellow', 'black') for spec in self.special_charcs}}
        amb = styles.get('X', ('#006daa', '#e1e6ff'))

        for pos, symbol in zip(positions, chars):
            button: QPushButton = QPushButton(symbol)
            CalcCtrl(button, self)
            button.setFixedSize(size, size)
            button.setFont(font)
            if symbol == '=':
                span[1] += 1
                pos = [4, 0, 1, 2]
                button.setFixedWidth(180)
            else:
                pos = (x + y for x, y in zip(pos, span))

            if button.text() in self.operations:
                # button.is_operation = True
                button.setStyleSheet('background-color: red;')

            elif button.text() in self.special_charcs:
                # button.is_special = True
                button.setStyleSheet('background-color: yellow; color: black;')
                # button.setStyleSheet('')

            buttons_layout.addWidget(button, *pos)
            self.buttons[symbol] = button

        self.arrangement.addLayout(buttons_layout)


class CalcCtrl:
    def __init__(self, button, window):
        self._button = button
        self._window: CalcUI = window
        self.label: QLineEdit = window.display
        self.symbols = window.buttons.keys()
        self.text = self._button.text()
        self._create_connections()

    def _create_connections(self):
        func = {
            'C': lambda: self.label.setText('0'),
            '\u232B': lambda: self.backspace(self.label.text()),
            '=': lambda: None
        }.get(self.text, lambda: self.on_click(self._window.operations))
        self._button.clicked.connect(func)

    def backspace(self, text: str):
        self: CalcCtrl
        label = self._window.display
        if len(text) != 1 and text not in self._window.operations:
            label.setText(text[:-1])

        else:
            label.setText('0')

    def on_click(self, operations: set):
        self: CalcCtrl
        label_txt = self.label.text()
        if label_txt == '0' and self.text not in {*operations, '.'}:
            label_txt = ''

        if all(txt in operations for txt in (self.text, label_txt)):
            self.label.setText(label_txt[:-1] + self.text)

        else:
            self.label.setText(label_txt + self.text)



def main():
    app: QApplication = QApplication(sys.argv)
    window: CalcUI = CalcUI()
    # CalcCtrl(view=window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
