# Digital Clock with custom font

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DIGITAL_CLOCK(QWidget):
    def __init__(self):
        super().__init__()
        
        self.text = QLabel(self)
        self.timer = QTimer(self)
        
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle("My Digital Clock")    
        self.setGeometry(300, 200, 100, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text)
        self.setLayout(vbox) # for text to be vertical 
        
        
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("Font-size: 100px;"
                                      "color: hsl(124, 100%, 61%)")
        self.setStyleSheet("Background-color: Black")
        
        # for time update
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        
        # for font
        font_id = QFontDatabase.addApplicationFont("Font\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        
        self.text.setFont(my_font)
        
        
        self.update_time()
        
        
    def update_time(self):
        # for current time
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.text.setText(current_time)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DIGITAL_CLOCK()
    clock.show()
    sys.exit(app.exec_())
    