# # ROS PROJECT

## Comment lancer le projet ?

Tout d'abord, ouvrir un terminal et aller à la racine du projet (là où se trouve ce README). Lancer ensuite un `catkin_make` afin de build l'environnement.


Vous devez aussi installer les dépendances suivantes :

`GStreamer` pour les codecs vidéo
```sh
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

`pyqt5.qtmultimedia` pour afficher la vidéo
```sh
sudo apt install python3-pyqt5.qtmultimedia
```

Une fois cela fait, choisir l'un des démarrage ci-dessous pour lancer le programme:

_NOTE : Si vous ne voyez pas la vidéo de test se lancer et que vous voyez un rectangle noir à la place, redémarrer le projet plusieurs fois pour qu'elle apparaisse. Le système n'est pas encore stable._


### # Démarrage simplifié

1) D'ABORD dans un terminal, lancer le script bash `ros_launcher.sh` 

2) Dans un autre terminal, lancer le script `gui_launcher.sh` 



### # Démarrage manuelle

1) Démarrer un shell, aller à la racine du projet (là où se trouve ce fichier Markdown) et `source` le fichier `setup.bash` qui se trouve dans le dossier `devel` :

```sh
source devel/setup.bash
``` 

2) Lancer le fichier `project.launch` se trouvant dans `src/my_ros_project/launch` :
```sh
roslaunch my_ros_project project.launch
```

3) Ouvrir un nouveau shell,  aller dans `src/my_ros_project` et lancer le fichier `main.py` avec Python (Python 3.8.10 utilisé pour les tests):
```sh
python3 src/my_ros_project/main.py
```





