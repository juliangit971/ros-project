from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDesktopWidget


class MainWindow():

    window = None

    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("Main Window")
        self.window.setMinimumSize(400,400)
        
        self.center_window()


    # Change the "view" of the main window
    def set_widget(self, widget):
        self.window.setCentralWidget(widget.get_widget())
        self.window.show()
        self.center_window()
        
        
    def center_window(self):        
        qtRectangle = self.window.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()        
        qtRectangle.moveCenter(centerPoint)
        self.window.move(qtRectangle.topLeft())

    def get_mainWindow(self):
        return self.window
    

