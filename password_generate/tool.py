import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from ui_password import Ui_Form

class Mywindows(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('img_good.png'))
        self.setupUi(self)
        self.pushButton.clicked.connect(self.bind)



    def bind(self):
        length = int(self.lineEdit_length.text())
        charest = ""

        if self.checkBox_a.isChecked():
            charest += "abcdefghijklmnopqrstuvwxyz"
        if self.checkBox_A.isChecked():
            charest += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.checkBox_0.isChecked():
            charest += "0123456789"

        password = "".join(random.choice(charest)for i in range(length))

        self.lineEdit.setText(password)


if __name__ == '__main__':
    app = QApplication([])
    windows = Mywindows()
    windows.show()
    app.exec()