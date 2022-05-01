import sys
from PyQt5.QtWidgets import QApplication

#// Custom import
from logic import MainWindow



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())