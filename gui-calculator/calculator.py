import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget


class Window(QWidget):
    def __int__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        self._create_label()

    def _create_label(self):
        label = QLabel('<h1> Hello World </h1>', parent=self)
        label.move(60, 15)


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    # window.setGeometry(100, 100, 280, 80)
    # window.move(60, 15)

    # hello = QLabel('<h1>Hello world?</h1>', parent=window)
    # hello.move(60, 15)

    window.show()

    sys.exit(app.exec_())

