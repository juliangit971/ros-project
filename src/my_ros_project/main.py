#!/usr/bin/env

import sys
import time
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal

from subscriber_nodes.subscriber_node import SensorSubscriber

from gui.main_window import MainWindow
from gui.widgets.main_menu import MainMenuWidget




def main():
    
    # Initialiser l'application PyQt
    app = QApplication(sys.argv)

    # TODO: Faire en sorte que ce popup s'affiche avec le texte à l'intérieur sans que "SensorSubscriber()" le bloque
    # La boucle Qt n'arrive pas à finir d'afficher le popup avant que "SensorSubscriber()" prenne la main et bloque le fil d'exécution
    # msg = QMessageBox()
    # msg.setWindowTitle("ROSCORE needed!")
    # msg.setText("Waiting for \"roscore\" and topic \"sensor_topic\"...")
    # msg.setModal(False)
    # msg.show()
    

    # Initialiser le "subscriber" ROS
    
    ros_subscriber = None
    
    try:
        ros_subscriber = SensorSubscriber()
    except Exception as e:
        print(f"Erreur lors de la 1ère initialisation du Subscriber:\n{e}")

    
    # Abonnement au topic ROS
    ros_subscriber.subscribe() 
    
    
    # Initialisation de la fenêtre principale
    program_window = MainWindow()
    main_widget = MainMenuWidget(ros_subscriber)
    
    program_window.set_widget(main_widget.get_widget())
    

    app.exec()



if __name__ == "__main__":
    main()