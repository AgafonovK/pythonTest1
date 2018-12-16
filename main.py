import sys
import postgresql
import gui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,QTableWidgetItem,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QTableWidget, QAction, QMainWindow)
from PyQt5.QtCore import QSize,Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        personTable = QTableWidget(self)
        self.setCentralWidget(personTable)

        addPersonAction = QAction('+ Add ',self)
        addPersonAction.setStatusTip('Add Person')
        addPersonAction.triggered.connect(self.buttonAddClicked)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(addPersonAction)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        toolbar.addAction(addPersonAction)

        with postgresql.open("pq://postgres:postgres@localhost:5432/book") as db:
            query = db.prepare("select * from user_book")
            rowCount = len(query())
            listUser = query()
            db.close()
        #print(listUser)

        personTable.setColumnCount(7)
        personTable.setRowCount(rowCount)

        personTable.setHorizontalHeaderLabels(["First name","Second name","Patronimyc","Phone", "Department","Email","Birthday"  ])
        personTable.horizontalHeader

        for row in range(0,rowCount):
            for column in  range(0,7):
                if type(listUser[row][column+1]=="datetime.date"):
                    widget = str(listUser[row][column+1])
                    personTable.setItem(row,column,QTableWidgetItem(widget))
                else:
                    personTable.setItem(row,column,QTableWidgetItem(listUser[row][column+1]))

        personTable.resizeColumnsToContents()

        self.setFixedSize(550,350)
        ##self.setGeometry(300, 300,550,350)
        self.setWindowTitle('Review')
        self.show()

    def buttonAddClicked(self):
        self.secondWindow = gui.SecondWindow()
        self.secondWindow.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())