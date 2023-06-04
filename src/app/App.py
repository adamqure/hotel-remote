import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from data.Repositories.ConcreteAuthenticationRepository import ConcreteAuthenticationRepository
from presentation.Authentication.SignInViewModel import SignInViewModel
from ui.Authentication.SignInView import SignInView

class stackedExample(QWidget):
    signInView = SignInView(viewModel=SignInViewModel(authRepository=ConcreteAuthenticationRepository()))

    def __init__(self):
        super(stackedExample, self).__init__()

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.authenticationViewUI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)
        self.Stack.addWidget (self.stack2)
        self.Stack.addWidget (self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.setGeometry(300, 50, 10,10)
        self.setWindowTitle('Hotel Remote')
        p = self.palette()
        gradient = QLinearGradient(50, 80, 120, 10)
        gradient.setColorAt(0.0, QColor(140, 84, 251))
        gradient.setColorAt(1.0, QColor(206, 79, 81))
        p.setBrush(self.backgroundRole(), gradient)
        self.setPalette(p)
        self.setFixedHeight(800)
        self.setFixedWidth(1024)
        self.show()

    def authenticationViewUI(self):
        self.stack1.setLayout(self.signInView.getLayout())

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QLineEdit())

        self.stack2.setLayout(layout)


    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)

    def display(self,i):
        self.Stack.setCurrentIndex(i)

def main():
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()