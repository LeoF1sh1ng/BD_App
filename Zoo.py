from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QMessageBox
import sqlite3

Form, Window = uic.loadUiType("ItZoo.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


window.show()
app.exec()