from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

from subscriber_nodes.subscriber_node import SensorSubscriber


class MainMenuWidget():
    
    def __init__(self, ros_subscriber: SensorSubscriber):
        
        self.widget = QWidget()
        self.ros_subscriber = ros_subscriber # Référence à l'objet ROSLogic pour accéder aux données du capteur
        self.value = "N/A"
        self.initUI()
        
        # Création d'un QTimer pour actualiser les données ROS périodiquement
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_sensor_data)
        self.timer.start(100) # Actualisation toutes les 100 ms (Exécuter cette fonction chaque 100ms)
        
        
    def initUI(self):
        # Interface graphique avec PyQt5
        self.layout = QVBoxLayout()
        self.label = QLabel(f"Valeur du Capteur: {self.value}")
        self.refresh_button = QPushButton("Resubscribe")
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.refresh_button)
        self.widget.setLayout(self.layout)
        self.widget.setWindowTitle('Interface Capteur ROS')
        self.widget.show()
        
        # Connexion du bouton pour mettre à jour manuellement les données
        self.refresh_button.clicked.connect(self.resubscribe_to_topic)
        
        
    def update_sensor_data(self):
        # Mettre à jour l'étiquette avec la nouvelle valeur des capteurs
        sensor_value = self.ros_subscriber.get_sensor_data()
        self.label.setText(f"Valeur du Capteur: {sensor_value}")
        
    def resubscribe_to_topic(self):
        self.ros_subscriber.unsubscribe()
        self.ros_subscriber.subscribe()
        
        
    def get_widget(self):
        return self.widget