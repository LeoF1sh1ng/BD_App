import sqlite3
from PyQt5 import QTableWidgetItem, QMessageBox, QHeaderView

conn = sqlite3.connect('data_base.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS data_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                PU TEXT,
                PRO TEXT,
                OP TEXT)""")
conn.commit()

# def add_data(PU, PRO, OP):
#     sPU = f'{PU[0]}, {PU[1]}, {PU[2]}'
#     sPRO = f'{PRO[0]}, {PRO[1]}, {PRO[2]}'
#     sOP = f'{OP[0]}, {OP[1]}'
#     cur.execute('INSERT INTO data_base (PU, PRO, OP) VALUES (?, ?, ?)', (sPU, sPRO, sOP))

def add_data_PU(PU):
    sPU = f'{PU[0]}, {PU[1]}, {PU[2]}'
    cur.execute('INSERT INTO data_base (PU) VALUES (?)', (sPU,))

def add_data_PRO(PRO):
    sPRO = f'{PRO[0]}, {PRO[1]}, {PRO[2]}'
    cur.execute('INSERT INTO data_base (PRO) VALUES (?)', (sPRO,))

def add_data_OP(OP):
    sOP = f'{OP[0]}, {OP[1]}'
    cur.execute('INSERT INTO data_base (OP) VALUES (?)', (sOP,))



def error_massage(x, y):
    msg = QMessageBox()
    msg.setWindowTitle(f"{x}")
    msg.setText(f"{y}")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


def check_massage(x, y):
    msg = QMessageBox()
    msg.setWindowTitle(f"{x}")
    msg.setText(f"{y}")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()


# def remove_user(id):



def update_table():
    form.tableWidget.setColumnCount(3)
    form.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    form.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ПУ(x, y, дальность'))
    form.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('ПРО(x, y, радиус'))
    form.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('ОП(x, y'))
    form.tableWidget.verticalHeader().setDefaultSectionSize(20)
    form.tableWidget.horizontalHeader().setDefaultSectionSize(60)
    form.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
    form.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

    bd = cur.execute('SELECT * FROM data_base').fetchall()
    form.tableWidget.setRowCount(len(bd))
    for i in range(len(bd)):
        for j range(len(bd[i])):
            form.tableWidget.setItem(i, j, QTableWidgetItem(str(bd[i][j])))
