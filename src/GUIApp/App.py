import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from data.Repositories.ConcreteAuthenticationRepository import ConcreteAuthenticationRepository
from presentation.Authentication.SignInViewModel import SignInViewModel
from ui.Authentication.SignInView import SignInView

class GUIApp(QWidget):
    signInView = SignInView(viewModel=SignInViewModel(authRepository=ConcreteAuthenticationRepository()))

    def __init__(self):
        super(GUIApp, self).__init__()

        self.stack1 = QWidget()

        self.authenticationViewUI()

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)

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

    def display(self,i):
        self.Stack.setCurrentIndex(i)

def main():
    app = QApplication(sys.argv)
    ex = GUIApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()