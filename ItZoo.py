from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QMessageBox
import sqlite3

Form, Window = uic.loadUiType("ItZoo.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

window.setWindowTitle("ItZoo")
form.comboBox.addItems(["Млекопитающие", "Рептилии", "Рыбы", "Земноводные", "Птицы"])
form.frame_2.hide()
window.resize(700, 461)

def new_window():
    form.frame.hide()
    form.frame_2.move(0, 0)
    form.frame_2.show()

form.izm.clicked.connect(new_window)

def new_window_2():
    form.frame_2.hide()
    form.frame.show()

form.dobav_val.clicked.connect(new_window_2)

conn = sqlite3.connect('bd.db')
cur = conn.cursor()

conn = sqlite3.connect('zoo.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS zoo (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nomer INTEGER,
x1_y1 TEXT,
x2_y2 TEXT,
name TEXT,
gruppa TEXT,
count INTEGER
)
""")
conn.commit()

def add_bd():
    nomer = len((cur.execute('SELECT * FROM zoo')).fetchall())
    nomer += 1
    x1_y1 = f'{form.x1.text()}_{form.y1.text()}'
    x2_y2 = f'{form.x2.text()}_{form.y2.text()}'
    name = form.name.text()
    gruppa = form.comboBox.currentText()
    count = form.spinBox.value()
    cur.execute("""
    INSERT INTO zoo (nomer, x1_y1, x2_y2, name, gruppa, count)
    VALUES (?,?,?,?,?,?)
    """, (nomer, x1_y1, x2_y2, name, gruppa, count))
    print(cur.execute('SELECT * FROM zoo').fetchall())

def delete_bd():
    d_nomer = int(form.name_delete.text())
    cur.execute('DELETE FROM zoo WHERE nomer = ?', (d_nomer,))
    update_id_bd()
    print(cur.execute('SELECT * FROM zoo').fetchall())


def update_id_bd():
    nomer = 1
    lst_id = cur.execute('SELECT id FROM zoo').fetchall()
    for i in lst_id:
        ids = i[0]
        cur.execute('UPDATE zoo SET nomer = ? WHERE id = ?', (nomer, ids,))
        nomer += 1

def update_count_bd():
    new_count = int(form.count.text())
    nomer = int(form.number.text())
    cur.execute('UPDATE zoo SET count = ? WHERE nomer = ?', (new_count, nomer,))
    print(cur.execute('SELECT * FROM zoo').fetchall())

def update_graph_from_bd():
    lst = cur.execute('SELECT * FROM zoo').fetchall()
    for i in lst:
        x1_y1 = i[2].split('_')
        x2_y2 = i[3].split('_')
        new_pr(i[1], x1_y1[0], x1_y1[1], x2_y2[0], x2_y2[1], i[4], i[5], i[6])

form.dobav.clicked.connect(add_bd)
form.izmenit.clicked.connect(update_count_bd)
form.delete_val.clicked.connect(delete_bd)

window.show()
app.exec()
