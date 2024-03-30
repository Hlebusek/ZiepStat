import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QColorDialog
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from DB_Manager import DBM

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.toilet_used = 0
        self.soap_used = 0
        self.percentage = 0
        self.initUI()
        self.DataBaseManager = DBM()


    def initUI(self):
        # izveidojam aplikācijas galveno logu, ar nosaukumu un izmēru
        self.setFixedSize(600, 300)  
        self.setWindowTitle('Analīzes aplikācija')


        # Pievienojam aizmgurējā fona attēlu
        background = QLabel(self)
        background.setGeometry(0, 0, 600, 300)
        background_pixmap = QPixmap('./data/images/background.png')
        background.setPixmap(background_pixmap)
        background.setScaledContents(True)

        # Pievienojam analīzes sākuma un beigu datuma izvēli
        self.start_date = QtWidgets.QCalendarWidget(self)
        self.start_date.setGeometry(10, 200, 140, 90)
        self.start_date.setDateEditAcceptDelay(2000)
        self.start_date.selectionChanged.connect(self.AprekinatRaditajus)
        #
        self.end_date = QtWidgets.QCalendarWidget(self)
        self.end_date.setGeometry(160, 200, 140, 90)
        self.end_date.setDateEditAcceptDelay(2000)
        self.end_date.selectionChanged.connect(self.AprekinatRaditajus)
 
        # pievienojam procentu rādītāja fona bildi
        self.percentage_image = QLabel(self)
        self.percentage_image.setGeometry(300, 0, 300, 300)  
        percentage_pixmap = QPixmap('./data/images/percentage.png')  
        self.percentage_image.setPixmap(percentage_pixmap)
        self.percentage_image.setAttribute(Qt.WA_TranslucentBackground)

        # pievienojam overlay procentu rādītāja fonam
        self.overlay = QLabel(self)
        self.overlay.setGeometry(300, 0, 300, 300)
        self.updateOverlayColor(QColor(0, 0, 0, 100))
        self.overlay.setAttribute(Qt.WA_TranslucentBackground)

        # pievienojam procentu rādītāja tekstu
        self.Percentage_text = QLabel(f'{self.percentage}%', self)
        self.Percentage_text.setGeometry(300, 0, 300, 300)  
        self.Percentage_text.setAlignment(Qt.AlignCenter)
        self.Percentage_text.setFont(QFont('Bahnschrift', 48) )
        self.Percentage_text.setStyleSheet("color: white")  

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
        self.stat_text = QLabel('0/0', self)
        self.stat_text.setGeometry(0, 70, 300, 60)  
        self.stat_text.setAlignment(Qt.AlignCenter)
        self.stat_text.setFont(QFont('Bahnschrift', 32))
        self.stat_text.setStyleSheet("color: white")  

        self.show()


    def get_rgba_color(self,value):
        if value > 100: value = 100
        
        proportion = value / 100
        red = (255, 0, 0)  # Red
        yellow = (255, 255, 0)  # Yellow
        green = (0, 255, 0)  # Green

        if value <= 50:
            # vienkārša interpolācija starp sarkanu un dzeltenu
            r = int((1 - proportion) * red[0] + proportion * yellow[0])
            g = int((1 - proportion) * red[1] + proportion * yellow[1])
            b = int((1 - proportion) * red[2] + proportion * yellow[2])
        else:
            # starp dzeltenu un zaļu
            r = int((1 - proportion) * yellow[0] + proportion * green[0])
            g = int((1 - proportion) * yellow[1] + proportion * green[1])
            b = int((1 - proportion) * yellow[2] + proportion * green[2])
        

        return QColor(r, g, b, 50)


    def updateOverlayColor(self, color):
        overlay_pixmap = self.createCircularOverlay(300, 300, 140, color)
        self.overlay.setPixmap(overlay_pixmap)


    def createCircularOverlay(self, width, height, radius, color):
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(color))
        painter.drawEllipse(width // 2 - radius, height // 2 - radius, 2 * radius, 2 * radius)
        painter.end()
        return pixmap


    def AprekinatProcentuRaditaju(self):
        if self.soap_used == 0 or self.toilet_used == 0: return 0
        return int(self.soap_used/self.toilet_used)

    def AprekinatRaditajus(self):
        start_date = self.start_date.selectedDate().toString("yyyy-MM-dd")
        end_date = self.end_date.selectedDate().toString("yyyy-MM-dd")
        self.toilet_used, self.soap_used = (self.DataBaseManager.GetTimePeriod(start_date, end_date))
        if self.toilet_used is not None and self.soap_used is not None and len(self.toilet_used) != 0:
            self.stat_text.setText(f'{len(self.soap_used)}/{len(self.toilet_used)}')
            self.percentage = int(len(self.soap_used) * 100 / len(self.toilet_used))
            self.Percentage_text.setText(f'{self.percentage}%')
        else:
            self.percentage = 0
            self.Percentage_text.setText('0%')
            self.stat_text.setText('0/0')  
        self.updateOverlayColor(self.get_rgba_color(self.percentage))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
