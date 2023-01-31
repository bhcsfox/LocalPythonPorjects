import threading
from time import sleep
from datetime import *
from demo2 import Ui_Form
import sys,time
from PyQt5 import QtWidgets,QtCore

class mydesigner(QtWidgets.QWidget,Ui_Form):
    signal_1 = QtCore.pyqtSignal()  # 不带参数
    def __init__(self):
        # super(mydesigner,self).__init__()
        # QtWidgets.QWidget.__init__(self)
        super().__init__()
        #以上三种继承都可以
        self.setupUi(self)
        # self.pushButton.clicked().connect(self.xianshi)
        self.signal_1.connect(self.xianshi)
        self.pushButton.clicked.connect(self.signal_1_call)
    def xianshi(self):
        time1=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.textEdit.append(time1)

    def signal_1_call(self):
        self.signal_1.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mydesigner()
    myshow.show()
    sys.exit(app.exec_())