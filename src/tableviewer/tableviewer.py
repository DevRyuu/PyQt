from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

class TableViewer(QTableWidget):
    def __init__(self, ui):
        super(TableViewer, self).__init__()
        self.view = ui.view_image
