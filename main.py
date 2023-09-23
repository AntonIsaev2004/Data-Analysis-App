import interface
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = interface.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tabWidget.setCurrentIndex(0)
    MainWindow.show()
    sys.exit(app.exec_())
