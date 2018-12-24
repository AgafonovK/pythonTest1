from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QGridLayout

from PyQt5.QtCore import pyqtSignal


class setDBAdress(QWidget):
    selected = pyqtSignal(str)

    def __init__(self):
        super(setDBAdress, self).__init__()
        self.dbadress = QLineEdit()
        butSave = QPushButton()
        butCancel = QPushButton()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.dbadress, 0, 0)
        grid.addWidget(butSave, 1, 0)
        grid.addWidget(butCancel, 1, 1)

        butSave.clicked.connect(self.btnSave)
        self.setLayout(grid)

    def btnSave(self):
        print("set db " + self.dbadress.text())
        self.selected.emit(self.dbadress.text())

        #MainWindow.var2 = self.dbadress.text()


    def close(self):
        setDBAdress.close()