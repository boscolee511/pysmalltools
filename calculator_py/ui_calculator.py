# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'computer.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(421, 351)
        self.lineEdit = QLineEdit(widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 10, 361, 81))
        self.lineEdit.setReadOnly(True)
        self.pushButton_7 = QPushButton(widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 140, 75, 24))
        self.pushButton_8 = QPushButton(widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 140, 75, 24))
        self.pushButton_9 = QPushButton(widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(220, 140, 75, 24))
        self.pushButton_4 = QPushButton(widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 190, 75, 24))
        self.pushButton_5 = QPushButton(widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 190, 75, 24))
        self.pushButton_6 = QPushButton(widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(220, 190, 75, 24))
        self.pushButton_1 = QPushButton(widget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 240, 75, 24))
        self.pushButton_2 = QPushButton(widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 240, 75, 24))
        self.pushButton_3 = QPushButton(widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 240, 75, 24))
        self.pushButton_0 = QPushButton(widget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(20, 290, 71, 24))
        self.pushButton_point = QPushButton(widget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        self.pushButton_point.setGeometry(QRect(130, 290, 61, 21))
        self.pushButton_div = QPushButton(widget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setGeometry(QRect(310, 140, 75, 24))
        self.pushButton_mul = QPushButton(widget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        self.pushButton_mul.setGeometry(QRect(310, 190, 75, 24))
        self.pushButton_sub = QPushButton(widget)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        self.pushButton_sub.setGeometry(QRect(310, 240, 75, 24))
        self.pushButton_add = QPushButton(widget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(310, 290, 75, 24))
        self.pushButton_clear = QPushButton(widget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(20, 100, 171, 24))
        self.pushButton_back = QPushButton(widget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(220, 100, 161, 24))
        self.pushButton_equal = QPushButton(widget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setGeometry(QRect(220, 290, 75, 24))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"calculator", None))
        self.pushButton_7.setText(QCoreApplication.translate("widget", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("widget", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("widget", u"9", None))
        self.pushButton_4.setText(QCoreApplication.translate("widget", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("widget", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("widget", u"6", None))
        self.pushButton_1.setText(QCoreApplication.translate("widget", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("widget", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("widget", u"3", None))
        self.pushButton_0.setText(QCoreApplication.translate("widget", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("widget", u".", None))
        self.pushButton_div.setText(QCoreApplication.translate("widget", u"/", None))
        self.pushButton_mul.setText(QCoreApplication.translate("widget", u"x", None))
        self.pushButton_sub.setText(QCoreApplication.translate("widget", u"-", None))
        self.pushButton_add.setText(QCoreApplication.translate("widget", u"+", None))
        self.pushButton_clear.setText(QCoreApplication.translate("widget", u"\u6e05\u7a7a", None))
        self.pushButton_back.setText(QCoreApplication.translate("widget", u"\u56de\u9000", None))
        self.pushButton_equal.setText(QCoreApplication.translate("widget", u"=", None))
    # retranslateUi

