
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)



        numRange = 5

        dial = QDial()
        dial.setNotchesVisible(True)
        dial.setWrapping(False)
        dial.setNotchTarget(numRange/10)
        spinbox = QSpinBox()


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
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)

        spinbox.valueChanged.connect(dial.setValue)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
