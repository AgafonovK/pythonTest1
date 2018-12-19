import sys

import postgresql
from PyQt5.QtWidgets import (QTableWidgetItem,
                             QApplication, QTableWidget, QAction, QMainWindow)

import gui


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.SecondWindow = gui.SecondWindow(self)
        self.initUI()

    def initUI(self):
        self.personTable = QTableWidget(self)
        self.setCentralWidget(self.personTable)

        addPersonAction = QAction('+ Add ', self)
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
        fileMenu = menubar.addMenu('&Setting')

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(addPersonAction)
        toolbar.addAction(exitAction)

        #listUser = self.getAllUser()
        #print(listUser)
        #rowCount = len(listUser)

        self.personTable.setColumnCount(7)
        #personTable.setRowCount(rowCount)

        self.refreshAllTableUser(self.personTable)
        self.personTable.setHorizontalHeaderLabels(
            ["First name", "Second name", "Patronimyc", "Phone", "Department", "Email", "Birthday"])
        self.personTable.horizontalHeader
        self.personTable.resizeColumnsToContents()

        self.setFixedSize(550, 350)
        ##self.setGeometry(300, 300,550,350)
        self.setWindowTitle('Review')
        self.show()

    def buttonAddClicked(self):
        self.secondWindow = gui.SecondWindow()
        self.secondWindow.show()

    def getAllUser(self):
        with postgresql.open("pq://postgres:postgres@localhost:5432/book") as db:
            query = db.prepare("select * from user_book")
            #rowCount = len(query())
            listUser = query()
            db.close()
        return listUser

    def refreshAllTableUser(self, personTable):

        listUser = self.getAllUser()
        rowCount = len(listUser)
        personTable.setRowCount(rowCount)
        for row in range(0, rowCount):
            for column in range(0, 7):
                if type(listUser[row][column + 1] == "datetime.date"):
                    widget = str(listUser[row][column + 1])
                    personTable.setItem(row, column, QTableWidgetItem(widget))
                else:
                    personTable.setItem(row, column, QTableWidgetItem(listUser[row][column + 1]))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
