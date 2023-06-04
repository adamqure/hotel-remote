from PyQt5.QtWidgets import QApplication, QLabel, QFormLayout, QPushButton, QMessageBox, QWidget, QFileDialog, QGridLayout, QLineEdit, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegularExpression, Qt
from domain.Constants import employeeIDValidationRegex
from presentation.Authentication.SignInViewModel import SignInViewModel

class SignInView:
    def __init__(self, viewModel: SignInViewModel):
        self._viewModel = viewModel
        self.id = ""
    
    def getLayout(self) -> QFormLayout:
        layout = QFormLayout()
        layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(200, 0, 200, 0)
        formText = QLabel()
        formText.setText("Enter Employee ID")
        formText.setFont(QFont("Arial", 56))
        formText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        employeeIDEditText = QLineEdit()
        employeeIDEditText.setPlaceholderText("Enter Employee ID")
        employeeIDEditText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        employeeIDEditText.textChanged.connect(self.idTextChanged)
        idRegex = QRegularExpression(employeeIDValidationRegex)
        validator = QRegularExpressionValidator(idRegex)
        employeeIDEditText.setValidator(validator)
        submitButton = QPushButton()
        submitButton.setText("Submit")
        submitButton.clicked.connect(lambda: self.buttonPressed(submitButton))
        layout.addRow(formText)
        layout.addRow(employeeIDEditText)
        layout.addRow(submitButton)
        return layout
    
    def idTextChanged(self, text):
        self.id = text
    
    def buttonPressed(self, button: QPushButton):
        print(f"Submit ID Button Pressed. ID={self.id}")
        try:
            self._viewModel.signIn(
                id=self.id
            )
        except:
            self.displayError()

    def displayError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText("Invalid ID")
        msg.setWindowTitle("Error")
        msg.exec_()