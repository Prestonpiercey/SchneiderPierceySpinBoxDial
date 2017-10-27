
import datetime
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        curtime = datetime.datetime.now().time()

        thour = int(str(curtime)[0:2])
        tmin = int(str(curtime)[3:5])
        tsec = int(str(curtime)[6:8])

        self.hourdial = QDial()
        self.hourdial.setNotchesVisible(True)
        self.hourdial.setWrapping(True)
        # hourdial.setNotchTarget(12)
        self.hourdial.setRange(0, 12)

        self.mindial = QDial()
        self.mindial.setNotchesVisible(True)
        self.mindial.setWrapping(True)
        # mindial.setNotchTarget(59)
        self.mindial.setRange(0, 59)

        self.secdial = QDial()
        self.secdial.setNotchesVisible(True)
        self.secdial.setWrapping(True)
        # secdial.setNotchTarget(60)
        self.secdial.setRange(0, 59)



        """
        # dial.setStyleSheet("background-color:turquoise;");
        dial.setStyleSheet("color:red");
        # spinbox.setStyleSheet("background-color:red;");
        spinbox.setStyleSheet("color:red");

        dial.setRange(1, int(numRange))
        spinbox.setRange(1, int(numRange))
        # dial.setValue(1)
        # dial.setValue(10)
        """


        layout = QHBoxLayout()
        layout.addWidget(self.hourdial)
        layout.addWidget(self.mindial)
        layout.addWidget(self.secdial)
        self.setLayout(layout)

        self.hourdial.setValue(thour-6)
        self.mindial.setValue(tmin-30)
        self.secdial.setValue(tsec-30)

        self.secdial.valueChanged.connect(self.updateUi)

    def updateUi(self):
        curtime = datetime.datetime.now().time()

        thour = int(str(curtime)[0:2])
        tmin = int(str(curtime)[3:5])
        tsec = int(str(curtime)[6:8])

        self.hourdial.setValue(thour-6)
        self.mindial.setValue(tmin-30)
        self.secdial.setValue(tsec-30)



if __name__ == "__main__":
    datetime.datetime.now().time()
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
