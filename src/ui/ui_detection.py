# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detection.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Detection(object):
    def setupUi(self, Detection):
        if not Detection.objectName():
            Detection.setObjectName(u"Detection")
        Detection.resize(361, 976)
        Detection.setStyleSheet(u"QLabel{font: }\n"
"QPushbutton{}")
        self.verticalLayout = QVBoxLayout(Detection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_filename = QLabel(Detection)
        self.label_filename.setObjectName(u"label_filename")
        font = QFont()
        font.setFamilies([u"\uc5d0\uc2a4\ucf54\uc5b4 \ub4dc\ub9bc 6 Bold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_filename.setFont(font)

        self.verticalLayout.addWidget(self.label_filename)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_plantname = QLabel(Detection)
        self.label_plantname.setObjectName(u"label_plantname")
        self.label_plantname.setFont(font)

        self.horizontalLayout.addWidget(self.label_plantname)

        self.btn_detection = QPushButton(Detection)
        self.btn_detection.setObjectName(u"btn_detection")
        self.btn_detection.setFont(font)

        self.horizontalLayout.addWidget(self.btn_detection)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_partname = QLabel(Detection)
        self.label_partname.setObjectName(u"label_partname")
        self.label_partname.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_partname)

        self.btn_detection_add = QPushButton(Detection)
        self.btn_detection_add.setObjectName(u"btn_detection_add")
        self.btn_detection_add.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_detection_add)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cbox_part = QComboBox(Detection)
        self.cbox_part.addItem("")
        self.cbox_part.setObjectName(u"cbox_part")
        self.cbox_part.setFont(font)

        self.horizontalLayout_3.addWidget(self.cbox_part)

        self.btn_delete_object = QPushButton(Detection)
        self.btn_delete_object.setObjectName(u"btn_delete_object")
        self.btn_delete_object.setFont(font)

        self.horizontalLayout_3.addWidget(self.btn_delete_object)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_reset_detection = QPushButton(Detection)
        self.btn_reset_detection.setObjectName(u"btn_reset_detection")
        self.btn_reset_detection.setFont(font)

        self.verticalLayout.addWidget(self.btn_reset_detection)

        self.listView_part = QListView(Detection)
        self.listView_part.setObjectName(u"listView_part")
        font1 = QFont()
        font1.setFamilies([u"\uc5d0\uc2a4\ucf54\uc5b4 \ub4dc\ub9bc 4 Regular"])
        font1.setPointSize(10)
        self.listView_part.setFont(font1)

        self.verticalLayout.addWidget(self.listView_part)

        self.verticalSpacer = QSpacerItem(20, 399, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Detection)

        QMetaObject.connectSlotsByName(Detection)
    # setupUi

    def retranslateUi(self, Detection):
        Detection.setWindowTitle(QCoreApplication.translate("Detection", u"Form", None))
        self.label_filename.setText(QCoreApplication.translate("Detection", u"\ud30c\uc77c\uba85:", None))
        self.label_plantname.setText(QCoreApplication.translate("Detection", u"\uc791\ubb3c\uba85:", None))
        self.btn_detection.setText(QCoreApplication.translate("Detection", u"\uc778\uc2dd", None))
        self.label_partname.setText(QCoreApplication.translate("Detection", u"\uae30\uad00\uba85", None))
        self.btn_detection_add.setText(QCoreApplication.translate("Detection", u"\ucd94\uac00\uc778\uc2dd", None))
        self.cbox_part.setItemText(0, QCoreApplication.translate("Detection", u"\uae30\uad00", None))

        self.btn_delete_object.setText(QCoreApplication.translate("Detection", u"\uc0ad\uc81c", None))
        self.btn_reset_detection.setText(QCoreApplication.translate("Detection", u"\ucd08\uae30\ud654", None))
    # retranslateUi

