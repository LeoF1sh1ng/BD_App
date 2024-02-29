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
    nomer = (cur.execute('SELECT COUNT(*) FROM zoo'))
    nomer += 1
    x1_y1 = f'{form.x1.rext()}_{form.y1.text()}'
    x2_y2 = f'{form.x2.rext()}_{form.y2.text()}'
    name = form.name.text()
    gruppa = form.comboBox.currentText()
    count = form.spinBox.value()
    cur.execute("""
    INSERT INTO zoo (nomer, x1_y1, x2_y2, name, gruppa, count)
    VALUES (?,?,?,?,?,?)
    """, (nomer, x1_y1, x2_y2, name, gruppa, count))

def delete_bd():
    d_nomer = int(form.name_delete.text())
    cur.execute('DELETE FROM zoo WHERE nomer = ?', (d_nomer,))
    update_id_bd()


def update_id_bd():
    nomer = 1
    lst_id = cur.execute('SELECT id FROM zoo').fetchall()
    for i in lst_id:
        cur.execute('UPDATE zoo SET id = ? WHERE id = ?', (nomer, i))
        nomer += 1

def update_count_bd():
    new_count = int(form.count.text())
    nomer = int(form.number.text())
    cur.execute('UPDATE zoo SET count = ? WHERE nomer = ?', (new_count, nomer,))

def update_graph_from_bd():
    lst = cur.execute('SELECT * FROM zoo').fetchall()
    for i in lst:
        x1_y1 = i[2].split('_')
        x2_y2 = i[3].split('_')
        new_pr(i[1], x1_y1[0], x1_y1[1], x2_y2[0], x2_y2[1], i[4], i[5], i[6])
