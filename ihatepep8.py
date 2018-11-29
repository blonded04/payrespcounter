import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit


class FreeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.makeUI()

    def makeUI(self):
        self.setGeometry(0, 0, 420, 300)
        self.setWindowTitle(
            "i hate pep8 6.0, added input-box(pay-respect counter)")

        self.frstbtn = QPushButton("F", self)
        self.frstbtn.resize(125, 100)
        self.frstbtn.move(137, 100)
        self.frstbtn.clicked.connect(self.i61)

        self.text = QLabel(self)
        self.text.setText("You have already PAYED RESPECT ")
        self.text.move(10, 225)

        self.counter = QLCDNumber(self)
        self.counter.move(200, 225)

        self.text = QLabel(self)
        self.text.setText("- these amount of times ")
        self.text.move(270, 225)

        self.text_for_input = QLabel(self)
        self.text_for_input.setText("Insert here ur int step ->")
        self.text_for_input.move(10, 50)

        self.inputbox = QLineEdit(self)
        self.inputbox.move(200, 50)

        self.count = 0

    def i61(self):
        self.count += int(self.inputbox.text())
        self.counter.display(self.count)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FreeWindow()
    ex.show()
    sys.exit(app.exec())
