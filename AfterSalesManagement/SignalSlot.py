from PyQt5 import QtCore


class eventMonitor(QtCore.QObject):  # 构建事件监控类
    EnterKeyPressed = QtCore.pyqtSignal()
    GetCurrentText = QtCore.pyqtSignal()

    def eventFilter(self, objwatched, event):
        eventType = event.type()
        flag = eventType == QtCore.QEvent.KeyPress
        if flag:
            ch = event.key()
            # print(f"In eventMonitor eventFilter:键盘按下，按键为：{event.key()}、{event.text()}")
            if ch == QtCore.Qt.Key_Return:
                # print("回车键按下了")
                self.EnterKeyPressed.emit()
        ret = super().eventFilter(objwatched, event)
        return False