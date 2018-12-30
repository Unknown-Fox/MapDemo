from PyQt5 import QtWebEngineWidgets, QtCore


def js_callback(result):
    print(result)


class Map(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parents):
        QtWebEngineWidgets.QWebEngineView.__init__(self, parents)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        point = e.pos()
        x = point.x()
        y = point.y()
        message = str(e.mimeData().data("text/plain"), encoding='utf-8')
        cmd = 'AddMarker(' + str(x) + ',' + str(y) + ',"' + message + '");'
        self.page().runJavaScript(cmd, js_callback)
