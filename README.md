# Scipt Python de configuration d'un Serveur Ubuntu
## Présentation
Ce script permet de configurer rapidement un serveur Ubuntu en y ajoutant un adressage IP fixe et 
en y installant les services DHCP, NTP et Samba.

Pour le service DHCP on aura une configuration simple. Pour le service NTP il n'y aura que 
l'installation du service. Enfin, pour Samba Nous allons jusqu'à la création du dossier de 
partage.

Le script sera composé de quatres fonctions qui seront appelés dans le programme principale.
La version d'Ubuntu est la 18.04.

## Utilisation
Pour ce script nous allons installer une machine Ubuntu 18.04, faire un apt update et l'utiliser comme serveur.
Pour lancer le script sur Ubuntu il faut :


    -mettre le script là où on le souhaite, pour ma part ça sera sur le bureau 
    
    -ouvrir l’invite de commande
    
    -se déplacer vers l’endroit où se trouve le script « cd Bureau » 
    
    -taper « sudo python3 -nomDuScript-.py »


!Important! Il faut lancer le script avec la commande sudo afin de ne pas avoir de problèmes de droits.

## Améliorations
J'ai déjà pensé à des amériolarations pour le script. Nous pourrons l'améliorer, par exemple,
en ajoutant d'autres services, en donnant la possibilité d'avoir plus de choix dans la 
configuration...

## Informations

Dans ce répertoire vous allez trouver la documentation du projet, la présentation du code et 
de son utilisation dans le Read me, la licence open source (MIT) et le code (main.py) avec les 
descriptions en commentaire. 
