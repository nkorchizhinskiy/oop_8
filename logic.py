from tkinter import Button
from PyQt5.QtWidgets import QMainWindow,\
                            QRadioButton,\
                            QComboBox,\
                            QVBoxLayout,\
                            QHBoxLayout,\
                            QLabel,\
                            QWidget,\
                            QDialog
from PyQt5.QtGui import QPainter, \
                        QPixmap, \
                        QColor
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, \
                         QPoint




class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self._set_default_settings()
        self._create_widgets()
        self._set_layouts()
        self._set_items_into_combobox()
        self._set_signals_combobox()
    
    def _set_default_settings(self):
        self.setWindowTitle("Графический редактор")
        self.resize(900, 650)
        
    def _create_widgets(self):
        """Create widgets in window"""
        #// Create Labels.
        self.label_instrument = QLabel("Инструменты", self)
        self.label_pallete = QLabel("Палитра", self)
        self.label_line = QLabel("Линия", self)
        self.label_background = QLabel("Фон", self)
        self.label_fill = QLabel("Заливка", self)
        
        #// Create RadioButtons.
        self.radiobutton_line = QRadioButton("Отрезок", self)
        self.radiobutton_ellipse = QRadioButton("Эллипс", self)
        self.radiobutton_rectangle = QRadioButton("Прямоугольник", self)
        
        
        #// Create ComboBox.
        self.combobox_line = QComboBox(self)
        self.combobox_background = QComboBox(self)
        self.combobox_fill = QComboBox(self)
        
        self.board = Board(
            self.radiobutton_line,
            self.radiobutton_ellipse,
            self.radiobutton_rectangle,
            self.combobox_line,
            self.combobox_fill
        )

        
    def _set_layouts(self):
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.label_instrument)
        self.vertical_layout.addWidget(self.radiobutton_line)
        self.vertical_layout.addWidget(self.radiobutton_ellipse)
        self.vertical_layout.addWidget(self.radiobutton_rectangle)
        
        self.vertical_layout.addWidget(self.label_pallete)
        self.vertical_layout.addWidget(self.label_line)
        self.vertical_layout.addWidget(self.combobox_line)
        self.vertical_layout.addWidget(self.label_background)
        self.vertical_layout.addWidget(self.combobox_background)
        self.vertical_layout.addWidget(self.label_fill)
        self.vertical_layout.addWidget(self.combobox_fill)
        
        self.horisontal_layout = QHBoxLayout()
        self.horisontal_layout.addLayout(self.vertical_layout)
        self.horisontal_layout.addWidget(self.board)

        self.setLayout(self.horisontal_layout)

    def _set_items_into_combobox(self):
        #// Combobox Line. 
        self.combobox_line.addItems(["Empty", "Red", "Green", "Blue", "Yellow", "Black", "White"])

        #// Combobox Background.
        self.combobox_background.addItems(["White", "Red", "Green", "Blue", "Yellow", "Black"])

        #// Combobox Fill.
        self.combobox_fill.addItems(["Empty", "Red", "Green", "Blue", "Yellow", "Black", "White"])

    def _set_signals_combobox(self):
        """Set signals on changed values in combobox"""
        self.combobox_line.currentTextChanged.connect(self._change_line)
        self.combobox_background.currentTextChanged.connect(self._change_background)
        self.combobox_fill.currentTextChanged.connect(self._change_fill)
        
    def _change_line(self, value):
        print(f"Change to {value}")
        
    def _change_background(self, value):
        self.board.pixmap.fill(QColor(value))
        self.board.update()
        
    def _change_fill(self, value):
        print(f"Change to {value}")

    #// QPainter.
        
    
               

               

class Board(QDialog):
    
    def __init__(self, radiobutton_line, radiobutton_ellipse, radiobutton_rectangle,
                 combobox_line, combobox_fill):
        super().__init__()
        self.setMinimumWidth(700)
        self.point_start = 0
        self.point_end = 0
        self.pixmap = QPixmap(700, 600)
        self.pixmap.fill(Qt.white)
        self.points = []

        #// Init
        self.radiobutton_line = radiobutton_line
        self.radiobutton_ellipse = radiobutton_ellipse
        self.radiobutton_rectangle = radiobutton_rectangle
        self.combobox_line = combobox_line
        self.combobox_fill = combobox_fill
        
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self.pixmap)
        if self.point_start != 0 and self.point_end != 0:
            print(self.points)
            for figure in self.points:
                if figure[0] == "line":
                    self.painter.drawLine(figure[1], figure[2])

                elif figure[0] == "ellipse":
                    x_center = figure[1].x()
                    y_center = figure[1].y()
                    r_x = figure[2].x() - figure[1].x()
                    r_y = figure[2].y() - figure[1].y()
                    self.painter.drawEllipse(x_center, y_center, r_x, r_y)
                
                elif figure[0] == "rectangle":
                    self.painter.drawRect(figure[1].x(), figure[1].y(), 
                                          figure[2].x() - figure[1].x(), 
                                          figure[2].y() - figure[1].y())
                
        self.painter.end()

        self.painter_2 = QPainter()
        self.painter_2.begin(self)
        self.painter_2.drawPixmap(0, 0, self.pixmap)
        self.painter_2.end()
        
    def mousePressEvent(self, event):
        if self.radiobutton_line.isChecked():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.point_start = event.pos()
        elif self.radiobutton_ellipse.isChecked():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.point_start = event.pos()
        elif self.radiobutton_rectangle.isChecked():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.point_start = event.pos()
            

    def mouseReleaseEvent(self, event):
        def update_dict_with_points(figure):
            if event.button() == QtCore.Qt.LeftButton:
                self.point_end = event.pos()
                self.points.append([f"{figure}", self.point_start, self.point_end])
                self.update()

        if self.radiobutton_line.isChecked():
            print('1')
            update_dict_with_points("line")
        elif self.radiobutton_ellipse.isChecked():
            print('2')
            update_dict_with_points("ellipse")
        elif self.radiobutton_rectangle.isChecked():
            print('3')
            update_dict_with_points("rectangle") 