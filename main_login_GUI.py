
from PyQt5.QtWidgets import QMessageBox
import SQLite_DB
from PyQt5 import QtCore, QtGui, QtWidgets


from main_frame import Ui_MainWindow_main_frame
class Ui_MainWindow_main_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos\\twitter-search_featured-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n""background-color:#F5F5F5")
        MainWindow.setWindowTitle("Rumor Detection")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_UserName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_UserName.setGeometry(QtCore.QRect(420, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_UserName.setFont(font)
        self.lineEdit_UserName.setStyleSheet("background:#fff;\n"
"border-radius:15px;\n"
"font: 12pt \"Calibri\";")
        self.lineEdit_UserName.setObjectName("lineEdit_UserName")
        self.lineEdit_UserName.setToolTip("Enter username")
        self.lineEdit_UserName.setPlaceholderText("Username")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(420, 400, 261, 41))
        self.lineEdit_Password.setStyleSheet("background:#fff;\n"
"border-radius:15px;\n"
"font: 12pt \"Calibri\";")
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setToolTip("Enter password")
        self.lineEdit_Password.setPlaceholderText("Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.bnt_login = QtWidgets.QPushButton(self.centralwidget)
        self.bnt_login.setGeometry(QtCore.QRect(420, 480, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bnt_login.setFont(font)
        self.bnt_login.setStyleSheet("QPushButton{\n"
                                      " background:#00BFFF;\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(0, 0, 0);\n"
                                      "font: 12pt \"Calibri\";\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "background:#0287C3;\n"
                                      "color:rgb(0, 0, 0);\n"
                                      "font: 12pt \"Calibri\";\n"
                                      "}")
        self.bnt_login.setObjectName("bnt_login")
        self.bnt_login.setText("Login")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(250, 80, 591, 211))
        self.label_logo.setStyleSheet(" background:transparent;")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("photos\logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.main_login_GUI=MainWindow
        self.fetchDB()
        self.bnt_login.clicked.connect(self.open_main_frame)
    def open_main_frame(self):
        self.user_name_fromUser= self.lineEdit_UserName.text()
        password_fromUser=self.lineEdit_Password.text()
        if password_fromUser=="" and self.user_name_fromUser=="":
            self.lineEdit_UserName.setStyleSheet("border: 1.5px solid red;\n border-radius:15px;")
            self.lineEdit_Password.setStyleSheet("border: 1.5px solid red;\n border-radius:15px;font: 12pt \"Calibri\";")
            return
        if password_fromUser=="":
            self.lineEdit_UserName.setStyleSheet("border-color: 1px rgb(0, 0,0);\n border-radius:15px")
            self.lineEdit_Password.setStyleSheet("border: 1.5px solid red;\n border-radius:15px;font: 12pt \"Calibri\";")
            self.Warning_QMessageBox_classifcation("The password field is empty, pleas enter password")
            return
        if  self.user_name_fromUser=="":
            self.lineEdit_UserName.setStyleSheet("border: 1.5px solid red;\n border-radius:15px")
            self.lineEdit_Password.setStyleSheet("border-color: 1px rgb(0, 0, 0);\n border-radius:15px;font: 12pt \"Calibri\";")
            self.Warning_QMessageBox_classifcation("The user name field is empty, pleas enter user name")
            return
        password_fromUser=int(password_fromUser)
        flag_login=self.check_user(password_fromUser,self.user_name_fromUser)
        if(flag_login):
            self.MainWindow_mainFram = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_main_frame()
            self.ui.setupUi(self.MainWindow_mainFram,self.user_name_fromUser,self.permission)
            self.lineEdit_UserName.setText("")
            self.lineEdit_Password.setText("")
            self.MainWindow_mainFram.show()
            self.main_login_GUI.close()
        else:
            self.Warning_QMessageBox_classifcation("User does not exist")


    def check_user(self,password_fromUser,user_name_fromUser):
        flag=False
        for i in range(len(self.list_user_name)):
            if self.list_user_name[i] == user_name_fromUser and password_fromUser == self.list_password[i]:
                self.permission=self.list_permission[i]
                flag = True
            if flag:
                break
        return flag

    def fetchDB(self):
        self.list_user_name=[]
        self.list_password=[]
        self.list_permission=[]
        connection = SQLite_DB.connect()
        SQLite_DB.create_table(connection)
        users = SQLite_DB.get_all_users(connection)
        for user in users:
            self.list_user_name.append(user[0])
            self.list_password.append(user[1])
            self.list_permission.append(user[2])
        print(self.list_user_name)
        print(self.list_password)
        print(self.list_permission)

    def Warning_QMessageBox_classifcation(self, str):
        self.msg = QtWidgets.QMessageBox(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(760, 510, 310, 580))
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(str)
        self.msg.setWindowTitle("Warning")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_login_GUI = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_main_login()
    ui.setupUi(main_login_GUI)
    main_login_GUI.show()
    sys.exit(app.exec_())
