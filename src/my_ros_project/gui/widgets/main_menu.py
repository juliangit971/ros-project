from PyQt5.QtWidgets import QWidget, QLabel, QGroupBox, QFrame, QSizePolicy, QGridLayout, QCheckBox, QLCDNumber, QSpacerItem, QPushButton, QMainWindow
from PyQt5.QtCore import QTimer, Qt, QRect, QMetaObject, QCoreApplication, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

import pathlib

from subscriber_nodes.subscriber_node import SensorSubscriber


class MainMenuWidget():
    
    def __init__(self, program_window : QMainWindow, ros_subscriber: SensorSubscriber):
        
        self.program_window = program_window
        self.main_widget = QWidget()
        self.ros_subscriber = ros_subscriber # Référence à l'objet ROSLogic pour accéder aux données du capteur
        self.value = "N/A"
        self.initUI()
        
        # Création d'un QTimer pour actualiser les données ROS périodiquement
        self.timer = QTimer(self.main_widget)
        self.timer.timeout.connect(self.update_sensor_data)
        self.timer.start(1000) # Actualisation toutes les 100 ms (Exécuter cette fonction chaque 100ms)
        
        
    def initUI(self):

        # Interface graphique avec PyQt5

        self.program_window.get_mainWindow().setWindowTitle('Interface Capteur ROS')
        self.program_window.get_mainWindow().setFixedSize(1000, 650)

        # Font settings

        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        # Audio / Video Output Label

        self.title1_label = QLabel(self.main_widget)
        self.title1_label.setGeometry(QRect(30, 30, 391, 51))
        self.title1_label.setFont(font)
        self.title1_label.setAlignment(Qt.AlignCenter)
        self.title1_label.setObjectName("title1_label")

        # Data Label

        self.title2_label = QLabel(self.main_widget)
        self.title2_label.setGeometry(QRect(520, 30, 131, 51))
        self.title2_label.setFont(font)
        self.title2_label.setAlignment(Qt.AlignCenter)
        self.title2_label.setObjectName("title2_label")
        
        # Actions Label

        self.title3_label = QLabel(self.main_widget)
        self.title3_label.setGeometry(QRect(820, 30, 131, 51))
        self.title3_label.setFont(font)
        self.title3_label.setAlignment(Qt.AlignCenter)
        self.title3_label.setObjectName("title3_label")
        
        # Separator Line

        self.line = QFrame(self.main_widget)
        self.line.setGeometry(QRect(750, 40, 20, 601))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        # Video Output Frame

        ## Création de la zone vidéo
        self.output_videoWidget = QVideoWidget(self.main_widget)
        self.output_videoWidget.setGeometry(QRect(30, 170, 426, 240))
        self.output_videoWidget.setObjectName("output_videoWidget")

        ## Configuration du lecteur multimédia
        self.media_player = QMediaPlayer(self.main_widget, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.output_videoWidget)

        ## Connecter le signal pour redémarrer la vidéo à la fin
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)


        # Action Section

        self.actions_GroupBox = QGroupBox(self.main_widget)
        self.actions_GroupBox.setGeometry(QRect(790, 150, 191, 321))
        font = QFont()
        font.setPointSize(18)
        self.actions_GroupBox.setFont(font)
        self.actions_GroupBox.setFlat(True)
        self.actions_GroupBox.setObjectName("actions_GroupBox")

        self.gridLayout = QGridLayout(self.actions_GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.ioCamera_checkBox = QCheckBox(self.actions_GroupBox)
        self.ioCamera_checkBox.setText("")
        self.ioCamera_checkBox.setObjectName("ioCamera_checkBox")
        self.gridLayout.addWidget(self.ioCamera_checkBox, 5, 1, 1, 1)
        self.ioCamera_label = QLabel(self.actions_GroupBox)
        self.ioCamera_label.setObjectName("ioCamera_label")
        self.gridLayout.addWidget(self.ioCamera_label, 5, 0, 1, 1)
        self.forward_checkBox = QCheckBox(self.actions_GroupBox)
        self.forward_checkBox.setText("")
        self.forward_checkBox.setObjectName("forward_checkBox")
        self.gridLayout.addWidget(self.forward_checkBox, 0, 1, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.left_checkBox = QCheckBox(self.actions_GroupBox)
        self.left_checkBox.setText("")
        self.left_checkBox.setObjectName("left_checkBox")
        self.gridLayout.addWidget(self.left_checkBox, 2, 1, 1, 1)
        self.ioTemperatue_label = QLabel(self.actions_GroupBox)
        self.ioTemperatue_label.setObjectName("ioTemperatue_label")
        self.gridLayout.addWidget(self.ioTemperatue_label, 7, 0, 1, 1)
        self.ioMic_label = QLabel(self.actions_GroupBox)
        self.ioMic_label.setObjectName("ioMic_label")
        self.gridLayout.addWidget(self.ioMic_label, 6, 0, 1, 1)
        self.ioTemperatue_checkBox = QCheckBox(self.actions_GroupBox)
        self.ioTemperatue_checkBox.setText("")
        self.ioTemperatue_checkBox.setObjectName("ioTemperatue_checkBox")
        self.gridLayout.addWidget(self.ioTemperatue_checkBox, 7, 1, 1, 1)
        self.right_checkBox = QCheckBox(self.actions_GroupBox)
        self.right_checkBox.setText("")
        self.right_checkBox.setObjectName("right_checkBox")
        self.gridLayout.addWidget(self.right_checkBox, 3, 1, 1, 1)
        self.backward_label = QLabel(self.actions_GroupBox)
        self.backward_label.setObjectName("backward_label")
        self.gridLayout.addWidget(self.backward_label, 1, 0, 1, 1)
        self.right_label = QLabel(self.actions_GroupBox)
        self.right_label.setObjectName("right_label")
        self.gridLayout.addWidget(self.right_label, 3, 0, 1, 1)
        self.ioMic_checkBox = QCheckBox(self.actions_GroupBox)
        self.ioMic_checkBox.setText("")
        self.ioMic_checkBox.setObjectName("ioMic_checkBox")
        self.gridLayout.addWidget(self.ioMic_checkBox, 6, 1, 1, 1)
        self.ioGPS_checkBox = QCheckBox(self.actions_GroupBox)
        self.ioGPS_checkBox.setText("")
        self.ioGPS_checkBox.setObjectName("ioGPS_checkBox")
        self.gridLayout.addWidget(self.ioGPS_checkBox, 8, 1, 1, 1)
        self.backward_checkBox = QCheckBox(self.actions_GroupBox)
        self.backward_checkBox.setText("")
        self.backward_checkBox.setObjectName("backward_checkBox")
        self.gridLayout.addWidget(self.backward_checkBox, 1, 1, 1, 1)
        self.left_label = QLabel(self.actions_GroupBox)
        self.left_label.setObjectName("left_label")
        self.gridLayout.addWidget(self.left_label, 2, 0, 1, 1)
        self.ioGPS_label = QLabel(self.actions_GroupBox)
        self.ioGPS_label.setObjectName("ioGPS_label")
        self.gridLayout.addWidget(self.ioGPS_label, 8, 0, 1, 1)
        self.forward_label = QLabel(self.actions_GroupBox)
        self.forward_label.setObjectName("forward_label")
        self.gridLayout.addWidget(self.forward_label, 0, 0, 1, 1)
        self.data_gridGroupBox = QGroupBox(self.main_widget)
        self.data_gridGroupBox.setGeometry(QRect(470, 170, 281, 241))

        # Data Section

        font = QFont()
        font.setPointSize(16)
        self.data_gridGroupBox.setFont(font)
        self.data_gridGroupBox.setFlat(True)
        self.data_gridGroupBox.setObjectName("data_gridGroupBox")
        self.gridLayout_2 = QGridLayout(self.data_gridGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.temperature_value_lcdNumber = QLCDNumber(self.data_gridGroupBox)
        self.temperature_value_lcdNumber.setObjectName("temperature_value_lcdNumber")
        self.gridLayout_2.addWidget(self.temperature_value_lcdNumber, 0, 1, 1, 1)
        self.humidity_value_lcdNumber = QLCDNumber(self.data_gridGroupBox)
        self.humidity_value_lcdNumber.setObjectName("humidity_value_lcdNumber")
        self.gridLayout_2.addWidget(self.humidity_value_lcdNumber, 1, 1, 1, 1)
        self.coordinates_label = QLabel(self.data_gridGroupBox)
        self.coordinates_label.setObjectName("coordinates_label")
        self.gridLayout_2.addWidget(self.coordinates_label, 3, 0, 1, 1)
        self.audio_label = QLabel(self.data_gridGroupBox)
        self.audio_label.setObjectName("audio_label")
        self.gridLayout_2.addWidget(self.audio_label, 2, 0, 1, 1)
        self.humidity_label = QLabel(self.data_gridGroupBox)
        self.humidity_label.setObjectName("humidity_label")
        self.gridLayout_2.addWidget(self.humidity_label, 1, 0, 1, 1)
        self.audio_value_lcdNumber = QLCDNumber(self.data_gridGroupBox)
        self.audio_value_lcdNumber.setObjectName("audio_value_lcdNumber")
        self.gridLayout_2.addWidget(self.audio_value_lcdNumber, 2, 1, 1, 1)
        self.airComposition_label = QLabel(self.data_gridGroupBox)
        self.airComposition_label.setObjectName("airComposition_label")
        self.gridLayout_2.addWidget(self.airComposition_label, 4, 0, 1, 1)
        self.temperature_label = QLabel(self.data_gridGroupBox)
        self.temperature_label.setObjectName("temperature_label")
        self.gridLayout_2.addWidget(self.temperature_label, 0, 0, 1, 1)
        self.coordinates_value_label = QLabel(self.data_gridGroupBox)
        self.coordinates_value_label.setObjectName("coordinates_value_label")
        self.gridLayout_2.addWidget(self.coordinates_value_label, 3, 1, 1, 1)
        self.airComposition_value_label = QLabel(self.data_gridGroupBox)
        self.airComposition_value_label.setObjectName("airComposition_value_label")
        self.gridLayout_2.addWidget(self.airComposition_value_label, 4, 1, 1, 1)

        # Resusbscribe Boutton

        self.resubscribe_button = QPushButton(self.main_widget)
        self.resubscribe_button.setGeometry(QRect(290, 550, 241, 33))
        self.resubscribe_button.setObjectName("resubscribe_button")
        self.resubscribe_button.clicked.connect(self.resubscribe_to_topic)

        # Set Text

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self.main_widget)

        # Play Video
        self.play_video()


        self.main_widget.show()
        
        
    
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.main_widget.setWindowTitle(_translate("main_widget", "Form"))
        self.title1_label.setText(_translate("main_widget", "Audio / Video Output"))
        self.title3_label.setText(_translate("main_widget", "Actions"))
        self.title2_label.setText(_translate("main_widget", "Data"))
        self.ioCamera_label.setText(_translate("main_widget", "O/I Camera"))
        self.ioTemperatue_label.setText(_translate("main_widget", "O/I Temperature"))
        self.ioMic_label.setText(_translate("main_widget", "O/I Mic"))
        self.backward_label.setText(_translate("main_widget", "Go backward"))
        self.right_label.setText(_translate("main_widget", "Go Right"))
        self.left_label.setText(_translate("main_widget", "Go Left"))
        self.ioGPS_label.setText(_translate("main_widget", "O/I GPS"))
        self.forward_label.setText(_translate("main_widget", "Go forward"))
        self.coordinates_label.setText(_translate("main_widget", "Coordinates :"))
        self.audio_label.setText(_translate("main_widget", "Audio (dB)"))
        self.humidity_label.setText(_translate("main_widget", "Humidity :"))
        self.airComposition_label.setText(_translate("main_widget", "Air Composition :"))
        self.temperature_label.setText(_translate("main_widget", "Temperature :"))
        self.coordinates_value_label.setText(_translate("main_widget", "coord"))
        self.airComposition_value_label.setText(_translate("main_widget", "compo"))
        self.resubscribe_button.setText(_translate("resubscribe_button", "Resubscribe"))
        
    def update_sensor_data(self):
        # Mettre à jour l'étiquette avec la nouvelle valeur des capteurs

        sensor_value = self.ros_subscriber.get_sensor_data()
        #self.label.setText(f"Valeur du Capteur: {sensor_value}")

        self.audio_value_lcdNumber.display(sensor_value)
        self.humidity_value_lcdNumber.display(sensor_value)
        self.temperature_value_lcdNumber.display(sensor_value)
        self.coordinates_value_label.setText(f"{sensor_value}")
        self.airComposition_value_label.setText(f"{sensor_value}")

        
    def resubscribe_to_topic(self):
        self.ros_subscriber.unsubscribe()
        self.ros_subscriber.subscribe()



    def play_video(self):

        # Vérifier et réinitialiser si nécessaire
        if self.media_player.mediaStatus() != QMediaPlayer.NoMedia:
            self.media_player.stop()  # Réinitialise le lecteur avant de recharger
            
        video_path = f"{pathlib.Path(__file__).parent.resolve()}/../../media/video.mp4"
        media_content = QMediaContent(QUrl.fromLocalFile(video_path))
        self.media_player.setMedia(media_content)

        self.media_player.play()


    def handle_media_status(self, status):
        # Redémarrer la vidéo lorsque la lecture est terminée
        if status == QMediaPlayer.EndOfMedia:
            self.media_player.setPosition(0)  # Revenir au début
            self.media_player.play()         # Relancer la lecture
        
        
    def get_widget(self):
        return self.main_widget
    
    def get_window_size(self):
        return []