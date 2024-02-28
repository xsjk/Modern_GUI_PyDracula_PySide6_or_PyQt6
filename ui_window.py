from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPointF
from ui_main import Ui_MainWindow

class MainWindowBase(QMainWindow):
    ui: Ui_MainWindow
    dragPos: QPointF
