import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 300)  
        self.setWindowTitle('Analīzes aplikācija')


        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.dateedit.setGeometry(20, 20, 40, 40)
        #self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())


        # Set background image
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 600, 300)
        background_pixmap = QPixmap('./data/images/background.png')
        self.background.setPixmap(background_pixmap)
        self.background.setScaledContents(True)

        # Add percentage image
        self.percentage_image = QLabel(self)
        self.percentage_image.setGeometry(300, 0, 300, 300)  
        percentage_pixmap = QPixmap('./data/images/percentage.png')  
        self.percentage_image.setPixmap(percentage_pixmap)
        self.percentage_image.setScaledContents(True)
        self.percentage_image.setAttribute(Qt.WA_TranslucentBackground)

        # Add text on the percentage image
        Percentage_text = QLabel('75%', self)
        Percentage_text.setGeometry(300, 0, 300, 300)  
        Percentage_text.setAlignment(Qt.AlignCenter)
        font = QFont('Bahnschrift', 48)  
        Percentage_text.setFont(font)
        Percentage_text.setStyleSheet("color: purple")  

        # Add general text
        Percentage_text = QLabel('Statistika', self)
        Percentage_text.setGeometry(60, 0, 160, 60)  
        Percentage_text.setAlignment(Qt.AlignCenter)
        font = QFont('Bahnschrift', 24)  
        Percentage_text.setFont(font)
        Percentage_text.setStyleSheet("color: purple")  





        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
