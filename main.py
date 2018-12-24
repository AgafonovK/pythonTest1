import sys

import postgresql
from PyQt5.QtWidgets import (QTableWidgetItem,
                             QApplication, QTableWidget, QAction, QMainWindow, QLabel)

from gui import SecondWindow
from SetDBAdress import setDBAdress


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.SecondWindow = SecondWindow()
        self.initUI()

    def initUI(self):
        self.personTable = QTableWidget(self)
        self.setCentralWidget(self.personTable)

        addPersonAction = QAction('+ Add ', self)
        addPersonAction.setStatusTip('Add Person')
        addPersonAction.triggered.connect(self.buttonAddClicked)

        refreshTableAction = QAction('ref tab', self)
        refreshTableAction.setStatusTip('refresh table')
        refreshTableAction.triggered.connect(self.refreshtable)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        #label = QLabel()
        #setDBAction = QAction('Set Data Base Url', self)
        #self.var2 =""
        #dialog = setDBAdress()
        #dialog.selected.connect(label.setText)

        #setDBAction.triggered.connect(self.setDB)

        #print("!!!! " + label.text())
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(addPersonAction)
        fileMenu.addAction(exitAction)
        #fileMenuSetting = menubar.addMenu('&Setting')
        #fileMenuSetting.addAction(setDBAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(addPersonAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(refreshTableAction)
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

    def foo(self):
        model = self.personTable.selectedItems()
        print(model)

    def refreshtable(self):
        self.personTable.clearContents()
        self.refreshAllTableUser(self.personTable)

    def setDB(self):
        self.setDBadress = self.SetDBAdress()
        #setDBadress.selected.connect(self.var2)
        self.setDBadress.show()


    def buttonAddClicked(self):
        self.secondWindow = SecondWindow()
        self.secondWindow.show()

    def getAllUser(self):
        #print("strdb get " + strdb)
        with postgresql.open("pq://postgres:postgres@localhost:5432/book") as db:
            #"pq://postgres:postgres@localhost:5432/book") as db:
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
