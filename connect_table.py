import sqlite3
from PyQt5 import QTableWidgetItem, QMessageBox, QHeaderView

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                UZ TEXT,
                age INTEGER,
                type_komand TEXT)""")
conn.commit()

def add_user(name, UZ, age, type_komand):
    if form.radioButton_profi.isChecked() or form.radioButton_osnova.isChecked():
        if name != '' and UZ != '' and age != 0 and type_komand != '':
            cur.execute('INSERT INTO users (name, UZ, age, type_komand) VALUES', (name, UZ, age, type_komand))
            conn.commit()
            check_massage()
        else:
            error_massage()
    else:
        error_massage()


def error_massage():
    msg = QMessageBox()
    msg.setWindowTitle("Ошибка")
    msg.setText("Введите правильные данные")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


def check_massage():
    msg = QMessageBox()
    msg.setWindowTitle("Добавление в БД")
    msg.setText("Успешно!")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()


def remove_user(id):
    try:
        id = int(id)
        cur.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
    except:
        error_massage()


def update_table():
    form.tableWidget.setColumnCount(5)
    form.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    form.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ID'))
    form.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('ФИО'))
    form.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Учебное Заведение'))
    form.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('Возраст'))
    form.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Команда'))
    form.tableWidget.verticalHeader().setDefaultSectionSize(20)
    form.tableWidget.horizontalHeader().setDefaultSectionSize(60)
    form.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
    form.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

    bd = cur.execute('SELECT * FROM users').fetchall()
    form.tableWidget.setRowCount(len(bd))
    for i in range(len(bd)):
        for j range(len(bd[i])):
            form.tableWidget.setItem(i, j, QTableWidgetItem(str(bd[i][j])))
