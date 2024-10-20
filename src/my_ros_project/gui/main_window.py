from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow():

    window = None

    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("Main Widget")
        self.window.setMinimumSize(400,400)
        
        self.center_window()


    # Change the "view" of the main window
    def set_widget(self, widget):
        self.window.setCentralWidget(widget)
        self.window.show()
        self.center_window()
        
        
    def center_window(self):
        qr = self.window.frameGeometry()
        cp = self.window.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
    

