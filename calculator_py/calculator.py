from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6.QtGui import QIcon
from ui_calculator import Ui_widget


class Mywindows(QWidget, Ui_widget ):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('img.png'))
        self.setupUi(self)
        self.result = ''
        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addnumber('0'))
        self.pushButton_1.clicked.connect(lambda: self.addnumber('1'))
        self.pushButton_2.clicked.connect(lambda: self.addnumber('2'))
        self.pushButton_3.clicked.connect(lambda: self.addnumber('3'))
        self.pushButton_4.clicked.connect(lambda: self.addnumber('4'))
        self.pushButton_5.clicked.connect(lambda: self.addnumber('5'))
        self.pushButton_6.clicked.connect(lambda: self.addnumber('6'))
        self.pushButton_7.clicked.connect(lambda: self.addnumber('7'))
        self.pushButton_8.clicked.connect(lambda: self.addnumber('8'))
        self.pushButton_9.clicked.connect(lambda: self.addnumber('9'))
        self.pushButton_add.clicked.connect(lambda: self.addnumber('+'))
        self.pushButton_sub.clicked.connect(lambda: self.addnumber('-'))
        self.pushButton_mul.clicked.connect(lambda: self.addnumber('*'))
        self.pushButton_div.clicked.connect(lambda: self.addnumber('/'))
        self.pushButton_point.clicked.connect(lambda: self.addnumber('.'))
        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)

    def addnumber(self, numder):
        self.result += numder
        self.lineEdit.setText(self.result)

    def equal(self):
        self.nresult = eval(self.result)
        self.lineEdit.setText(str(self.nresult))


    def clear(self):
        self.result = ''
        self.lineEdit.clear()

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)


if __name__ == '__main__':
    app = QApplication([])
    windows = Mywindows()
    windows.show()
    app.exec()




