import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("светофор.ui", self)

        self.pbvukl.clicked.connect(self.first)
    def first(self):
        self.pbred1.setStyleSheet("""
            Qpbred1{
                background-color: grey;
            }
        """)
        self.pbyel2.setStyleSheet("""
            Qpbyel2{
                background-color: grey;
            }
        """)
        self.pbgr3.setStyleSheet("""
            Qpbgr3{
                background-color: grey;
            }
        """)

        self.pbvkl.clicked.connect(self.second)
    def second(self):
        self.pbred1.setStyleSheet("""
            Qpbred1{
                background-color: red;
        }
    """)
        self.pbyel2.setStyleSheet("""
            Qpbyel2{
               background-color: yellow;
        }
   """)
        self.pbgr3.setStyleSheet("""
            Qpbgr3{
                background-color: green;
        }
   """)





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()