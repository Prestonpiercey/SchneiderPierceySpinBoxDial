
# DIALS AND BOXES!

## This is a program that demonstrates the usage of signals and slots in PyQt

### It makes use of the high-level communication system built into PyQt, which are commonly referred to as 'signals and slots'. High-level is used because we need to know that something happened, not the details of said incident. Low-level gives more information than is needed.

#### All QObjects support the "signals and slots" mechanism. The signals are always there, but by default are thrown away by Qt.                  To make use of these signals we need to connect them to a slot, which in PyQt is any callable function or method. This makes it             easier to create new slots that were not there originally. 

#####  This block of code is what imports the modules we need to run our program, sys, which lets us actually run the program, and three modules from the module PyQt5. These are .QtCore, .QtGui, and .QtWidgets, which are the core module needed for anything else, the module that allows us to work with GUIs, and the module that gives us the abillity to make widgets for the aforementioned GUIs respectively.


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
```

##### Here, we define the class Form, which inherits QDialog, i.e. dialog windows, from PyQt5. First we give it the method __init__ as usual, then use super to make acessing the class easier. This is the base framework which allows us to open up a window and do things with it.


```python
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
```

##### In this block, we set up the widgets, spinbox and dial, that we will use. First, we set the range of numbers we want to allow on the dial, then generate the dial. Then we then make the notches visible, and set the number of notches using the range we defined earlier. Then we generate the spinbox we will use. 


```python
        numRange = 100

        dial = QDial()
        dial.setNotchesVisible(True)
        dial.setWrapping(False)
        dial.setNotchTarget(numRange/10)
        spinbox = QSpinBox()
```

##### This code block adds the widgets created in the previous block to the box's layout. This is what makes the widgets show up in the window.


```python
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
```

##### This makes it so that when the value in the spinbox is changed by the user it also changes the value of the dial and turns it, and vice-versa. This is essential the only moving part of of the program, and is the implementation of the signals and slots that were explained earlier. In the first line, we connect the slot which is the setValue method of spinbox, which changes the value of the spinbox according to the valueChange signal that is given by the dial. The same is done for the dial from the spinbox value. 


```python
        dial.valueChanged.connect(spinbox.setValue)

        spinbox.valueChanged.connect(dial.setValue)
```

##### Finally, this code actually generates everything and enables it to be interacted with. It opens a windows and tells it to show an instance of the form we just created.


```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
```
