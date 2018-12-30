from PyQt5 import QtGui, QtWidgets, QtCore
import form
import sys


class MyApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self, parents):
        self.app = parents
        QtWidgets.QMainWindow.__init__(self)
        form.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        if parents.applicationName().find(".py") != -1:
            # Python文件运行状态
            url = "file:" + sys.path[0] + "/map/map.html"
        else:
            # 可执行程序运行状态
            url = "file:" + parents.applicationDirPath() + "/map/map.html"
        self.map.load(QtCore.QUrl(url))
        item = QtWidgets.QListWidgetItem()
        item.setText("艾森豪威尔")
        self.target_list.addItem(item)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp(app)
    window.show()
    window.resizeEvent(None)
    sys.exit(app.exec_())
