#!/usr/bin/env

import rospy
from std_msgs.msg import Int32
from subscriber_nodes.subscriber_superclass import SubscriberSuperclass



class SensorSubscriber(SubscriberSuperclass):

    def __init__(self):
        super().__init__('sensor_subscriber_node')        
        self.sensor_data = None


    # Override
    # Abonnement aux topics
    def subscribe(self):
        super().subscribe('sensor_topic', Int32)
        

    # Override
    # Mettre à jour la variable des capteurs
    def sensor_callback(self, data):
        self.sensor_data = data.data


    # Retourne la valeur actuelle du capteur ou "N/A" si aucune donnée n'est reçue
    def get_sensor_data(self):
        return self.sensor_data if self.sensor_data is not None else "N/A"
    
    

    # Cette méthode est appelée périodiquement pour traiter les callbacks ROS
    # def process_ros(self):
    #     rospy.spin_once()
