#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Mason created

used to test the mouse and key capture.
"""

import sys
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel("ddddddd", self)

        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # hbox = QtWidgets.QHBo、xLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(self.label)
        # # self.setCentralWidget(self.label)
        #
        # vbox = QtWidgets.QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        #
        # self.setLayout(vbox)

        self.resize(500, 500)
        self.center()
        self.setWindowTitle('Mouse & Key')

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def keyPressEvent(self, e):
        self.label.setText(e.text())
        self.statusBar().showMessage(e.text())

    def mouseMoveEvent(self, e):
        self.label.setText("("+str(e.x())+","+str(e.y())+")")
        self.statusBar().showMessage("("+str(e.x())+","+str(e.y())+")")

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.label.setText(self.tr("Mouse Left Button Pressed:"))
            self.statusBar().showMessage(self.tr("Mouse Left Button Pressed:"))
        elif e.button() == QtCore.Qt.RightButton:
            self.label.setText(self.tr("Mouse Right Button Pressed:"))
            self.statusBar().showMessage(self.tr("Mouse Right Button Pressed:"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
