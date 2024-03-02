from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
form = Form()
window = Window()
form.setupUi(window)
window.show()

plt1 = pg.plot()
plt1.showGrid(x = True, y = True)
form.verticalLayout.addWidget(plt1)

def posible(lst):
    x, y = [], []
    l = 1
    for i in lst:
        x.append(l)
        y.append(i[1])
        text = pg.TextItem(i[0])
        text.setPos(l + 0.5 , 0)
        plt1.addItem(text, ignoreBounce = True)
        l += 1
        print(x, y)
    x.append(l)
    plt1.plot(x, y, stepMode=True, fillLevel = 0, brush = (0, 0, 255))

posible([('1.03.2024', 7), ('2.03.2024', 3), ('3.03.2024', 5)])
app.exec()
