import sys
from pymouse import PyMouse
from PyQt5 import QtCore, QtGui, QtWidgets
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Hello PyQt')
    w.show()
    sys.exit(app.exec_())
