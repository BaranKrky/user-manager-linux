# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserInfoWindow(object):
    def setupUi(self, UserInfoWindow):
        UserInfoWindow.setObjectName("UserInfoWindow")
        UserInfoWindow.resize(509, 329)
        self.centralwidget = QtWidgets.QWidget(UserInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 461, 281))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 421, 165))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.name_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.name_txt.setText("")
        self.name_txt.setObjectName("name_txt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_txt)
        self.surname_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.surname_txt.setText("")
        self.surname_txt.setObjectName("surname_txt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surname_txt)
        self.gender_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.gender_txt.setText("")
        self.gender_txt.setObjectName("gender_txt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gender_txt)
        self.birthdate_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.birthdate_txt.setText("")
        self.birthdate_txt.setObjectName("birthdate_txt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthdate_txt)
        self.phone_number_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.phone_number_txt.setText("")
        self.phone_number_txt.setObjectName("phone_number_txt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phone_number_txt)
        self.email_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.email_txt.setText("")
        self.email_txt.setObjectName("email_txt")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email_txt)
        self.username_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.username_txt.setText("")
        self.username_txt.setObjectName("username_txt")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.username_txt)
        self.okbtn = QtWidgets.QPushButton(self.groupBox)
        self.okbtn.setGeometry(QtCore.QRect(180, 240, 89, 25))
        self.okbtn.setObjectName("okbtn")
        UserInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserInfoWindow)
        self.okbtn.clicked.connect(UserInfoWindow.close)
        QtCore.QMetaObject.connectSlotsByName(UserInfoWindow)

    def retranslateUi(self, UserInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        UserInfoWindow.setWindowTitle(_translate("UserInfoWindow", "MainWindow"))
        self.label.setText(_translate("UserInfoWindow", "Name :"))
        self.label_2.setText(_translate("UserInfoWindow", "Surname :"))
        self.label_3.setText(_translate("UserInfoWindow", "Gender :"))
        self.label_4.setText(_translate("UserInfoWindow", "Birthdate :"))
        self.label_5.setText(_translate("UserInfoWindow", "Phone Number :"))
        self.label_6.setText(_translate("UserInfoWindow", "Email :"))
        self.label_7.setText(_translate("UserInfoWindow", "Username :"))
        self.okbtn.setText(_translate("UserInfoWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_UserInfoWindow()
    ui.setupUi(UserInfoWindow)
    UserInfoWindow.show()
    sys.exit(app.exec_())
