from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem
import pyqtgraph as pg

Form, Window = uic.loadUiType('yb.ui')

app = QApplication([])
form = Form()
window = Window()
form.setupUi(window)
window.show()

graph = pg.plot()
form.verticalLayout.addWidget(graph)
# graph.setBackground('w')

def anicolor(txt):
    if txt.lower() == 'млекопитающие':
        return (128, 64, 0)
    if txt.lower() == 'рептилии':
        return (0, 255, 0)
    if txt.lower() == 'рыбы':
        return (0, 0, 255)
    if txt.lower() == 'земноводные':
        return (255, 0, 0)
    if txt.lower() == 'птицы':
        return (0, 255, 255)
    else:
        return (255,255,255)
def new_pr(num, x1, y1, x2, y2, name, col, count):
    pr = QGraphicsRectItem(x1, y1, x2, y2)
    pr.setPen(pg.mkPen(col[0], col[1], col[2]))
    text = pg.TextItem(text = f'{num} - {name} ({count} шт.)')
    text.setPos(x1 + (x1 / 10), y1 + 0.25)
    graph.addItem(pr)
    graph.addItem(text, ignoreBounds = True)

x = [[6 , 2], [0, 3], [0, 1], [7, 10], [5.9, 7]]
y = [[3, 8], [9, 2], [4, 7], [8, 9], [2, 3.5]]
cache_x = []
cache_y = []

for i in range(len(x)):
    var = True
    x_list, y_list = x[i], y[i]
    x1, x2, y1, y2 = min(x_list), max(x_list), min(y_list), max(y_list)
    num = i + 1
    print(x1, x2, y1, y2)
    for i in range(len(cache_x)):
        cac_x, cac_y = cache_x[i], cache_y[i]
        print(cache_x, cache_y)
        cx1, cx2, cy1, cy2 = cac_x[0], cac_x[1], cac_y[0], cac_y[1]
        print(cx1, cx2, cy1, cy2)
        if ((x1 <= cx2 and cx1 <= x2 <= cx2) or (x1 <= cx2 and x2 > cx2)) and (y1 <= cy2 and y2 > cy1):
            print('error')
            var = False
            break
    if var:
        new_pr(num, x1, y1, x2 - x1, y2 - y1, 'name', anicolor('group'), 3)
        cache_x += [[min(x_list), max(x_list)]]
        cache_y += [[min(y_list), max(y_list)]]

app.exec()
