from PyQt5.QtWidgets import QLabel,QLineEdit, QDialog, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSignal
import main
import postgresql
from datetime import datetime,date

class SecondWindow(QDialog):

    #varSignal = pyqtSignal(str)

    def __init__(self, parent=main.MainWindow):
        super(SecondWindow, self).__init__()
        self.initUi()

    def initUi(self):

        firstName = QLabel("First Name")
        lastName = QLabel("Last Name")
        patronymic = QLabel("Patronymic")
        phone = QLabel("Phone")
        department = QLabel("Department")
        email = QLabel("email")
        birthday = QLabel("birthday")

        firstNameText = QLineEdit()
        lastNameText = QLineEdit()
        patronymicText = QLineEdit()
        phoneText = QLineEdit()
        departmentText = QLineEdit()
        emailText = QLineEdit()
        birthdayText=QLineEdit()

        buttonAdd = QPushButton("Add User")
        buttonCancel = QPushButton("Cancel")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(firstName, 0, 0)
        grid.addWidget(firstNameText, 0, 1)

        grid.addWidget(lastName, 1, 0)
        grid.addWidget(lastNameText, 1, 1)

        grid.addWidget(patronymic, 2, 0)
        grid.addWidget(patronymicText, 2, 1)

        grid.addWidget(phone, 3, 0)
        grid.addWidget(phoneText, 3, 1)

        grid.addWidget(department, 4, 0)
        grid.addWidget(departmentText, 4, 1)

        grid.addWidget(email, 5, 0)
        grid.addWidget(emailText, 5, 1)

        grid.addWidget(birthday, 6, 0)
        grid.addWidget(birthdayText, 6, 1)

        grid.addWidget(buttonAdd, 7, 0)
        grid.addWidget(buttonCancel, 7, 1)

        buttonAdd.clicked.connect(lambda: self.addUserInDB(firstNameText.text(),lastNameText.text(),
                                                           patronymicText.text(),phoneText.text(),
                                                           departmentText.text(),emailText.text(),
                                                           birthdayText.text()))

        buttonCancel.clicked.connect(self.cancelAdd)
        self.setLayout(grid)

    def addUserInDB(self, var1,var2,var3,var4,var5,var6,var7):
        print(var1 + " " + var2 + " " + var3+ " " + var4+ " " + var5 + " " + var6 + " " + var7)
        db = postgresql.open("pq://postgres:postgres@localhost:5432/book")
        print("er")
        var8 = date.strftime(var7, '%Y-%m-%d')
        var8.date()
        rowquery = db.prepare("select * from user_book")
        row=len(rowquery())
        row=row+1
        print(row)
        print(type(var1))

        print(var8.date() + " " + type(var8))
        query = db.prepare("insert into user_book (id,first_name,second_name,patronymic,phone,department,email,date_of_birth) VALUES ($1,$2,$3,$4,$5,$6,$7,$8)")
        #query(row,var1,var2,var3,var4,var5,var6,var8)

    def cancelAdd(self):
        self.close()