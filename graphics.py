from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QGraphicsEllipseItem
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
import pyqtgraph as pg
import math as mh
import numpy as np
import pyqtgraph.examples
import time
Form, Window = uic.loadUiType('test.ui')

app = QApplication([])
form = Form()
window = Window()
# window.setWindowFlags(QtCore.Qt.WindowFrameSection)
window.setFixedSize(721,721)
form.setupUi(window)
window.show()

# pyqtgraph.examples.run()

graph = pg.plot()
graph.setBackground('w')
form.verticalLayout.addWidget(graph)
graph.showGrid(x=True, y=True)
# lst = np.arange(0, 10, 0.01)
# y = [math.sin(i) for i in lst]
# z = [math.cos(i) for i in lst]
# cache_x, cache_y = [], []
# graph.plot(lst, y)
pro_x = [4,1]; pro_y = [4, 5]; pro_r = [4.7, 3.2]
py_x , py_y, py_r = [0, -10], [0, -10], [6.28, 38]
op_x, op_y = [10, 6, 7, -4, 8], [7, 3, 4, 3, 10]
py_r = [i * 2 for i in py_r]
pro_r = [i * 2 for i in pro_r]
def add_pro():
    for i in range(len(pro_x)):
        kryg = QGraphicsEllipseItem(pro_x[i] - pro_r[i] / 2, pro_y[i] - pro_r[i] / 2, pro_r[i], pro_r[i])
        kryg.setPen(pg.mkPen((0,3)))
        dot = QGraphicsEllipseItem((pro_x[i]) - 0.1, (pro_y[i]) - 0.1, 0.2, 0.2)
        dot.setPen(pg.mkPen((255, 255, 255)))
        dot.setBrush(pg.mkBrush((0, 0, 255)))
        graph.addItem(kryg)
        graph.addItem(dot)

def add_py():
    for i in range(len(py_x)):
        kryg = QGraphicsEllipseItem(py_x[i] - py_r[i] / 2, py_y[i]-py_r[i] / 2, py_r[i], py_r[i])
        kryg.setPen(pg.mkPen((0, 2)))
        dot = QGraphicsEllipseItem((py_x[i]) - 0.1, (py_y[i]) - 0.1 , 0.2, 0.2)
        dot.setPen(pg.mkPen((255, 255, 255)))
        dot.setBrush(pg.mkBrush((0, 255, 0)))
        graph.addItem(kryg)
        graph.addItem(dot)

def add_op():
    for i in range(len(op_x)):
        dot = QGraphicsEllipseItem(op_x[i] - 0.1, op_y[i] - 0.1, 0.2, 0.2)
        dot.setPen(pg.mkPen((255, 255, 255)))
        dot.setBrush(pg.mkBrush((255,0,0)))
        graph.addItem(dot)


def sf(x_circle, y_circle, r_circle, x1, y1, x2, y2):
    # Расстояние от центра окружности до отрезка
    dx = x2 - x1
    dy = y2 - y1

    # Вычисление ближайшей точки к центру окружности на отрезке
    closest_x = x1 + dx * ((x_circle - x1) * dx + (y_circle - y1) * dy) / (dx**2 + dy**2)
    closest_y = y1 + dy * ((x_circle - x1) * dx + (y_circle - y1) * dy) / (dx**2 + dy**2)

    # Проверка: если ближайшая точка внутри отрезка и расстояние до центра окружности меньше радиуса
    if x1 <= closest_x <= x2 and y1 <= closest_y <= y2 and mh.sqrt((closest_x - x_circle)**2 + (closest_y - y_circle)**2) <= r_circle:
        return True
    else:
        return False

    # Если траектория мортиры пересекает зону воздействия ветра
    if abs(angle_to_target) <= wind_effect:
        return False

    # Досягаемость точки поражения радиусом мортиры
    if mh.sqrt((x_mortar - x_target)**2 + (y_mortar - y_target)**2) <= r_mortar:
        return True

    return False

def res():
    x_lst, y_lst = [], []
    var_lst = []
    for i in range(len(py_x)):
        x_py = py_x[i]
        y_py = py_y[i]
        r_py = py_r[i] / 2

        for j in range(len(op_x)):
            x_op = op_x[j]
            y_op = op_y[j]
            var_py = []
            cache_x, cache_y = [], []
            for k in range(len(pro_x)):
                x_pro, y_pro, r_pro = pro_x[k], pro_y[k], pro_r[k] / 2

            # print(x_py, y_py, r_py)

                print(f'Точка :{x_op}, {y_op}')
                print(f'ПВО: {x_pro}, {y_pro}')
                print(f'mortar: {x_py}, {y_py}')
                if mh.sqrt(abs(x_pro - x_py) ** 2 + abs(y_pro - y_py) ** 2) <= r_pro:
                    var_py += [False]
                    break
                else:
                    var_py += [True]
                if mh.sqrt(((x_op - x_py) ** 2) + (y_op - y_py) ** 2) > r_py:
                    print('no1')
                    var_py += [False]
                elif mh.sqrt(((x_op - x_pro) ** 2) + (y_op - y_pro) ** 2) <= r_pro:
                    print('no2')
                    var_py += [False]
                    # if [x_py, x_op] in x_lst and [y_py, y_op] in y_lst:
                    #     ind = x_lst.index([y_py, y_op])
                    #     if var_lst[i] == True:
                    #         var_lst += [False]
                else:
                    if not(sf(x_pro, y_pro, r_pro, x_py, y_py, x_op, y_op)):
                        if not(False in var_py):
                            var_py += [True]
                            cache_x += [[x_py, x_op]]
                            cache_y += [[y_py, y_op]]
                    else:
                        var_py += [False]
            else:
                print(var_py)
                if len(var_py) == sum(var_py):
                    x_lst += cache_x
                    y_lst += cache_y
                    # var_lst += [True]
                    print('yes')
    for i in range(len(var_lst)):
        print(x_lst, y_lst, var_lst, sep = '\n')
        if var_lst[i] == False:
            del x_lst[i]
            del y_lst[i]
    for i in range(len(x_lst)):
        graph.plot(x_lst[i], y_lst[i], pen = 'g')

form.add_pro.clicked.connect(add_pro)
form.add_py.clicked.connect(add_py)
form.add_op.clicked.connect(add_op)
form.res.clicked.connect(res)




app.exec()
