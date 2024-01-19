import sys
import os

from ui.ui_mainwindow import Ui_MainWindow
from imageviewer.imageviewer import ImageViewer
from chartviewer.chartviewer import ChartViewer
from tableviewer.tableviewer import TableViewer

from utils.utils import check_directory, check_project_directory, clear_temp_directory, get_path

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    updateRoi = Signal(list)
    updateRect = Signal(object)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.ui.stackedWidget_view.setCurrentIndex(0)
        self.ui.stackedWidget_control.setCurrentIndex(0)
        self.ui.btn_close.clicked.connect(lambda: app.exit())
        self.ui.btn_maximize.clicked.connect(self.toggleMaximized)
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.frame_titlebar.mouseMoveEvent = self.moveWindow
        self.ui.frame_titlebar.mousePressEvent = self.mousePressEvent
        self.ui.btn_viewMaximize.clicked.connect(self.toggleControl)
        self.ui.btn_menu.clicked.connect(self.toggleMenu)

        self.clickPosition = None
        self.dir = os.path.abspath(os.getcwd())

        self.iviewer = ImageViewer(self.ui)
        self.cviewer = ChartViewer(self.ui)

        self.ui.btn_file.clicked.connect(self.get_image)
        self.ui.btn_menu_detection.clicked.connect(self.object_detection)
        self.ui.btn_menu_generation.clicked.connect(self.generate_hyperspectral)

    def toggleMaximized(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.btn_maximize.setIcon(QIcon(u":/maximize.svg"))
            self.ui.btn_maximize.setIconSize(QSize(30, 30))
        else:
            self.showMaximized()
            self.ui.btn_maximize.setIcon(QIcon(u":/maximize_back.svg"))
            self.ui.btn_maximize.setIconSize(QSize(30, 30))

    def moveWindow(self, event):
        if self.isMaximized():
            return
        if self.clickPosition is not None:
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    def toggleMenu(self):
        if self.ui.frame_menu.isVisible():
            self.ui.frame_menu.hide()
        else:
            self.ui.frame_menu.show()

    def toggleControl(self):
        if self.ui.stackedWidget_control.isVisible():
            self.ui.stackedWidget_control.hide()
            self.ui.btn_viewMaximize.setIcon(QIcon(u":/right.svg"))
            self.ui.btn_viewMaximize.setIconSize(QSize(25, 50))
        else:
            self.ui.stackedWidget_control.show()
            self.ui.btn_viewMaximize.setIcon(QIcon(u":/left.svg"))
            self.ui.btn_viewMaximize.setIconSize(QSize(25, 50))

    def _init_directory(self):
        self.imageDir, self.tempDir, self.resultDir = check_directory(self.dir)
        self.inputDir, self.outputDir = check_project_directory(self.imageDir, self.resultDir)
        clear_temp_directory(self.tempDir)

    def get_image(self):
        self.iviewer.path = get_path(self.dir)
        self.iviewer.update_image()
        self.ui.label_filename.setText(f"파일명: {self.iviewer.path[2]}{self.iviewer.path[3]}")

    def object_detection(self):
        self.ui.stackedWidget_control.setCurrentIndex(0)
        self.ui.stackedWidget_view.setCurrentIndex(0)

    def generate_hyperspectral(self):
        self.ui.stackedWidget_control.setCurrentIndex(1)
        self.ui.stackedWidget_view.setCurrentIndex(1)
        self.iviewer.copysource()
        self.cviewer.show_graph()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showMaximized()
    sys.exit(app.exec())
