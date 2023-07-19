# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(367, 285)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 230, 261, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit_length = QLineEdit(Form)
        self.lineEdit_length.setObjectName(u"lineEdit_length")
        self.lineEdit_length.setGeometry(QRect(140, 100, 71, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 40, 221, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_a = QCheckBox(self.widget)
        self.checkBox_a.setObjectName(u"checkBox_a")

        self.horizontalLayout.addWidget(self.checkBox_a)

        self.checkBox_A = QCheckBox(self.widget)
        self.checkBox_A.setObjectName(u"checkBox_A")

        self.horizontalLayout.addWidget(self.checkBox_A)

        self.checkBox_0 = QCheckBox(self.widget)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.horizontalLayout.addWidget(self.checkBox_0)

        QWidget.setTabOrder(self.checkBox_0, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.checkBox_a)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"GO", None))
        self.checkBox_a.setText(QCoreApplication.translate("Form", u"a-z", None))
        self.checkBox_A.setText(QCoreApplication.translate("Form", u"A-Z", None))
        self.checkBox_0.setText(QCoreApplication.translate("Form", u"0-9", None))
    # retranslateUi

