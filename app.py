from datetime import datetime
from PyQt5.QtGui import QIcon
from forms.usermanagerForm import Ui_UserManager
from forms.loginForm import Ui_LoginWindow
from forms.registerForm import Ui_RegisterWindow
from forms.userpanelForm import Ui_UserPanel
from forms.userinfoForm import Ui_UserInfoWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit
import sys
import sqlite3


def showMessage(message):
    msg = QMessageBox()
    msg.setText(message)
    msg.setStandardButtons(msg.Ok)
    msg.setDefaultButton(msg.Ok)
    msg.exec()


def showError(message, error):
    msg = QMessageBox()
    msg.setIcon(msg.Critical)
    msg.setText(message)
    msg.setDetailedText(str(error))
    msg.setStandardButtons(msg.Ok)
    msg.setDefaultButton(msg.Ok)
    msg.exec()


class UserManager(QMainWindow):
    def __init__(self):
        super(UserManager, self).__init__()
        self.um = Ui_UserManager()
        self.um.setupUi(self)
        self.setWindowTitle("User Manager")
        self.setWindowIcon(QIcon("icon.png"))
        self.um.exitbtn.clicked.connect(self.close)
        self.um.loginbtn.clicked.connect(self.showLW)
        self.um.registerbtn.clicked.connect(self.showRW)
        self.um.version_lbl.setVisible(False)
        self.um.version_number.setText("v5.1")

    def showLW(self):
        self.l_w = LoginWindow()
        self.l_w.show()
        self.hide()

    def showRW(self):
        self.r_w = RegisterWindow()
        self.r_w.show()
        self.hide()


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.lw = Ui_LoginWindow()
        self.lw.setupUi(self)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("icon.png"))
        self.lw.loginbtn.clicked.connect(self.loginUser)
        self.lw.password_txt.setEchoMode(QLineEdit.Password)
        self.lw.password_txt.returnPressed.connect(self.loginUser)
        self.lw.username_txt.returnPressed.connect(self.loginUser)

    def userPanel(self, name, surname, gender, birthdate, phoneNumber, email, username):
        def showUserInfo():
            global gendern
            if gender == "I prefer don't to specify":
                gendern = "Not Specified"
            else:
                gendern = gender

            global phoneNumbern
            if phoneNumber == "":
                phoneNumbern = "Not Specified"
            else:
                phoneNumbern = f"0{phoneNumber}"
            self.uwindow = QMainWindow()
            self.useri = Ui_UserInfoWindow()
            self.useri.setupUi(self.uwindow)
            self.useri.name_txt.setText(name)
            self.useri.surname_txt.setText(surname)
            self.useri.gender_txt.setText(gendern)
            self.useri.birthdate_txt.setText(birthdate)
            self.useri.phone_number_txt.setText(phoneNumbern)
            self.useri.email_txt.setText(email)
            self.useri.username_txt.setText(username)
            self.useri.groupBox.setTitle(f"Logged as ({username})")
            self.useri.okbtn.clicked.connect(self.close)
            self.uwindow.show()

        def showUserManager():
            self.um = UserManager()
            self.um.show()
            self.hide()

        def logoutUser():
            self.up.username_lbl.clear()
            showMessage("Logged out Successfully.")
            self.window.close()
            showUserManager()

        self.window = QMainWindow()
        self.up = Ui_UserPanel()
        self.up.setupUi(self.window)
        self.setWindowTitle("User Panel")
        self.setWindowIcon(QIcon("icon.png"))
        self.up.username_lbl.setText(username)
        self.up.logout_btn.clicked.connect(logoutUser)
        self.up.userinfo_btn.clicked.connect(showUserInfo)
        self.window.show()
        self.close()

    def loginUser(self):
        username = self.lw.username_txt.text()
        password = self.lw.password_txt.text()

        if username == "":
            showMessage("Please Enter Your Username.")
        elif password == "":
            showMessage("Please Enter Your Password.")
        else:
            try:
                conn = sqlite3.connect(database="db/database.db")
                cur = conn.cursor()
                sql = "Select * from users where username = ? and password = ?"
                cur.execute(sql, [(username), (password)])
                result = cur.fetchall()
                if result:
                    for i in result:
                        showMessage(f"Logged successfully. Welcome {i[6]} !")
                        self.lw.username_txt.clear()
                        self.lw.password_txt.clear()
                        self.userPanel(i[0], i[1], i[2], i[3], i[4], i[5], i[6])

                else:
                    showMessage("Username or password incorrect.")
            except sqlite3.Error as err:
                showError("An Error has occured.", err)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.rw = Ui_RegisterWindow()
        self.rw.setupUi(self)
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("icon.png"))
        self.rw.registerbtn.clicked.connect(self.registerUser)
        self.rw.password_txt.setEchoMode(QLineEdit.Password)
        self.rw.passagain_txt.setEchoMode(QLineEdit.Password)
        self.rw.username_txt.returnPressed.connect(self.registerUser)
        self.rw.password_txt.returnPressed.connect(self.registerUser)
        self.rw.passagain_txt.returnPressed.connect(self.registerUser)

    def registerUser(self):
        name = self.rw.name_txt.text()
        surname = self.rw.surname_txt.text()
        gender = self.rw.gender_cbox.currentText()
        birthdate = self.rw.birthdate_date.text()
        phoneNumber = self.rw.phonenumber_txt.text()
        email = self.rw.email_txt.text()
        username = self.rw.username_txt.text()
        password = self.rw.password_txt.text()
        passagain = self.rw.passagain_txt.text()

        if name == "":
            showMessage("Please Enter Your Name.")
        elif surname == "":
            showMessage("Please Enter Your Surname.")
        elif gender == "<Select Gender>":
            showMessage("Please Select a Gender.")
        elif email == "":
            showMessage("Please Enter a Email.")
        elif username == "":
            showMessage("Please Enter a Username.")
        elif password == "":
            showMessage("Please Enter a Password.")
        elif password == passagain:
            try:
                conn = sqlite3.connect(database="db/database.db")
                cur = conn.cursor()
                sql = "Insert into users(name, surname, gender, birthdate, phoneNumber, email, username, password, createdtime) values (?,?,?,?,?,?,?,?,?)"
                cur.execute(sql,
                            [(name), (surname), (gender), (birthdate), (phoneNumber), (email), (username), (password),
                             (datetime.now())])
                showMessage(f"User : {username} Registered Successfully.")
                self.rw.name_txt.clear()
                self.rw.surname_txt.clear()
                self.rw.gender_cbox.setCurrentIndex(0)
                self.rw.phonenumber_txt.clear()
                self.rw.email_txt.clear()
                self.rw.username_txt.clear()
                self.rw.password_txt.clear()
                self.rw.passagain_txt.clear()
            except sqlite3.Error as err:
                showError("An error has occured", err)
        else:
            showMessage("Passwords don't match.")


def window():
    app = QApplication(sys.argv)
    win = UserManager()
    win.show()
    sys.exit(app.exec_())


window()
