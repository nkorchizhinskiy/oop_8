from PyQt5.QtWidgets import QMainWindow,\
                            QRadioButton,\
                            QComboBox,\
                            QVBoxLayout,\
                            QHBoxLayout,\
                            QLabel,\
                            QWidget,\
                            QDialog




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
        
        self.board = Board()

        
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
        self.board.setStyleSheet(f"background-color: {value};")
        
    def _change_fill(self, value):
        print(f"Change to {value}")
               

               

class Board(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(700)