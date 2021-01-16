import pickle
import pyqtgraph as pg
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from thread_cnn import thread_cnn_model
from thread_cnn import thread_cnn_analyze
from thread_cnn import thread_cnn_twiteer
import SQLite_DB_results
import SOLite_hyperparameters


class Ui_MainWindow_main_frame(object):
    def setupUi(self, MainWindow_mainFram, user_name,permission):
        MainWindow_mainFram.setObjectName("MainWindow_mainFram")
        MainWindow_mainFram.resize(1024, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos\\twitter-search_featured-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_mainFram.setWindowIcon(icon)
        MainWindow_mainFram.setStyleSheet("background-color:#F5F5F5")
        self.userID=user_name
        self.centralwidget = QtWidgets.QWidget(MainWindow_mainFram)
        self.centralwidget.setObjectName("centralwidget")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(260, 120, 561, 141))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("photos\\logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(60, 10, 191, 31))
        self.username_label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";")
        self.username_label.setObjectName("username_label")
        self.username_label.setText("Hello "+user_name+"!")
        self.logout_but = QtWidgets.QPushButton(self.centralwidget)
        self.logout_but.setGeometry(QtCore.QRect(40, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.logout_but.setFont(font)
        self.logout_but.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background: ;\n"
"    background-color: ;\n"
"    background-color: ;\n"
"    background-color:  #FFFFFF;\n"
"color:rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";\n"
"border-radius:15px;\n"
"}")
        self.logout_but.setObjectName("logout_but")

        self.frame_Classifcation = QtWidgets.QFrame(self.centralwidget)
        self.frame_Classifcation.setGeometry(QtCore.QRect(20, 260, 981, 501))
        self.frame_Classifcation.setStyleSheet("border-color: transparent;")
        self.frame_Classifcation.setObjectName("frame_Classifcation")
        self.label_Classifcation = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_Classifcation.setGeometry(QtCore.QRect(280, 30, 361, 37))
        self.label_Classifcation.setStyleSheet("color:rgb(0, 0, 0);\n"
                                               "font: 18pt \"Calibri\";\n"
                                               "")
        self.label_Classifcation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Classifcation.setObjectName("label_Classifcation")
        self.upload_but = QtWidgets.QPushButton(self.frame_Classifcation)
        self.upload_but.setGeometry(QtCore.QRect(400, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_but.sizePolicy().hasHeightForWidth())
        self.upload_but.setSizePolicy(sizePolicy)
        self.upload_but.setStyleSheet("QPushButton{\n"
                                      " background:#00BFFF;\n"
                                      "border-radius:15px;\n"
                                      "color:#fff;\n"
                                      "font: 12pt \"Calibri\";\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "background:#0287C3;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "font: 12pt \"Calibri\";\n"
                                      "}")
        self.upload_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photos\\arrow.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.upload_but.setIcon(icon1)
        self.upload_but.setIconSize(QtCore.QSize(50, 30))
        self.upload_but.setObjectName("upload_but")
        self.label_twitterUserName = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_twitterUserName.setGeometry(QtCore.QRect(10, 120, 161, 30))
        self.label_twitterUserName.setStyleSheet("color: rgb(0, 0, 0);\n"
                                                 "font: 12pt \"Calibri\";")
        self.label_twitterUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_twitterUserName.setObjectName("label_twitterUserName")
        self.label_TweetsTest = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_TweetsTest.setGeometry(QtCore.QRect(710, 80, 91, 21))
        self.label_TweetsTest.setStyleSheet("color:rgb(0, 0, 0);\n"
                                            "font: 12pt \"Calibri\";")
        self.label_TweetsTest.setObjectName("label_TweetsTest")
        self.label_amountofTweet = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_amountofTweet.setGeometry(QtCore.QRect(10, 180, 161, 30))
        self.label_amountofTweet.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "font: 12pt \"Calibri\";")
        self.label_amountofTweet.setObjectName("label_amountofTweet")
        self.runanalyze_but = QtWidgets.QPushButton(self.frame_Classifcation)
        self.runanalyze_but.setGeometry(QtCore.QRect(360, 360, 241, 35))
        self.runanalyze_but.setStyleSheet("QPushButton{\n"
                                          " background:#00BFFF;\n"
                                          "border-radius:15px;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "font: 12pt \"Calibri\";\n"
                                          "}\n"
                                          "QPushButton:hover\n"
                                          "{\n"
                                          "background:#0287C3;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "font: 12pt \"Calibri\";\n"
                                          "}")
        self.runanalyze_but.setObjectName("runanalyze_but")
        self.lineEdit_amountofTweet = QtWidgets.QLineEdit(self.frame_Classifcation)
        self.lineEdit_amountofTweet.setGeometry(QtCore.QRect(170, 180, 211, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amountofTweet.sizePolicy().hasHeightForWidth())
        self.lineEdit_amountofTweet.setSizePolicy(sizePolicy)
        self.lineEdit_amountofTweet.setStyleSheet("background:#fff;\n"
                                                  "border-radius:15px;\n"
                                                  "font: 12pt \"Calibri\";")
        self.lineEdit_amountofTweet.setAlignment(QtCore.Qt.AlignLeft)
        self.lineEdit_amountofTweet.setObjectName("lineEdit_amountofTweet")
        self.lineEdit_twitterUserName = QtWidgets.QLineEdit(self.frame_Classifcation)
        self.lineEdit_twitterUserName.setEnabled(True)
        self.lineEdit_twitterUserName.setGeometry(QtCore.QRect(170, 120, 211, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_twitterUserName.sizePolicy().hasHeightForWidth())
        self.lineEdit_twitterUserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_twitterUserName.setFont(font)
        self.lineEdit_twitterUserName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_twitterUserName.setStyleSheet("background:#fff;\n"
                                                    "border-radius:15px;\n"
                                                    "font: 12pt \"Calibri\";")
        self.lineEdit_twitterUserName.setAlignment(QtCore.Qt.AlignLeft)
        self.lineEdit_twitterUserName.setObjectName("lineEdit_twitterUserName")
        self.plainTextEdit_tweetToTest = QtWidgets.QPlainTextEdit(self.frame_Classifcation)
        self.plainTextEdit_tweetToTest.setEnabled(True)
        self.plainTextEdit_tweetToTest.setGeometry(QtCore.QRect(540, 120, 431, 181))
        self.plainTextEdit_tweetToTest.setStyleSheet("background:#fff;\n"
                                                     "border-radius:15px;\n"
                                                     "font: 12pt \"Calibri\";")
        self.plainTextEdit_tweetToTest.setObjectName("plainTextEdit_tweetToTest")
        self.plainTextEdit_tweetToTest.setReadOnly(True)
        self.label_modelName = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_modelName.setGeometry(QtCore.QRect(50, 240, 111, 30))
        self.label_modelName.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "font: 12pt \"Calibri\";")
        self.label_modelName.setObjectName("label_modelName")
        self.comboBox_model = QtWidgets.QComboBox(self.frame_Classifcation)
        self.comboBox_model.setGeometry(QtCore.QRect(170, 240, 211, 33))
        self.comboBox_model.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                          "border-radius:15px;\n"
                                          "font: 12pt \"Calibri\";\n"
                                          "\n"
                                          "")
        self.comboBox_model.setObjectName("comboBox_model")
        self.connection = SQLite_DB_results.connect()
        self.connection_hyperparameters=SOLite_hyperparameters.connect()
        SOLite_hyperparameters.create_table(self.connection_hyperparameters)
        SQLite_DB_results.create_table(self.connection)
        self.set_comboBox_model_name()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.label.setStyleSheet("\n"
"border-radius:30px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos\\iconUser.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 30, 571, 91))
        self.frame.setObjectName("frame")
        if permission==1:
            self.modelSetting_bnt = QtWidgets.QPushButton(self.frame)
            self.modelSetting_bnt.setGeometry(QtCore.QRect(380, 20, 188, 35))
            self.modelSetting_bnt.setStyleSheet("QPushButton{\n"
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
            self.modelSetting_bnt.setObjectName("modelSetting_bnt")
            self.modelSetting_bnt.clicked.connect(self.open_model_setting_form)
            self.modelSetting_bnt.setText( "Model Setting")

        self.classifcation_btn = QtWidgets.QPushButton(self.frame)
        self.classifcation_btn.setGeometry(QtCore.QRect(0, 20, 188, 35))
        self.classifcation_btn.setStyleSheet("QPushButton{\n"
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
        self.classifcation_btn.setObjectName("classifcation_btn")
        self.result_btn = QtWidgets.QPushButton(self.frame)
        self.result_btn.setEnabled(True)
        self.result_btn.setGeometry(QtCore.QRect(190, 20, 188, 35))
        self.result_btn.setStyleSheet("QPushButton{\n"
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
        self.result_btn.setObjectName("result_btn")
        self.result_btn.clicked.connect(self.open_result_form)

        self.dict_frame={
           "frame_classifcation":True,
           "frame_result":False,
           "frame_model_setting":False
          }
        self.dict_result={
            "user_name":[],
            "amount_tweets":[],
            "model_name":[],
            "avg_result":[],
            "graph_result":[]
        }
        self.fetchDB_result()

        MainWindow_mainFram.setCentralWidget(self.centralwidget)
        self.mainwindow_mainFram=MainWindow_mainFram
        self.retranslateUi(MainWindow_mainFram)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_mainFram)
        self.logout_but.clicked.connect(self.open_main_login_GUI)
    def open_main_login_GUI(self):
        from main_login_GUI import Ui_MainWindow_main_login
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_main_login()
        self.ui.setupUi(self.MainWindow)
        self.mainwindow_mainFram.close()
        self.MainWindow.show()



    def set_comboBox_model_name(self):
        self.list_model_name=[]
        tuple_model_DB=SOLite_hyperparameters.get_model_name(self.connection_hyperparameters)
        self.list_model_DB=list(tuple_model_DB)
        print(self.list_model_DB)
        if len(self.list_model_DB)==0:
                self.comboBox_model.addItem('default model')
        else:
            for name in self.list_model_DB:
                test=str(name)
                test = test.strip("('")
                test = test.strip("',)")
                self.comboBox_model.addItem(test)
                self.list_model_name.append(test)



    def fetchDB_result(self):
        analyze_results=[]
        analyze_results=SQLite_DB_results.get_results_by_id(self.connection,self.userID)
        if len(analyze_results)==0:
            return
        else:
            for result in analyze_results:
             self.dict_result["user_name"].append(result[1])
             self.dict_result["amount_tweets"].append(result[2])
             self.dict_result["avg_result"].append(result[3])
             self.dict_result["model_name"].append(result[4])
             self.dict_result["graph_result"].append(result[5])



    def open_model_setting_form(self):
        if not self.dict_frame["frame_model_setting"]:
            for frame, status in self.dict_frame.items():
                if status:
                    self.dict_frame[frame] = False
                    self.frameToHide = frame
                    self.dict_frame["frame_model_setting"] = True
                    break
            if self.frameToHide == "frame_classifcation":
                self.frame_Classifcation.hide()
            else:
                self.frame_result.hide()
            self.setup_model_setting_form(self)
        else: pass


    def buildspiner_uploadtweets(self):
        self.label_gif = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_for_gif = QtWidgets.QLabel(self.frame_Classifcation)
        self.label_for_gif.setGeometry(400, 90, 121, 31)
        self.label_for_gif.setStyleSheet("font: 25 14pt \"Calibri \"background-color:#F5F5F5;")
        self.label_for_gif.setText("Loading tweets...")
        self.label_for_gif.setVisible(True)
        self.label_gif.setGeometry(440, 120, 50, 50)
        self.animation_gif = QMovie("photos\\black_loading.gif")
        self.label_gif.setMovie(self.animation_gif)
        self.animation_gif.start()
        self.label_gif.setVisible(True)


    def treahFinished_loadingModel(self):
        self.label_for_gif.setVisible(False)
        self.label_gif.setVisible(False)
        self.logout_but.setEnabled(True)
        self.runanalyze_but.setEnabled(True)
        self.classifcation_btn.setEnabled(True)
        self.result_btn.setEnabled(True)
        self.modelSetting_bnt.setEnabled(True)
        self.upload_but.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logout_but.setText(_translate("MainWindow", "Logout"))
        self.label_Classifcation.setText(_translate("MainWindow", "Classifcation"))
        self.upload_but.setToolTip(_translate("MainWindow", "Click to extract tweet"))
        self.label_modelName.setText(_translate("MainWindow", "Model name "))
        self.label_twitterUserName.setText(_translate("MainWindow", "Twitter user name "))
        self.label_TweetsTest.setText(_translate("MainWindow", "Tweets"))
        self.label_amountofTweet.setText(_translate("MainWindow", "Amount of Tweet"))
        self.runanalyze_but.setText(_translate("MainWindow", "Run Analyze"))
        self.lineEdit_twitterUserName.setToolTip(_translate("MainWindow", "Enter Twitter user name"))
        self.classifcation_btn.setText(_translate("MainWindow", "Classifcation"))
        self.classifcation_btn.clicked.connect(self.setup_classifcation)
        self.result_btn.setText(_translate("MainWindow", "Result"))
        self.upload_but.clicked.connect(self.upload_tweet)
        self.runanalyze_but.clicked.connect(self.start_analyze)
        self.runanalyze_but.setEnabled(False)

    def fetchDB_hyperarameters(self):
        list_hyperarameters=SOLite_hyperparameters.get_hyperparameters_by_model(self.connection_hyperparameters,self.comboBox_model.currentText())
        return list_hyperarameters[0][1],list_hyperarameters[0][2],list_hyperarameters[0][3],list_hyperarameters[0][4]

    def start_analyze(self):
            self.dict_result["user_name"].append(self.testname)
            if self.newAmountOfTweet!=int(self.amountOfTweet):
                self.dict_result["amount_tweets"].append(self.newAmountOfTweet)
            else:
                self.dict_result["amount_tweets"].append(int(self.amountOfTweet))
            self.dict_result["model_name"].append(self.comboBox_model.currentText())
            filters_number,optimizer,epochs,batch_size=self.fetchDB_hyperarameters()
            self.thread_analyze = thread_cnn_analyze(self.list_tweet_from_twitter,self.comboBox_model.currentText(),filters_number,optimizer,epochs,batch_size)
            self.thread_analyze.commit_analyze.connect(self.treahFinished_RunAnalyze)
            self.thread_analyze.start()



    def treahFinished_RunAnalyze(self,analyze):
        self.runanalyze_but.setEnabled(False)
        print(analyze)
        height=[]
        left=[]
        colors=[]
        tick_label=[]
        avg=0.0
        for x in analyze:
            height.append(float(x))
            avg+=float(x)
        avg=avg/len(analyze)
        self.dict_result["avg_result"].append(avg)
        self.dict_result["graph_result"].append(analyze)
        for i in range(len(analyze)):
            left.append(i)
            tick_label.append('tweet '+str(i+1))

        for tweet in analyze:
            if float(tweet)>0.65:
                colors.append('lightgreen')
            else:
                colors.append('#FF3333')

        plt.bar(left, height, tick_label=tick_label,
                width=0.7, color=colors)

        plt.xlabel('tweets')
        plt.ylabel('percentage %')
        plt.title('Analyze result for - '+str(self.lineEdit_twitterUserName.text()))
        modelTemp=str(self.comboBox_model.currentText())
        amountTemp=int(self.lineEdit_amountofTweet.text())
        UserNameTemp=str(self.lineEdit_twitterUserName.text())
        SQLite_DB_results.add_results(self.connection,self.userID, UserNameTemp, amountTemp,avg,modelTemp,analyze)
        self.lineEdit_twitterUserName.clear()
        self.lineEdit_amountofTweet.clear()
        self.plainTextEdit_tweetToTest.clear()
        plt.show()


    def upload_tweet(self):
        self.testname = str(self.lineEdit_twitterUserName.text())
        self.amountOfTweet=str(self.lineEdit_amountofTweet.text())
        if self.amountOfTweet=='' and self.testname=="":
            self.Warning_QMessageBox_classifcation("You must first enter user name and amount of tweets")
            return
        if self.amountOfTweet=='':
            self.Warning_QMessageBox_classifcation("You must first enter amount of tweets to upload tweets")
        else:
            tempamountOfTweet = int(self.amountOfTweet)
            if self.testname == '':
                self.Warning_QMessageBox_classifcation("You must first enter a user name to upload tweets")
                self.lineEdit_twitterUserName.clear()
            elif int(self.amountOfTweet) < 0 or int(self.amountOfTweet) == 0:
                self.Warning_QMessageBox_classifcation(
                    "The amount of tweets must be a positive number or greater than zero")
                self.lineEdit_amountofTweet.clear()
            elif not isinstance(tempamountOfTweet, int):
                self.Warning_QMessageBox_classifcation("The amount of tweets must be a integer number")
                self.lineEdit_amountofTweet.clear()
            else:
                # self.dict_result["user_name"].append(self.testname)
                # self.dict_result["amount_tweets"].append(int(self.amountOfTweet))
                # self.dict_result["model_name"].append(self.comboBox_model.currentText())

                self.lineEdit_twitterUserName.setEnabled(False)
                self.lineEdit_amountofTweet.setEnabled(False)
                self.comboBox_model.setEnabled(False)
                self.upload_but.setEnabled(False)
                self.buildspiner_uploadtweets()
                self.thread_twiteer = thread_cnn_twiteer(self.testname, int(self.amountOfTweet))
                self.thread_twiteer.commit_tweets.connect(self.treahFinished_extract_tweet)
                self.thread_twiteer.start()




    def Warning_QMessageBox_classifcation(self, str):
        self.msg = QtWidgets.QMessageBox(self.frame_Classifcation)
        self.msg.setGeometry(QtCore.QRect(760, 510, 310, 580))
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(str)
        self.msg.setWindowTitle("Warning")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()


    def treahFinished_extract_tweet(self,list_tweet):
        self.label_for_gif.setVisible(False)
        self.label_gif.setVisible(False)
        self.list_tweet_from_twitter=list_tweet
        self.lineEdit_twitterUserName.setEnabled(True)
        self.lineEdit_amountofTweet.setEnabled(True)
        self.comboBox_model.setEnabled(True)
        self.upload_but.setEnabled(True)
        self.plainTextEdit_tweetToTest.clear()
        if self.list_tweet_from_twitter[0]==-1:
            self.Warning_QMessageBox_classifcation("User dose not exist")
            self.lineEdit_twitterUserName.clear()
            self.lineEdit_amountofTweet.clear()
            return
        elif self.list_tweet_from_twitter[0] == 0:
            self.Warning_QMessageBox_classifcation("This user has no tweets")
            self.runanalyze_but.setEnabled(False)
            self.lineEdit_twitterUserName.clear()
            self.lineEdit_amountofTweet.clear()
            return
        elif len(self.list_tweet_from_twitter) < int(self.amountOfTweet):
            self.newAmountOfTweet=len(self.list_tweet_from_twitter)
            self.Warning_QMessageBox_classifcation("The user have only " + str(len(self.list_tweet_from_twitter)))
        self.plainTextEdit_tweetToTest.verticalScrollBar().minimum()
        for tweet in self.list_tweet_from_twitter:
            self.plainTextEdit_tweetToTest.appendPlainText(str(tweet))
        self.runanalyze_but.setEnabled(True)
        self.newAmountOfTweet = len(self.list_tweet_from_twitter)




    def setup_classifcation(self):
        if not self.dict_frame["frame_classifcation"]:
            for frame, status in self.dict_frame.items():
                if status:
                    self.dict_frame[frame] = False
                    self.frameToHide = frame
                    self.dict_frame["frame_classifcation"] = True
                    break
            if self.frameToHide == "frame_result":
                self.frame_result.hide()
            else:
                self.frame_model_setting.hide()
            self.frame_Classifcation.show()
        else: pass


    def setup_model_setting_form(self,Form):
        self.frame_model_setting = QtWidgets.QFrame(self.centralwidget)
        self.frame_model_setting.setGeometry(QtCore.QRect(20, 260, 981, 501))
        self.frame_model_setting.setObjectName("frame_model_setting")
        self.starttrain_but = QtWidgets.QPushButton(self.frame_model_setting)
        self.starttrain_but.setGeometry(QtCore.QRect(230, 360, 241, 35))
        self.starttrain_but.setStyleSheet("QPushButton{\n"
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
        self.starttrain_but.setObjectName("starttrain_but")

        self.view_models_but = QtWidgets.QPushButton(self.frame_model_setting)
        self.view_models_but.setGeometry(QtCore.QRect(230, 410, 241, 35))
        self.view_models_but.setStyleSheet("QPushButton{\n"
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
        self.view_models_but.setObjectName("view_models_but")

        self.model_acc_Button = QtWidgets.QPushButton(self.frame_model_setting)
        self.model_acc_Button.setGeometry(QtCore.QRect(680, 410, 101, 31))
        self.model_acc_Button.setStyleSheet("QPushButton{\n"
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
        self.model_acc_Button.setObjectName("model_acc_Button")
        self.model_acc_Button.setText("acc graph")
        self.model_acc_Button.setVisible(False)
        self.model_acc_Button.clicked.connect(self.show_acc_graph)

        self.FLAG_GRAPH="train loss"
        self.title_graph="Rumor detection model loss train"
        self.name_to_graph="loss"

        self.label_amountofword = QtWidgets.QLabel(self.frame_model_setting)
        self.label_amountofword.setGeometry(QtCore.QRect(70, 140, 161, 31))
        self.label_amountofword.setStyleSheet("color:rgb(0, 0, 0);\n"
                                              "font: 12pt \"Calibri\";")
        self.label_amountofword.setObjectName("label_amountofword")
        self.lineEdit_bach_size = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_bach_size.setGeometry(QtCore.QRect(230, 240, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bach_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_bach_size.setSizePolicy(sizePolicy)
        self.lineEdit_bach_size.setStyleSheet("background:#fff;\n"
                                              "border-radius:15px;\n"
                                              "font: 12pt \"Calibri\";")
        self.lineEdit_bach_size.setObjectName("lineEdit_bach_size")
        self.label_modelsetting = QtWidgets.QLabel(self.frame_model_setting)
        self.label_modelsetting.setGeometry(QtCore.QRect(160, 10, 361, 51))
        self.label_modelsetting.setStyleSheet("color:rgb(0, 0, 0);\n"
                                              "font: 18pt \"Calibri\";\n"
                                              "")
        self.label_modelsetting.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modelsetting.setObjectName("label_modelsetting")
        self.lineEdit_numberfeaturemaps = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_numberfeaturemaps.setEnabled(True)
        self.lineEdit_numberfeaturemaps.setGeometry(QtCore.QRect(230, 90, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_numberfeaturemaps.sizePolicy().hasHeightForWidth())
        self.lineEdit_numberfeaturemaps.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_numberfeaturemaps.setFont(font)
        self.lineEdit_numberfeaturemaps.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_numberfeaturemaps.setStyleSheet("background:#fff;\n"
                                                      "border-radius:15px;\n"
                                                      "font: 12pt \"Calibri\";")
        self.lineEdit_numberfeaturemaps.setAlignment(QtCore.Qt.AlignLeft)
        self.lineEdit_numberfeaturemaps.setObjectName("lineEdit_numberfeaturemaps")
        self.lineEdit_numberofepoch = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_numberofepoch.setGeometry(QtCore.QRect(230, 190, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_numberofepoch.sizePolicy().hasHeightForWidth())
        self.lineEdit_numberofepoch.setSizePolicy(sizePolicy)
        self.lineEdit_numberofepoch.setStyleSheet("background:#fff;\n"
                                                  "border-radius:15px;\n"
                                                  "font: 12pt \"Calibri\";")
        self.lineEdit_numberofepoch.setObjectName("lineEdit_numberofepoch")


        self.lineEdit_optimizer = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_optimizer.setGeometry(QtCore.QRect(230, 140, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_optimizer.sizePolicy().hasHeightForWidth())
        self.lineEdit_optimizer.setSizePolicy(sizePolicy)
        self.lineEdit_optimizer.setStyleSheet("background:#fff;\n"
                                                 "border-radius:15px;\n"
                                                 "font: 12pt \"Calibri\";")
        self.lineEdit_optimizer.setAlignment(QtCore.Qt.AlignLeft)
        self.lineEdit_optimizer.setObjectName("lineEdit_optimizer")
        self.lineEdit_optimizer.setVisible(False)

        list_optimizers=['Adam','Adadelta','AdaGrad','Nadam','Adagrad','SGD']
        self.comboBox_Optimizer = QtWidgets.QComboBox(self.frame_model_setting)
        self.comboBox_Optimizer.setGeometry(QtCore.QRect(230, 140, 241, 32))
        self.comboBox_Optimizer.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                          "border-radius:15px;\n"
                                          "font: 12pt \"Calibri\";\n"
                                          "\n"
                                          "")
        self.comboBox_Optimizer.setObjectName("comboBox_Optimizer")
        self.comboBox_Optimizer.addItems(list_optimizers)




        self.label_numberfeaturemaps = QtWidgets.QLabel(self.frame_model_setting)
        self.label_numberfeaturemaps.setGeometry(QtCore.QRect(10, 90, 221, 31))
        self.label_numberfeaturemaps.setStyleSheet("color:rgb(0, 0, 0);\n"
                                                   "font: 12pt \"Calibri\";")
        self.label_numberfeaturemaps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_numberfeaturemaps.setObjectName("label_numberfeaturemaps")
        self.label_numberofepoch = QtWidgets.QLabel(self.frame_model_setting)
        self.label_numberofepoch.setGeometry(QtCore.QRect(70, 190, 151, 21))
        self.label_numberofepoch.setStyleSheet("color:rgb(0, 0, 0);\n"
                                               "font: 12pt \"Calibri\";")
        self.label_numberofepoch.setObjectName("label_numberofepoch")
        self.label_bach_size = QtWidgets.QLabel(self.frame_model_setting)
        self.label_bach_size.setGeometry(QtCore.QRect(130, 240, 91, 21))
        self.label_bach_size.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "font: 12pt \"Calibri\";")
        self.label_bach_size.setObjectName("label_bach_size")
        self.label_modelname = QtWidgets.QLabel(self.frame_model_setting)
        self.label_modelname.setGeometry(QtCore.QRect(110, 290, 111, 31))
        self.label_modelname.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "font: 12pt \"Calibri\";")
        self.label_modelname.setObjectName("label_modelname")
        self.lineEdit_modelName = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_modelName.setGeometry(QtCore.QRect(230, 290, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_modelName.sizePolicy().hasHeightForWidth())
        self.lineEdit_modelName.setSizePolicy(sizePolicy)
        self.lineEdit_modelName.setStyleSheet("background:#fff;\n"
                                              "border-radius:15px;\n"
                                              "font: 12pt \"Calibri\";")
        self.lineEdit_modelName.setObjectName("lineEdit_modelName")
        self.gridWidget_graph = QtWidgets.QWidget(self.frame_model_setting)
        self.gridWidget_graph.setGeometry(QtCore.QRect(530, 70, 421, 321))
        self.gridWidget_graph.setObjectName("gridWidget_graph")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget_graph)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_graph_result = QtWidgets.QLabel(self.frame_model_setting)
        self.label_graph_result.setGeometry(QtCore.QRect(530, 10, 361, 51))
        self.label_graph_result.setStyleSheet("color:rgb(0, 0, 0);\n"
                                              "font: 18pt \"Calibri\";\n"
                                              "")
        self.label_graph_result.setVisible(False)
        self.label_graph_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_result.setObjectName("label_graph_result")
        self.label_graph_result.setText( "Graph Result")

        self.lineEdit_batch_size = QtWidgets.QLineEdit(self.frame_model_setting)
        self.lineEdit_batch_size.setGeometry(QtCore.QRect(230, 240, 241, 32))

        sizePolicy.setHeightForWidth(self.lineEdit_batch_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_batch_size.setSizePolicy(sizePolicy)
        self.lineEdit_batch_size.setStyleSheet("background:#fff;\n"
                                                  "border-radius:15px;\n"
                                                  "font: 12pt \"Calibri\";")
        self.lineEdit_batch_size.setObjectName("lineEdit_batch_size")

        self.label_batch_size = QtWidgets.QLabel(self.frame_model_setting)
        self.label_batch_size.setGeometry(QtCore.QRect(130, 240, 91, 21))
        self.label_batch_size.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "font: 12pt \"Calibri\";")
        self.label_batch_size.setObjectName("label_batch_size")
        self.starttrain_but.setText( "Start Train")

        self.view_models_but.setText("view models")

        self.label_modelname.setText("Model name")
        self.label_amountofword.setText( "Optimizer name")
        self.label_modelsetting.setText( "Model Setting")
        self.lineEdit_numberfeaturemaps.setToolTip("Enter a number of feature maps")
        self.lineEdit_numberofepoch.setToolTip("Enter a number of epoch")
        self.lineEdit_batch_size.setToolTip("Enter a number of batch size")
        # self.lineEdit_amountofword.setToolTip("Enter a mount of max sequence length")
        self.lineEdit_modelName.setToolTip("Enter a new name for the model")
        self.label_numberfeaturemaps.setText("Number of feature maps")
        self.label_numberofepoch.setText( "Number of epoch")
        self.label_batch_size.setText("Batch size")
        self.starttrain_but.clicked.connect(self.start_train_new_setting)
        self.view_models_but.clicked.connect(self.setup_view_models)
        self.frame_model_setting.setVisible(True)


    def setup_view_models(self):
        self.model_acc_Button.setVisible(False)
        self.label_modelsetting.setText("Model View")
        self.starttrain_but.setVisible(False)
        self.view_models_but.setVisible(False)
        self.lineEdit_modelName.setVisible(False)
        self.lineEdit_modelName.clear()
        self.lineEdit_batch_size.setEnabled(False)
        self.lineEdit_batch_size.clear()
        self.lineEdit_numberofepoch.setEnabled(False)
        self.lineEdit_numberofepoch.clear()
        # self.lineEdit_amountofword.setEnabled(False)
        # self.lineEdit_amountofword.clear()
        self.lineEdit_optimizer.setVisible(True)
        self.lineEdit_optimizer.setEnabled(False)
        self.comboBox_Optimizer.setVisible(False)
        self.lineEdit_numberfeaturemaps.setEnabled(False)
        self.lineEdit_numberfeaturemaps.clear()
        self.label_graph_result.setVisible(False)
        self.gridWidget_graph.setVisible(False)
        self.comboBox_model_name = QtWidgets.QComboBox(self.frame_model_setting)
        self.comboBox_model_name.setGeometry(QtCore.QRect(230, 290, 241, 32))
        self.comboBox_model_name.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                          "border-radius:15px;\n"
                                          "font: 12pt \"Calibri\";\n"
                                          "\n"
                                          "")
        self.comboBox_model_name.setObjectName("comboBox_model_name")
        self.comboBox_model_name.setVisible(True)
        self.set_comboBox_model_name_view()

        self.view_but = QtWidgets.QPushButton(self.frame_model_setting)
        self.view_but.setGeometry(QtCore.QRect(230, 360, 241, 35))
        self.view_but.setStyleSheet("QPushButton{\n"
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
        self.view_but.setObjectName("view_but")
        self.view_but.setText("view")
        self.view_but.setVisible(True)

        self.delete_but= QtWidgets.QPushButton(self.frame_model_setting)
        self.delete_but.setGeometry(QtCore.QRect(230, 460, 241, 35))
        self.delete_but.setStyleSheet("QPushButton{\n"
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
        self.delete_but.setObjectName("delete_but")
        self.delete_but.setText("delete model")
        self.delete_but.setVisible(True)
        self.delete_but.clicked.connect(self.delete_model)



        self.back_model_setting = QtWidgets.QPushButton(self.frame_model_setting)
        self.back_model_setting.setGeometry(QtCore.QRect(230, 410, 241, 35))
        self.back_model_setting.setStyleSheet("QPushButton{\n"
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
        self.back_model_setting.setObjectName("back_model_setting")
        self.back_model_setting.setText("Back")
        self.back_model_setting.setVisible(True)
        self.back_model_setting.clicked.connect(self.setup_back_modelSetting)
        self.view_but.clicked.connect(self.view_model_hyperparameters)


    def delete_model(self):
        self.modelToDELETE=str(self.comboBox_model_name.currentText())
        SOLite_hyperparameters.delete_model_by_model_name(self.connection_hyperparameters,self.modelToDELETE)
        self.list_model_name.remove(self.modelToDELETE)
        self.set_comboBox_model_name_view()
        self.comboBox_model.clear()
        self.comboBox_model.addItems(self.list_model_name)
        self.Information_QMessageBox_settings(self.modelToDELETE+" has been successfully deleted!")
        self.model_acc_Button.setVisible(False)
        self.label_graph_result.setVisible(False)
        self.setup_view_models()

    def view_model_hyperparameters(self):
        self.gridWidget_graph.setVisible(True)
        list_hyperparameters_DB=SOLite_hyperparameters.get_hyperparameters_by_model(self.connection_hyperparameters,self.comboBox_model_name.currentText())
        print(list_hyperparameters_DB)
        self.lineEdit_batch_size.setText(str(list_hyperparameters_DB[0][4]))
        self.lineEdit_numberofepoch.setText(str(list_hyperparameters_DB[0][3]))
        self.lineEdit_optimizer.setText(str(list_hyperparameters_DB[0][2]))
        self.lineEdit_numberfeaturemaps.setText(str(list_hyperparameters_DB[0][1]))
        self.new_modelName=str(list_hyperparameters_DB[0][0])
        self.label_graph_result.setVisible(True)
        self.load_history()
        self.result_graf()


    def setup_back_modelSetting(self):
        self.delete_but.setVisible(False)
        self.lineEdit_modelName.clear()
        self.lineEdit_modelName.setEnabled(True)
        self.label_graph_result.setVisible(False)
        self.lineEdit_batch_size.clear()
        self.lineEdit_batch_size.setEnabled(True)
        self.lineEdit_numberofepoch.clear()
        self.lineEdit_numberofepoch.setEnabled(True)
        self.lineEdit_optimizer.clear()
        self.lineEdit_optimizer.setVisible(False)
        self.comboBox_Optimizer.setVisible(True)
        self.lineEdit_numberfeaturemaps.clear()
        self.lineEdit_numberfeaturemaps.setEnabled(True)
        self.back_model_setting.setVisible(False)
        self.view_but.setVisible(False)
        self.label_modelsetting.setText("Model Setting")
        self.starttrain_but.setVisible(True)
        self.view_models_but.setVisible(True)
        self.comboBox_model_name.setVisible(False)
        self.lineEdit_modelName.setVisible(True)
        self.model_acc_Button.setVisible(False)
        self.gridWidget_graph.setVisible(False)
        self.graphWidget.setVisible(False)

    def set_comboBox_model_name_view(self):
        if len(self.list_model_name)==0:
                self.comboBox_model_name.addItem('default model')
        else:
            for name in self.list_model_name:
                self.comboBox_model_name.addItem(name)




    def start_train_new_setting(self):
        self.new_numberfeaturemaps = self.lineEdit_numberfeaturemaps.text()
        #self.new_amountofword = self.lineEdit_optimizer.text()
        self.new_optimizer=self.comboBox_Optimizer.currentText()
        self.new_numberofepoch = self.lineEdit_numberofepoch.text()
        self.new_batch_size = self.lineEdit_batch_size.text()
        if self.new_numberfeaturemaps == '' or self.new_numberofepoch == '' or self.new_batch_size == '':
            self.Warning_QMessageBox_settings("One of the hyperparameters is missing")
            return
        try:
            self.new_numberfeaturemaps = int(self.new_numberfeaturemaps)

            self.new_numberofepoch = int(self.new_numberofepoch)
            self.new_batch_size = int(self.new_batch_size)
            if self.new_numberfeaturemaps <= 0 or self.new_numberfeaturemaps > 250:
                self.Warning_QMessageBox_settings("The number of feature maps should be a positive number")
            elif self.new_numberofepoch <= 0:
                self.Warning_QMessageBox_settings("The number of epoch should be a positive number")
            elif self.new_batch_size <= 0:
                self.Warning_QMessageBox_settings("The batch size should be a positive number")
            else:
                self.new_modelName = self.lineEdit_modelName.text()
                if self.new_modelName=='':
                    self.Warning_QMessageBox_settings("A new name for the model is missing")
                    return
                for temp_modelName in self.list_model_name:
                    if self.new_modelName==temp_modelName:
                        self.Warning_QMessageBox_settings("This model name already exists, pick a new name")
                        self.lineEdit_modelName.clear()
                        break
                else:

                    self.buildspiner_buildingNewModel()
                    self.thread_cnn = thread_cnn_model(400,140, self.new_optimizer, self.new_numberofepoch, self.new_batch_size,self.new_numberfeaturemaps,self.new_modelName)
                    self.thread_cnn.commit.connect(self.treahFinished_buldingNewModel)
                    self.thread_cnn.start()
                    self.list_model_name.append(self.new_modelName)

                    self.comboBox_model.addItem(self.new_modelName)

        except ValueError:
            self.Warning_QMessageBox_settings("All the values should be a number")


    def treahFinished_buldingNewModel(self):
        self.gridWidget_graph.setVisible(True)
        self.insert_hyperparameters_DB(self.new_modelName, self.new_numberfeaturemaps, self.new_optimizer,
                                       self.new_numberofepoch, self.new_batch_size)
        self.label_for_gif.setVisible(False)
        self.label_gif.setVisible(False)
        self.Information_QMessageBox_settings('A new model was successfully built')
        self.logout_but.setEnabled(True)
        self.view_models_but.setEnabled(True)
        self.classifcation_btn.setEnabled(True)
        self.result_btn.setEnabled(True)
        self.modelSetting_bnt.setEnabled(True)
        self.load_history()
        self.result_graf()
        self.label_graph_result.setVisible(True)

    def load_history(self):
        dict_history=pickle.load(open('models/history'+self.new_modelName+'.pkl', 'rb'))
        self.temp_val_loss,self.temp_loss,self.temp_acc,self.temp_acc_val,self.list_amount=[],[],[],[],[]
        train_loss=list(dict_history['train_loss'])
        train_val_loss=list(dict_history['train_val_loss'])
        train_acc=list(dict_history['train_acc'])
        train_acc_val=list(dict_history['train_val_acc'])
        for i in train_loss:
            self.temp_loss.append(i)
        for i in train_val_loss:
            self.temp_val_loss.append(i)
        for i in train_acc:
            self.temp_acc.append(i)
        for i in train_acc_val:
            self.temp_acc_val.append(i)
        for i in range(len(self.temp_loss)):
            self.list_amount.append(i+1)


    def show_acc_graph(self):
        if self.FLAG_GRAPH=="train loss":
            self.FLAG_GRAPH="train acc"
            self.title_graph="Rumor detection model acc train"
            self.name_to_graph="acc"
            self.model_acc_Button.setText("loss graph")
            self.graphWidget.close()
            self.result_graf()
        else:
            self.FLAG_GRAPH = "train loss"
            self.title_graph = "Rumor detection model loss train"
            self.name_to_graph = "loss"
            self.model_acc_Button.setText("acc graph")
            self.graphWidget.close()
            self.result_graf()


    def result_graf(self):
        self.model_acc_Button.setVisible(True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle(self.title_graph)
        self.graphWidget.setLabel('left', 'value')
        self.graphWidget.setLabel('bottom', 'epoch')
        self.graphWidget.plotItem.getAxis('left').setPen(pg.mkPen(color=(0, 0, 0), width=1))
        self.graphWidget.plotItem.getAxis('bottom').setPen(pg.mkPen(color=(0, 0, 0), width=1))
        self.gridLayout.addWidget(self.graphWidget, 2, 1)
        self.graphWidget.addLegend()
        if self.FLAG_GRAPH=="train loss":
            self.graphWidget.plot(self.list_amount, self.temp_loss, name="train " + self.name_to_graph,
                                  pen=pg.mkPen(color=(0, 0, 255), symbol='+', symbolSize=30, symbolBrush=('b'),
                                               width=2))
            self.graphWidget.plot(self.list_amount, self.temp_val_loss, name="val " + self.name_to_graph,
                                  pen=pg.mkPen(color=(255, 0, 0), symbol='+', symbolSize=30, symbolBrush=('r'),
                                               width=2))

        else:
            self.graphWidget.plot(self.list_amount, self.temp_acc, name="train " + self.name_to_graph,
                                  pen=pg.mkPen(color=(0, 0, 255), symbol='+', symbolSize=30, symbolBrush=('b'),
                                               width=2))
            self.graphWidget.plot(self.list_amount, self.temp_acc_val, name="val " + self.name_to_graph,
                                  pen=pg.mkPen(color=(255, 0, 0), symbol='+', symbolSize=30, symbolBrush=('r'),
                                               width=2))
        self.graphWidget.setEnabled(True)


    def insert_hyperparameters_DB(self,model_name,filters_number,optimizer,epochs,batch_size):
        SOLite_hyperparameters.add_hyperparameters(self.connection_hyperparameters,model_name,filters_number,optimizer,epochs,batch_size)



    def buildspiner_buildingNewModel(self):
        self.label_gif = QtWidgets.QLabel(self.frame_model_setting)
        self.label_for_gif = QtWidgets.QLabel(self.frame_model_setting)
        self.label_for_gif.setGeometry(620, 70, 250, 75)
        self.label_for_gif.setStyleSheet("font: 25 14pt \"Calibri \"background-color:#F5F5F5;")
        self.label_for_gif.setText("building New model...")
        self.label_for_gif.setVisible(True)
        self.label_gif.setGeometry(600, 120, 250, 200)
        self.animation_gif = QMovie("photos\\blue_spiner3.gif")
        self.label_gif.setMovie(self.animation_gif)
        self.animation_gif.start()
        self.view_models_but.setEnabled(False)
        self.label_gif.setVisible(True)
        self.lineEdit_modelName.setEnabled(False)
        self.lineEdit_batch_size.setEnabled(False)
        self.lineEdit_numberofepoch.setEnabled(False)
        # self.lineEdit_optimizer.setEnabled(False)
        self.comboBox_Optimizer.setEnabled(False)
        self.lineEdit_numberfeaturemaps.setEnabled(False)
        self.logout_but.setEnabled(False)
        self.classifcation_btn.setEnabled(False)
        self.result_btn.setEnabled(False)
        self.modelSetting_bnt.setEnabled(False)
        self.starttrain_but.setEnabled(False)



    def Warning_QMessageBox_settings(self, str):
        self.msg = QtWidgets.QMessageBox(self.frame_model_setting)
        self.msg.setGeometry(QtCore.QRect(760, 510, 310, 580))
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(str)
        self.msg.setWindowTitle("Warning")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    def Information_QMessageBox_settings(self, str):
        self.msg = QtWidgets.QMessageBox(self.frame_model_setting)
        self.msg.setGeometry(QtCore.QRect(760, 510, 310, 580))
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText(str)
        self.msg.setWindowTitle("Information")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    def open_result_form(self):
        if not self.dict_frame["frame_result"]:
            for frame, status in self.dict_frame.items():
                if status:
                    self.dict_frame[frame] = False
                    self.frameToHide = frame
                    self.dict_frame["frame_result"] = True
                    break
            if self.frameToHide == "frame_classifcation":
                self.frame_Classifcation.hide()
            else:
                self.frame_model_setting.hide()
            self.setup_result_form()
        else: pass


    def setup_result_form(self):
        self.frame_result = QtWidgets.QFrame(self.centralwidget)
        self.frame_result.setGeometry(QtCore.QRect(20, 260, 981, 501))
        self.frame_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result.setObjectName("frame_result")
        self.label_result = QtWidgets.QLabel(self.frame_result)
        self.label_result.setGeometry(QtCore.QRect(280, 30, 361, 37))
        self.label_result.setStyleSheet("color:rgb(0, 0, 0);\n"
                                        "font: 18pt \"Calibri\";\n"
                                        "")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.table_result = QtWidgets.QTableWidget(self.frame_result)
        self.table_result.setGeometry(QtCore.QRect(110, 100, 781, 381))
        self.table_result.setStyleSheet("\n"
                                        "font: 12pt \"Calibri\";")
        self.table_result.setStyleSheet("background-color:rgb(255, 255, 255)")
        header_labels = ['User name', 'Amount of tweets', 'Avg detection','Model name', 'Graph result']
        self.table_result.setColumnCount(5)
        self.table_result.setHorizontalHeaderLabels(header_labels)
        self.table_result.setObjectName("table_result")
        self.addTableRow()
        self.label_result.setText("Result")
        self.table_result.setColumnWidth(0,170)
        self.table_result.setColumnWidth(2, 110)
        self.table_result.setColumnWidth(3, 170)
        self.table_result.setColumnWidth(4, 165)
        self.frame_result.setVisible(True)

    def addTableRow(self):
        for i in range(len(self.dict_result["user_name"])):
            avg=self.dict_result["avg_result"][i]
            self.i=i
            col = 0
            self.row=self.table_result.rowCount()
            self.table_result.setRowCount(self.row+1)
            cell_user_name=QTableWidgetItem(self.dict_result["user_name"][i])
            cell_user_name.setTextAlignment(QtCore.Qt.AlignCenter)
            cell_amount_tweets=QTableWidgetItem(str(self.dict_result["amount_tweets"][i]))
            cell_amount_tweets.setTextAlignment(QtCore.Qt.AlignCenter)
            cell_model_name=QTableWidgetItem(self.dict_result["model_name"][i])
            cell_model_name.setTextAlignment(QtCore.Qt.AlignCenter)
            cell_avg_result=QTableWidgetItem(str("{:.3f}%".format(avg*100.0)))
            cell_avg_result.setTextAlignment(QtCore.Qt.AlignCenter)
            if avg<0.65:
                cell_user_name.setBackground(QtGui.QColor(220,20,60))
                cell_amount_tweets.setBackground(QtGui.QColor(220,20,60))
                cell_avg_result.setBackground(QtGui.QColor(220,20,60))
                cell_model_name.setBackground(QtGui.QColor(220,20,60))
            else:
                cell_user_name.setBackground(QtGui.QColor(144,238,144))
                cell_amount_tweets.setBackground(QtGui.QColor(144,238,144))
                cell_avg_result.setBackground(QtGui.QColor(144,238,144))
                cell_model_name.setBackground(QtGui.QColor(144,238,144))

            self.table_result.setItem(self.row, col, cell_user_name)
            col += 1
            self.table_result.setItem(self.row, col, cell_amount_tweets)
            col += 1
            self.table_result.setItem(self.row, col, cell_avg_result)
            col += 1
            self.table_result.setItem(self.row, col, cell_model_name)
            col += 1
            btn = QPushButton(self.table_result)
            btn.setStyleSheet("QPushButton{\n"
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
            btn.setText('analyzed results')
            #btn.clicked.connect(lambda *args, row=self.row, column=col: self.cellClick(self.row, col))
            index = QtCore.QPersistentModelIndex(self.table_result.model().index(self.row, col))
            btn.clicked.connect(
                lambda *args, index=index: self.cellClick(index.row(), index.column()))
            self.table_result.setCellWidget(self.row, col, btn)
            col += 1

    def cellClick(self,row, column):
        analyze=self.dict_result["graph_result"][row]
        print(row)
        print(analyze)
        height=[]
        left=[]
        colors=[]
        tick_label=[]
        for x in analyze:
            height.append(float(x))
        for i in range(len(analyze)):
            left.append(i)
            tick_label.append('tweet '+str(i+1))

        for tweet in analyze:
            if float(tweet)>0.65:
                colors.append('lightgreen')
            else:
                colors.append('#FF3333')
        plt.bar(left, height, tick_label=tick_label,
                width=0.7, color=colors)
        plt.xlabel('tweets')
        plt.ylabel('percentage %')
        plt.title('Analyze result for - '+str(self.dict_result["user_name"][row]))
        plt.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_main_frame()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


