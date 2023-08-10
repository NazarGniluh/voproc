from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(300, 100)

ans1 = QRadioButton("2005")
ans2 = QRadioButton("2008")
ans3 = QRadioButton("2010")
ans4 = QRadioButton("2007")
fiet = QLabel("в якому році канал отримав золоту кнопку від Youtube?")

olin = QVBoxLayout()
olin.addWidget(fiet)

olin2 = QHBoxLayout()

olin2.addWidget(ans1)
olin2.addWidget(ans2)
olin.addLayout(olin2)

olin3 = QHBoxLayout()
olin3.addWidget(ans3)
olin3.addWidget(ans4)
olin.addLayout(olin3)

window.setLayout(olin)

def show_defeat():
    defeat_defor = QMessageBox()
    defeat_defor.setText("НЕ ВІРНА ВІДПОВІДЬ!")
    defeat_defor.exec_()


ans1.clicked.connect(show_defeat)
ans3.clicked.connect(show_defeat)
ans4.clicked.connect(show_defeat)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Правильна Відповідь!")
    victory_win.exec_()



ans2.clicked.connect(show_win)

window.show()
app.exec()
