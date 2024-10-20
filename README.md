# # ROS PROJECT

## Comment lancer le projet ?

Tout d'abord, ouvrir un terminal et aller à la racine du projet (là où se trouve ce README). Lancer ensuite un `catkin_make` afin de build l'environnement.
Une fois cela fait, choisir l'un des démarrage ci-dessous pour lancer le programme:


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





