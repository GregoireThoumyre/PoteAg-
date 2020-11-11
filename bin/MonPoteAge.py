# -*- coding: utf-8 -*-
import sys
import qdarkstyle
from PyQt5 import QtWidgets

from src.graphics import ApplicationWindow

"""
File: window.py
Description: GUI of the main project. Allow the user to display the potager of her mother,
"""

stylesheet = """
    ApplicationWindow {
        background-image: url(../src/data/img/patate.png);
        background-position: center;
    }
"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(stylesheet)
    ex = ApplicationWindow.ApplicationWindow(title="The Potager of The Garden of My Mother")
    ex.show()
    sys.exit(app.exec_())
