# importing libraries
from PyQt5.QtWidgets import *
import sys


# creating a class
# that inherits the QDialog class
class Window(QDialog):

    # constructor
    def __init__(self):
        super(Window, self).__init__()

        # setting window title
        self.setWindowTitle("Cardmaker")

        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)

        # creating a group box
        self.formGroupBox = QGroupBox("Parameters")

        # creating a line edit
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit2 = QLineEdit()

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

        # get info method called when form is accepted

    def getInfo(self):
        # printing the form information
        print("Person Name : {0}".format(self.nameLineEdit.text()))
        print("Message : {0}".format(self.nameLineEdit2.text()))


        # closing the window
        self.close()

        # creat form method

    def createForm(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("CSV text file"), self.nameLineEdit)
        layout.addRow(QLabel("Message"), self.nameLineEdit2)


        # setting layout
        self.formGroupBox.setLayout(layout)

    # main method


if __name__ == '__main__':
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())