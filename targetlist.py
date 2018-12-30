from PyQt5 import QtWidgets, QtCore, QtGui


class TargetList(QtWidgets.QListWidget):
    def __init__(self, parents):
        QtWidgets.QListView.__init__(self, parents)
        self.setDragEnabled(True)

    def startDrag(self, dropActions):
        item = self.currentItem()
        mime_data = QtCore.QMimeData()
        data = bytes(item.text(), encoding='utf8')
        # stream = QtCore.QDataStream(data, QtCore.QIODevice.WriteOnly)
        # stream << self.text << icon
        # stream.writeQString(item.text())
        mime_data.setData("text/plain", data)
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        if drag.exec(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            self.takeItem(self.row(item))

