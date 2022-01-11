#!/usr/bin/python 3
# -*-coding:Latin-1 -*
# coding: utf-8

# ----------------------------------------------------------------------------- #
#       Formation Administrateur Infrastructure et Cloud OpenClassRooms         #
#         Projet 6 : Participer à la vie de la communauté Open Source           #
#                              CECCHINATO Quentin                               #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#        Programme d'installation et de configuration Ubuntu Serveur            #

# Rôle : Ce programme sera composé de 4 fonctions qui vont installer et         #
#        configurer un serveur Ubuntu.                                          #
# ----------------------------------------------------------------------------- #

import sys, getopt
import fileinput
import os
from socket import *
# import yaml
import os.path


#                                  Les Fonctions                                #

# ----------------------------------------------------------------------------- #
#                           Fonction 1 : ConfigurerIP()                         #

# Rôle : Avec cette fonction on va pouvoir configurer l'adresse IP, le masque   #
#        de sous-réseeu, le DNS, la passerelle par défaut du serveur Ubuntu.    #

#                                ConfigurerIP()                                 #


def configurerip():
    print("Bienvenue dans la configuration IP du serveur Ubuntu.")

    numinterface = input("Entrez le numéro de l'interface réseau (ex : 3 pour enp0s3) : ")  # Variables
    adresseip = input("Entrez l'adresse IP du serveur : ")  # Variables
    netmask = input("Entrez le masque sous réseau : ")  # Variables
    gateway = input("Entrez la passerelle : ")  # Variables
    dns = input("Entrez l'adresse IP du DNS : ")  # Variables

    configip = open("/etc/network/interfaces", "w")  # Ouverture du fichier de configuration interfaces
    configip.write("auto enp0s" + numinterface + "\n")  # Ecriture : numéro de l'interface réseau
    configip.write("iface enp0s" + numinterface + " inet static\n")  # Ecriture : numéro de l'interface réseau
    configip.write("address " + adresseip + "\n")  # Ecriture : adresse IP
    configip.write("netmask " + netmask + "\n")  # Ecriture : Netmask
    configip.write("gateway " + gateway + "\n")  # Ecriture : Gateway
    configip.write("dns-nameservers " + dns + "\n")  # Ecriture : DNS
    print("Vous avez terminé la configuration IP du serveur Ubuntu.")


pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#                            Fonction 2 : dhcp()                                #

# Rôle : Cette fonction va insaller le service DHCP.                            #

#                                    dhcp()                                     #


def dhcp():
    print("Bienvenue dans l'installation et configuration du service DHCP.")
    os.system("apt-get install isc-dhcp-server")  # Installation du service DHCP

    ip = input("Entrez l'adresse IP du réseau (ex : 192.168.*.0) : ")  # Variables
    netmask = input("Entrez le masque sous réseau : ")  # Variables
    range_debut = input("Entrez la premiere adresse IP : ")  # Variables
    range_fin = input("Entrez la derniere adresse IP : ")  # Variables
    dns = input("Entrez le dns : ")  # Variables
    route = input("Entrez la route par defaut : ")  # Variables
    broadcast = input("Entrez l'adresse de Broadcast : ")  # Variables

    fichier = open("/etc/dhcp/dhcpd.conf", "w")  # Ouverture du fichier de configuration dhcpd.conf
    fichier.write("# Configuration pour le réseau \n")  # Ecriture : Configuration pour le réseau
    fichier.write("\nsubnet " + ip + " netmask " + netmask + " {\n")  # Ecriture : adresse IP + netmask
    fichier.write("\nrange " + range_debut + " " + range_fin + ";\n")  # Ecriture : @IP de Début et de Fin
    fichier.write("\noption domain-name-servers " + dns + ";\n")  # Ecriture : DNS
    fichier.write("\noption routers " + route + ";\n")  # Ecriture : Route par défeaut
    fichier.write("\noption broadcast-address " + broadcast + ";\n")  # Ecriture : adresse de Broadcast
    fichier.write("\ndefault-lease-time 3600;")  # Ecriture : Default lease time
    fichier.write("\nmax-lease-time 7200;")  # Ecriture : Max lease time
    fichier.write("\n}")  # Ecriture : }

    oui = "o"  # Variables
    non = "n"  # Variables
    reponse = input("Est ce que le serveur DHCP fait aussi routeur ? (Oui : o Non : n) : \n")
    if reponse == oui:
        iv4 = input("Entrez l'interface réseau connecté au routeur (enp0s8): ")  # Variables
        fichier2 = open("/etc/default/isc-dhcp-server", "w")  # Ouverture du fichier de configuration interfaces
        fichier2.write("\nINTERFACES=" '"' + iv4 + '\n"')  # Ecriture : numéro de l'interface réseau
        fichier2.write("\nINTERFACESv6=" '"''\n"')  # Ecriture : numéro de l'interface réseau
    else:
        print("Non il ne fait pas routeur.")
    pass
    os.system("service isc-dhcp-server restart")  # Redémarrage du service DHCP
    print("Vous avez terminé l'installation et configuration du service DHCP.")


pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#                             Fonction 3 : ntp()                                #

# Rôle : Cette fonction va insaller le service ntp.                             #

#                                     ntp()                                     #


def ntp():
    print("Bienvenue dans l'installation du service NTP.")
    os.system("apt-get install ntp")  # Installation du service NTP


pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#                             Fonction 4 : Samba()                              #

# Rôle : Cette fonction va insaller le service Samba.                           #

#                                     samba()                                   #


def samba():
    print("Bienvenue dans l'installation du service Samba.")
    os.system("apt-get install samba")  # Installation du service Samba

    fichier = open("/etc/samba/smb.conf", "a")  # Ouverture du fichier de configuration
    fichier.write("[partage];\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   comment = Partage de données\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   path = /srv/partage\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   guest ok = no\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   read only = no\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   browsable = yes\n")  # Ecriture des configurations dans le fichier
    fichier.write("\n   valid users = @partage\n")  # Ecriture des configurations dans le fichier

# Création d'un utilisateur et d'un groupe de partage

    os.system("adduser quentin")  # création d'un utilisateur
    os.system("smbpasswd -a quentin")  # ajout de l'utilisateur
    os.system("groupadd partage")  # création d'un groupe de partage
    os.system("gpasswd -a quentin partage")  # ajout de l'utilisateur dans un groupe

# Préparation du dossier partage

    os.system("mkdir /srv/partage")  # Création du dossier de partage
    os.system("chgrp -R partage /srv/partage/")  # Création des droits du dossier de partage
    os.system("chmod -R g+rw /srv/partage/")  # Création des droits du dossier de partage


pass
#                                      Fin                                      #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#      Programme d'installation et de configuration d'un serveur ubuntu         #

# Rôle : Ce programme sera composé de 4 fonctions qui vont installer et         #
#        configurer, avec un paramétrage basique, un serveur Ubuntu.            #

#                   Programme : Installer&ConfigurerUbuntuSRV                   #

Oui = "o"
Non = "n"

reponse2 = input("Bonjour, voulez vouz configurer Ubuntu ? (Oui : o Non : n) : \n")
if reponse2 == Oui:
    print("Nous allons commencer l'installation.")

    print("Première étape : Configuration de l'adressage IP du Serveur Ubuntu\n")
    configurerip()  # Appel de la fonction

    print("Deuxième étape : Installation du service DHCP")
    dhcp()  # Appel de la fonction

    print("troisième étape : Installation du service NTP")
    ntp()  # Appel de la fonction

    print("quatrième étape : Installation du service Samba")
    samba()  # Appel de la fonction

    print("Vous avez terminer la configuration de votre serveur Ubuntu.")

else:
    print("La configuration a été annulé.")
pass

#                                      Fin                                      #
# ----------------------------------------------------------------------------- #
