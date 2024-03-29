import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets





class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.toilet_used = 0
        self.soap_used = 0
        self.percentage = 0

    def initUI(self):
        # izveidojam aplikācijas galveno logu, ar nosaukumu un izmēru
        self.setFixedSize(600, 300)  
        self.setWindowTitle('Analīzes aplikācija')


        # Pievienojam aizmgurējā fona attēlu
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 600, 300)
        background_pixmap = QPixmap('./data/images/background.png')
        self.background.setPixmap(background_pixmap)
        self.background.setScaledContents(True)

        # Pievienojam analīzes sākuma un beigu datuma izvēli
        self.start_date = QtWidgets.QCalendarWidget(self)
        self.start_date.setGeometry(10, 200, 140, 90)
        self.start_date.setDateEditAcceptDelay(2000)
        #
        self.end_date = QtWidgets.QCalendarWidget(self)
        self.end_date.setGeometry(160, 200, 140, 90)
        self.end_date.setDateEditAcceptDelay(2000)
 
        # pievienojam procentu rādītāja fona bildi
        self.percentage_image = QLabel(self)
        self.percentage_image.setGeometry(300, 0, 300, 300)  
        percentage_pixmap = QPixmap('./data/images/percentage.png')  
        self.percentage_image.setPixmap(percentage_pixmap)
        self.percentage_image.setAttribute(Qt.WA_TranslucentBackground)

        # pievienojam procentu rādītāja tekstu
        Percentage_text = QLabel(f'{self.percentage}%', self)
        Percentage_text.setGeometry(300, 0, 300, 300)  
        Percentage_text.setAlignment(Qt.AlignCenter)
        Percentage_text.setFont(QFont('Bahnschrift', 48) )
        Percentage_text.setStyleSheet("color: white")  

        # pievienojam tekstu 'statistika'
        general_text = QLabel('Statistika', self)
        general_text.setGeometry(70, 0, 160, 60)  
        general_text.setAlignment(Qt.AlignCenter)
        general_text.setFont(QFont('Bahnschrift', 24))
        general_text.setStyleSheet("color: white")  

        # pievienojam tekstu 'laika periods'
        date_select_text = QLabel('Laika periods', self)
        date_select_text.setGeometry(30, 130, 260, 60)  
        date_select_text.setAlignment(Qt.AlignCenter)
        date_select_text.setFont(QFont('Bahnschrift', 24))
        date_select_text.setStyleSheet("color: white")  

        # pievienojam rādītāju cik cilvēku izmantoja ziepes
        stat_text = QLabel(f'{self.soap_used}/{self.toilet_used}', self)
        stat_text.setGeometry(0, 70, 300, 60)  
        stat_text.setAlignment(Qt.AlignCenter)
        stat_text.setFont(QFont('Bahnschrift', 32))
        stat_text.setStyleSheet("color: white")  

        self.show()

    def AprekinatProcentuRaditaju(self):
        if self.soap_used == 0 or self.toilet_used == 0: return 0
        return int(self.soap_used/self.toilet_used)

    def AprekinatRaditajus(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
