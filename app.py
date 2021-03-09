from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
import sys
import numpy as np
from scipy import interpolate


class PlotWidget(QtWidgets.QLabel):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.parent = parent
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.points=[]
        pixmap = QtGui.QPixmap(1300,700)
        self.setPixmap(pixmap)

        #self.label = QtWidgets.QLabel()
        #canvas = QtGui.QPixmap(400, 300)
        #self.label.setPixmap(canvas)
        #self.setCentralWidget(self.label)

        
       
        self.Label_X = QLabel("X :", self)
        self.Label_X.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.Label_Y = QLabel("Y :", self)
        self.Label_Y.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.X_position= QLineEdit(self)
        self.X_position.setGeometry(QtCore.QRect(40, 30, 60, 20))
        self.X_position.setText("0")
        self.Y_position= QLineEdit(self)
        self.Y_position.setGeometry(QtCore.QRect(40, 50, 60, 20))
        self.Y_position.setText("0")

        

    
    """
    def paintEvent(self,e):
        
        self.x=float(self.X_position.text())
        self.y=float(self.Y_position.text())

        painter = QPainter(self)
        pen=QPen(Qt.red)
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawPoint(self.x,self.y)
        self.()
    """    
    def draw_point (self,e):
        
        self.x=float(self.X_position.text())
        self.y=float(self.Y_position.text())
        
        painter = QPainter(self.pixmap())
        pen=QPen(Qt.red)
        pen.setWidth(6)
        painter.setPen(pen)
        painter.drawPoint(self.x,self.y)
        painter.end()
        self.points.append(self.x)
        self.points.append(self.y)
        
        self.update()
        print(self.points)
        
    def drawLine (self, e):
        
        self.x=float(self.X_position.text())
        self.y=float(self.Y_position.text())
        
        painter = QPainter(self.pixmap())
        pen=QPen(Qt.blue)
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawLine(self.x,self.y,self.points[-2],self.points[-1])
        painter.end()
        self.points.append(self.x)
        self.points.append(self.y)
        print(self.points)
        self.update()
    """
    def draw_arc(self):
        
        #print("Input three coordinate of the circle:")
        x1= float(self.points[-6])
        y1= float(self.points[-5])
        x2= float(self.points[-4])
        y2= float(self.points[-3])
        x3= float(self.points[-2])
        y3= float(self.points[-1])
        #x1, y1, x2, y2, x3, y3 = map(float, input().split())
        c = (x1-x2)**2 + (y1-y2)**2
        a = (x2-x3)**2 + (y2-y3)**2
        b = (x3-x1)**2 + (y3-y1)**2
        s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
        px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
        py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
        ar = a**0.5
        br = b**0.5
        cr = c**0.5 
        r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
        print("Radius of the said circle:")
        print("{:>.3f}".format(r))
        print("Central coordinate (x, y) of the circle:")
        print("{:>.3f}".format(px),"{:>.3f}".format(py))
        """
    def draw_arc(self,e):
        x = [self.points[-6],self.points[-4],self.points[-2]]
        y = [self.points[-5],self.points[-3],self.points[-1]]
    
        x2 = np.linspace(x[0], x[-1], 10000)
        y2 = interpolate.pchip_interpolate(x, y, x2)
        
        x_list = x2.tolist()
        y_list = y2.tolist()
       
        painter = QPainter(self.pixmap())
        pen=QPen(Qt.blue)
        pen.setWidth(4)
        painter.setPen(pen)
        
        for i in range(len(x_list)):
            painter.drawPoint(x_list[i],y_list[i])
            #painter.drawLine(x_list[i],y_list[i],x_list[i+1],y_list[i+1])
            print(x_list[i],y_list[i])
        painter.end()
       
        self.update()

    def draw_connect (self, e):
        
        painter = QPainter(self.pixmap())
        pen=QPen(Qt.blue)
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawLine(self.points[0],self.points[1],self.points[-2],self.points[-1])
        painter.end()
        
        self.update()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


        

class TableWidget(QtWidgets.QWidget):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.parent = parent
        self.layout = QtWidgets.QVBoxLayout(self)
        
       
        self.button_widget = QtWidgets.QWidget(self)
        self.layout.addWidget(self.button_widget)

        self.start= QtWidgets.QPushButton(self)
        self.start.setGeometry(QtCore.QRect(10, 90, 80, 50))
        self.start.setText("Start")
        self.start.clicked.connect(self.parent.plot_widget.draw_point)

        self.line = QtWidgets.QPushButton(self)
        self.line.setGeometry(QtCore.QRect(10, 140, 80, 50))
        self.line.setText("Linia")
        self.line.clicked.connect(self.parent.plot_widget.drawLine)

        self.arc = QtWidgets.QPushButton(self)
        self.arc.setGeometry(QtCore.QRect(10, 190, 80, 50))
        self.arc.setText("Łuk")
        self.arc.clicked.connect(self.parent.plot_widget.draw_arc)

        self.split = QtWidgets.QPushButton(self)
        self.split.setGeometry(QtCore.QRect(10, 240, 80, 50))
        self.split.setText("Krzywa")
        

        self.join = QtWidgets.QPushButton(self)
        self.join.setGeometry(QtCore.QRect(10, 290, 80, 50))
        self.join.setText("Połącz")
        self.join.clicked.connect(self.parent.plot_widget.draw_connect)

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(10, 340, 80, 50))
        self.back.setText("Wstecz")

        self.save = QtWidgets.QPushButton(self)
        self.save.setGeometry(QtCore.QRect(10, 450, 80, 50))
        self.save.setText("Zapisz")
        

        self.close_exit = QtWidgets.QPushButton(self)
        self.close_exit.setGeometry(QtCore.QRect(10, 500, 80, 50))
        self.close_exit.setText("koniec")
        self.close_exit.clicked.connect(self.parent.plot_widget.koniec)

        self.close_exit = QtWidgets.QPushButton(self)
        self.close_exit.setGeometry(QtCore.QRect(10, 550, 80, 50))
        self.close_exit.setText("Ustawienia")
       
       



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setGeometry(0, 0, 1440, 700)
        self.setWindowTitle('Skanowanie szablonów')

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        main_layout = QtWidgets.QHBoxLayout(self._main)

        self.plot_widget = PlotWidget(self)
        main_layout.addWidget(self.plot_widget)


        self.table_widget = TableWidget(self)
        main_layout.addWidget(self.table_widget)


#%%
if __name__ == "__main__":
    
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    sys.exit(qapp.exec_())