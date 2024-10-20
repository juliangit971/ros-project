import rospy



class SubscriberSuperclass():
    
    def __init__(self, subscriber_node_name: str):
        rospy.init_node(subscriber_node_name, anonymous=True)
        self.sensor_data = None


    # Abonnement aux topics
    def subscribe(self, topic_name: str, data_class):
        self.sub = rospy.Subscriber('sensor_topic', data_class, self.sensor_callback)


    # Mettre à jour la variable des capteurs
    def sensor_callback(self):
        pass
    
    
    # Se désinscrire du topic
    def unsubscribe(self):
        self.sub.unregister()