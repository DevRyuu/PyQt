# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import ui.main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1032)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{background: transparent;}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"QFrame{background: gray;}")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_control = QStackedWidget(self.frame_main)
        self.stackedWidget_control.setObjectName(u"stackedWidget_control")
        self.stackedWidget_control.setStyleSheet(u"QWidget{max-width: 300px}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QLabel{background-color: rgb(255, 255, 255);}\n"
"QComboBox{background-color: rgb(255, 255, 255);}\n"
"QPushButton{background-color: rgb(255, 255, 255); max-width: 80px;}\n"
"QListView{background-color: rgb(255, 255, 255);}")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 7, 0, 7)
        self.label_filename = QLabel(self.page)
        self.label_filename.setObjectName(u"label_filename")
        font = QFont()
        font.setFamilies([u"\uc5d0\uc2a4\ucf54\uc5b4 \ub4dc\ub9bc 6 Bold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_filename.setFont(font)

        self.verticalLayout_3.addWidget(self.label_filename)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_plantname = QLabel(self.page)
        self.label_plantname.setObjectName(u"label_plantname")
        self.label_plantname.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_plantname)

        self.btn_detection = QPushButton(self.page)
        self.btn_detection.setObjectName(u"btn_detection")
        self.btn_detection.setFont(font)

        self.horizontalLayout_4.addWidget(self.btn_detection)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_partname = QLabel(self.page)
        self.label_partname.setObjectName(u"label_partname")
        self.label_partname.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_partname)

        self.btn_detection_add = QPushButton(self.page)
        self.btn_detection_add.setObjectName(u"btn_detection_add")
        self.btn_detection_add.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_detection_add)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cbox_part = QComboBox(self.page)
        self.cbox_part.addItem("")
        self.cbox_part.setObjectName(u"cbox_part")
        self.cbox_part.setFont(font)

        self.horizontalLayout_6.addWidget(self.cbox_part)

        self.btn_delete_object = QPushButton(self.page)
        self.btn_delete_object.setObjectName(u"btn_delete_object")
        self.btn_delete_object.setFont(font)

        self.horizontalLayout_6.addWidget(self.btn_delete_object)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.btn_reset_detection = QPushButton(self.page)
        self.btn_reset_detection.setObjectName(u"btn_reset_detection")
        self.btn_reset_detection.setFont(font)
        self.btn_reset_detection.setStyleSheet(u"QPushButton{min-width: 290px;}")

        self.verticalLayout_3.addWidget(self.btn_reset_detection, 0, Qt.AlignHCenter)

        self.listView_part = QListView(self.page)
        self.listView_part.setObjectName(u"listView_part")
        font1 = QFont()
        font1.setFamilies([u"\uc5d0\uc2a4\ucf54\uc5b4 \ub4dc\ub9bc 4 Regular"])
        font1.setPointSize(10)
        self.listView_part.setFont(font1)

        self.verticalLayout_3.addWidget(self.listView_part)

        self.verticalSpacer_2 = QSpacerItem(20, 399, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget_control.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_view = QLabel(self.page_2)
        self.label_view.setObjectName(u"label_view")

        self.gridLayout_5.addWidget(self.label_view, 0, 0, 1, 1)

        self.stackedWidget_control.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget_control)

        self.btn_viewMaximize = QPushButton(self.frame_main)
        self.btn_viewMaximize.setObjectName(u"btn_viewMaximize")
        icon = QIcon()
        icon.addFile(u":/left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_viewMaximize.setIcon(icon)
        self.btn_viewMaximize.setIconSize(QSize(25, 50))

        self.horizontalLayout_3.addWidget(self.btn_viewMaximize)

        self.stackedWidget_view = QStackedWidget(self.frame_main)
        self.stackedWidget_view.setObjectName(u"stackedWidget_view")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.page_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"QGraphicsView{border: none; background-color: rgb(255, 255, 255);}\n"
"")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.stackedWidget_view.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_6 = QGridLayout(self.page_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_chart = QFrame(self.page_4)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_chart, 0, 0, 1, 1)

        self.stackedWidget_view.addWidget(self.page_4)

        self.horizontalLayout_3.addWidget(self.stackedWidget_view)


        self.gridLayout.addWidget(self.frame_main, 1, 1, 1, 1)

        self.frame_titlebar = QFrame(self.centralwidget)
        self.frame_titlebar.setObjectName(u"frame_titlebar")
        self.frame_titlebar.setStyleSheet(u"QFrame{background: black; max-height: 52px}\n"
"QPushButton:hover{background-color: white;}")
        self.frame_titlebar.setFrameShape(QFrame.StyledPanel)
        self.frame_titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_titlebar)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 7, 0, 7)
        self.btn_menu = QPushButton(self.frame_titlebar)
        self.btn_menu.setObjectName(u"btn_menu")
        icon1 = QIcon()
        icon1.addFile(u":/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.Btn_info = QPushButton(self.frame_titlebar)
        self.Btn_info.setObjectName(u"Btn_info")
        icon2 = QIcon()
        icon2.addFile(u":/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_info.setIcon(icon2)
        self.Btn_info.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.Btn_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.frame_titlebar)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\uc5d0\uc2a4\ucf54\uc5b4 \ub4dc\ub9bc 9 Black"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel{color: rgb(252, 196, 25);}\n"
"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(self.frame_titlebar)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.widget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        icon3 = QIcon()
        icon3.addFile(u":/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon3)
        self.btn_minimize.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.widget)
        self.btn_maximize.setObjectName(u"btn_maximize")
        icon4 = QIcon()
        icon4.addFile(u":/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon4)
        self.btn_maximize.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.widget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignRight)

        self.widget_3 = QWidget(self.frame_titlebar)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.frame_titlebar, 0, 0, 1, 2)

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"QFrame{background: black; max-width: 76px}\n"
"QPushButton{margin: 9px;}\n"
"QPushButton:hover{background-color: white;}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.frame_menu)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_file = QPushButton(self.widget_4)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setToolTipDuration(100)
        icon6 = QIcon()
        icon6.addFile(u":/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_file.setIcon(icon6)
        self.btn_file.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_file)

        self.btn_menu_detection = QPushButton(self.widget_4)
        self.btn_menu_detection.setObjectName(u"btn_menu_detection")
        icon7 = QIcon()
        icon7.addFile(u":/detection.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_detection.setIcon(icon7)
        self.btn_menu_detection.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_menu_detection)

        self.btn_menu_generation = QPushButton(self.widget_4)
        self.btn_menu_generation.setObjectName(u"btn_menu_generation")
        icon8 = QIcon()
        icon8.addFile(u":/generation.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_generation.setIcon(icon8)
        self.btn_menu_generation.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_menu_generation)

        self.btn_menu_diagnosis = QPushButton(self.widget_4)
        self.btn_menu_diagnosis.setObjectName(u"btn_menu_diagnosis")
        icon9 = QIcon()
        icon9.addFile(u":/diagnosis.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_diagnosis.setIcon(icon9)
        self.btn_menu_diagnosis.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_menu_diagnosis)

        self.btn_menu_solution = QPushButton(self.widget_4)
        self.btn_menu_solution.setObjectName(u"btn_menu_solution")
        icon10 = QIcon()
        icon10.addFile(u":/solution.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_solution.setIcon(icon10)
        self.btn_menu_solution.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_menu_solution)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 510, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_menu)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_menu)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_menu, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_control.setCurrentIndex(1)
        self.stackedWidget_view.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_filename.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85:", None))
        self.label_plantname.setText(QCoreApplication.translate("MainWindow", u"\uc791\ubb3c\uba85:", None))
        self.btn_detection.setText(QCoreApplication.translate("MainWindow", u"\uc778\uc2dd", None))
        self.label_partname.setText(QCoreApplication.translate("MainWindow", u"\uae30\uad00\uba85", None))
        self.btn_detection_add.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00\uc778\uc2dd", None))
        self.cbox_part.setItemText(0, QCoreApplication.translate("MainWindow", u"\uae30\uad00", None))

        self.btn_delete_object.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.btn_reset_detection.setText(QCoreApplication.translate("MainWindow", u"\ucd08  \uae30  \ud654", None))
        self.label_view.setText("")
        self.btn_viewMaximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_menu.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_menu.setText("")
#if QT_CONFIG(tooltip)
        self.Btn_info.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Btn_info.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_info.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ucd08\ubd84\uad11 \uc0dd\uc131 \ubc0f \uc9c4\ub2e8 \uc194\ub8e8\uc158", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_minimize.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_maximize.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_close.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_file.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_file.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_file.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_detection.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_menu_detection.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_menu_detection.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_generation.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_menu_generation.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_menu_generation.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_diagnosis.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_menu_diagnosis.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_menu_diagnosis.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_solution.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_menu_solution.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_menu_solution.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubb34\uc5b8\uac00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ubb34\uc5c7", None))
    # retranslateUi

