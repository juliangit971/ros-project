# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_widget(object):
    
    def setupUi(self, main_widget):

        # Main Widget Settings

        main_widget.setObjectName("main_widget")
        main_widget.resize(1000, 650)

        # Font settings

        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        # Audio / Video Output Label

        self.title1_label = QtWidgets.QLabel(main_widget)
        self.title1_label.setGeometry(QtCore.QRect(30, 30, 391, 51))
        self.title1_label.setFont(font)
        self.title1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title1_label.setObjectName("title1_label")

        # Data Label

        self.title2_label.setFont(font)
        self.title2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title2_label.setObjectName("title2_label")
        self.title2_label = QtWidgets.QLabel(main_widget)
        self.title2_label.setGeometry(QtCore.QRect(520, 30, 131, 51))

        # Actions Label

        self.title3_label = QtWidgets.QLabel(main_widget)
        self.title3_label.setGeometry(QtCore.QRect(820, 30, 131, 51))
        self.title3_label.setFont(font)
        self.title3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title3_label.setObjectName("title3_label")
        
        # Separator Line

        self.line = QtWidgets.QFrame(main_widget)
        self.line.setGeometry(QtCore.QRect(750, 40, 20, 601))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Video Output Frame

        self.output_videoWidget = QVideoWidget(main_widget)
        self.output_videoWidget.setGeometry(QtCore.QRect(30, 170, 426, 240))
        self.output_videoWidget.setObjectName("output_videoWidget")
        self.actions_GroupBox = QtWidgets.QGroupBox(main_widget)
        self.actions_GroupBox.setGeometry(QtCore.QRect(790, 150, 191, 321))

        # Action Section

        font = QtGui.QFont()
        font.setPointSize(18)
        self.actions_GroupBox.setFont(font)
        self.actions_GroupBox.setFlat(True)
        self.actions_GroupBox.setObjectName("actions_GroupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.actions_GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.ioCamera_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.ioCamera_checkBox.setText("")
        self.ioCamera_checkBox.setObjectName("ioCamera_checkBox")
        self.gridLayout.addWidget(self.ioCamera_checkBox, 5, 1, 1, 1)
        self.ioCamera_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.ioCamera_label.setObjectName("ioCamera_label")
        self.gridLayout.addWidget(self.ioCamera_label, 5, 0, 1, 1)
        self.forward_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.forward_checkBox.setText("")
        self.forward_checkBox.setObjectName("forward_checkBox")
        self.gridLayout.addWidget(self.forward_checkBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.left_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.left_checkBox.setText("")
        self.left_checkBox.setObjectName("left_checkBox")
        self.gridLayout.addWidget(self.left_checkBox, 2, 1, 1, 1)
        self.ioTemperatue_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.ioTemperatue_label.setObjectName("ioTemperatue_label")
        self.gridLayout.addWidget(self.ioTemperatue_label, 7, 0, 1, 1)
        self.ioMic_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.ioMic_label.setObjectName("ioMic_label")
        self.gridLayout.addWidget(self.ioMic_label, 6, 0, 1, 1)
        self.ioTemperatue_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.ioTemperatue_checkBox.setText("")
        self.ioTemperatue_checkBox.setObjectName("ioTemperatue_checkBox")
        self.gridLayout.addWidget(self.ioTemperatue_checkBox, 7, 1, 1, 1)
        self.right_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.right_checkBox.setText("")
        self.right_checkBox.setObjectName("right_checkBox")
        self.gridLayout.addWidget(self.right_checkBox, 3, 1, 1, 1)
        self.backward_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.backward_label.setObjectName("backward_label")
        self.gridLayout.addWidget(self.backward_label, 1, 0, 1, 1)
        self.right_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.right_label.setObjectName("right_label")
        self.gridLayout.addWidget(self.right_label, 3, 0, 1, 1)
        self.ioMic_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.ioMic_checkBox.setText("")
        self.ioMic_checkBox.setObjectName("ioMic_checkBox")
        self.gridLayout.addWidget(self.ioMic_checkBox, 6, 1, 1, 1)
        self.ioGPS_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.ioGPS_checkBox.setText("")
        self.ioGPS_checkBox.setObjectName("ioGPS_checkBox")
        self.gridLayout.addWidget(self.ioGPS_checkBox, 8, 1, 1, 1)
        self.backward_checkBox = QtWidgets.QCheckBox(self.actions_GroupBox)
        self.backward_checkBox.setText("")
        self.backward_checkBox.setObjectName("backward_checkBox")
        self.gridLayout.addWidget(self.backward_checkBox, 1, 1, 1, 1)
        self.left_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.left_label.setObjectName("left_label")
        self.gridLayout.addWidget(self.left_label, 2, 0, 1, 1)
        self.ioGPS_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.ioGPS_label.setObjectName("ioGPS_label")
        self.gridLayout.addWidget(self.ioGPS_label, 8, 0, 1, 1)
        self.forward_label = QtWidgets.QLabel(self.actions_GroupBox)
        self.forward_label.setObjectName("forward_label")
        self.gridLayout.addWidget(self.forward_label, 0, 0, 1, 1)
        self.data_gridGroupBox = QtWidgets.QGroupBox(main_widget)
        self.data_gridGroupBox.setGeometry(QtCore.QRect(470, 170, 281, 241))

        # Data Section

        font = QtGui.QFont()
        font.setPointSize(16)
        self.data_gridGroupBox.setFont(font)
        self.data_gridGroupBox.setFlat(True)
        self.data_gridGroupBox.setObjectName("data_gridGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.data_gridGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.temperature_value_lcdNumber = QtWidgets.QLCDNumber(self.data_gridGroupBox)
        self.temperature_value_lcdNumber.setObjectName("temperature_value_lcdNumber")
        self.gridLayout_2.addWidget(self.temperature_value_lcdNumber, 0, 1, 1, 1)
        self.humidity_value_lcdNumber = QtWidgets.QLCDNumber(self.data_gridGroupBox)
        self.humidity_value_lcdNumber.setObjectName("humidity_value_lcdNumber")
        self.gridLayout_2.addWidget(self.humidity_value_lcdNumber, 1, 1, 1, 1)
        self.coordinates_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.coordinates_label.setObjectName("coordinates_label")
        self.gridLayout_2.addWidget(self.coordinates_label, 3, 0, 1, 1)
        self.audio_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.audio_label.setObjectName("audio_label")
        self.gridLayout_2.addWidget(self.audio_label, 2, 0, 1, 1)
        self.humidity_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.humidity_label.setObjectName("humidity_label")
        self.gridLayout_2.addWidget(self.humidity_label, 1, 0, 1, 1)
        self.audio_value_lcdNumber = QtWidgets.QLCDNumber(self.data_gridGroupBox)
        self.audio_value_lcdNumber.setObjectName("audio_value_lcdNumber")
        self.gridLayout_2.addWidget(self.audio_value_lcdNumber, 2, 1, 1, 1)
        self.airComposition_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.airComposition_label.setObjectName("airComposition_label")
        self.gridLayout_2.addWidget(self.airComposition_label, 4, 0, 1, 1)
        self.temperature_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.temperature_label.setObjectName("temperature_label")
        self.gridLayout_2.addWidget(self.temperature_label, 0, 0, 1, 1)
        self.coordinates_value_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.coordinates_value_label.setObjectName("coordinates_value_label")
        self.gridLayout_2.addWidget(self.coordinates_value_label, 3, 1, 1, 1)
        self.airComposition_value_label = QtWidgets.QLabel(self.data_gridGroupBox)
        self.airComposition_value_label.setObjectName("airComposition_value_label")
        self.gridLayout_2.addWidget(self.airComposition_value_label, 4, 1, 1, 1)

        # Resubscribe Button

        self.resubscribe_button = QtWidgets.QPushButton(main_widget)
        self.resubscribe_button.setGeometry(QtCore.QRect(290, 550, 241, 33))
        self.resubscribe_button.setObjectName("resubscribe_button")

        # Set Text

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        _translate = QtCore.QCoreApplication.translate
        main_widget.setWindowTitle(_translate("main_widget", "Form"))
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

from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_widget = QtWidgets.QWidget()
    ui = Ui_main_widget()
    ui.setupUi(main_widget)
    main_widget.show()
    sys.exit(app.exec_())
