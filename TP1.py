# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:03:22 2021

@author: louison
"""

###Lancement de cassandra:
cd apache-cassandra-4.0-beta4/
bin/cqlsh

###########################################
###########################################
EXERCICE 1
###########################################
###########################################


###Création d'un KEYSPACE elections
CREATE KEYSPACE elections WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'} AND durable_writes= 'true';

###On rentre dans le KEYSPACE elections
USE elections;

###On créé un tableau administré avec dedans numéro d'id nationale, le nom, le prénom, et l'adresse
CREATE TABLE administre (numero_id_nationale int PRIMARY KEY, nom text, prenom text, adresse text);

###On créé maintenant un tableau candidat avec dedans le nom, le prénom et le parti politique du candidat
 CREATE TABLE candidat (nom text PRIMARY KEY, prenom text, parti_politique text, nombre_de_voies int);

###Si on ouvre maintenant le TABLES on  a : 
 administre  candidat

###On insere maintenant des valeurs à nos administrés (ici 5 personnes)
INSERT INTO administre(numero_id_nationale, nom, prenom, adresse) VALUES (17, 'DUPONT', 'Louis', 'Paris');
INSERT INTO administre(numero_id_nationale, nom, prenom, adresse) VALUES (29, 'GROSJEAN', 'Romain', 'Monaco');
INSERT INTO administre(numero_id_nationale, nom, prenom, adresse) VALUES (44, 'HAMILTON', 'Lewis', 'Manchester');
INSERT INTO administre(numero_id_nationale, nom, prenom, adresse) VALUES (34, 'LECLERC', 'Charles', 'Paris');
INSERT INTO administre(numero_id_nationale, nom, prenom, adresse) VALUES (98,'OCON', 'Esteban', 'Reims');

###On affiche maintenant le tableau administré:
SELECT * FROM administre;

 numero_id_nationale | adresse    | nom      | prenom
---------------------+------------+----------+---------
                  44 | Manchester | HAMILTON |   Lewis
                  98 |      Reims |     OCON | Esteban
                  29 |     Monaco | GROSJEAN |  Romain
                  17 |      Paris |   DUPONT |   Louis
                  34 |      Paris |  LECLERC | Charles

###On fait de même avec les candidats:
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('HIDALGO', 'Anne', 'B', 234);
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('LASALLE', 'Jean', 'A', 34567);
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('SARKOZY', 'Nicolas', 'C',16742);
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('MELENCHON', 'Jean-Luc', 'A', 2341);
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('BACHELOT', 'ROSELINE', 'B', 1957);
INSERT INTO candidat(nom, prenom, parti_politique, nombre_de_voies) VALUES ('MACRON', 'Emmanuel', 'C', 19);


###On affiche le tableau des candidats: 
SELECT * FROM candidat;

 nom       | nombre_de_voies | parti_politique | prenom
-----------+-----------------+-----------------+----------
 MELENCHON |            2341 |               A | Jean-Luc
   LASALLE |           34567 |               A |     Jean
  BACHELOT |            1957 |               B | ROSELINE
   HIDALGO |             234 |               B |     Anne
    MACRON |              19 |               C | Emmanuel
   SARKOZY |           16742 |               C |  Nicolas
   
###On créé un index
CREATE index ipp on candidat (parti_politique) ;


###QUESTION 1. Quel parti politique a réuni le plus de voix ?
###Parti politique A
SELECT SUM(nombre_de_voies) from candidat WHERE parti_politique='A';

 system.sum(nombre_de_voies)
-----------------------------
                       36908

###Parti politique B
SELECT SUM(nombre_de_voies) from candidat WHERE parti_politique='B';

 system.sum(nombre_de_voies)
-----------------------------
                        2191

###Parti politique C
SELECT SUM(nombre_de_voies) from candidat WHERE parti_politique='C';

 system.sum(nombre_de_voies)
-----------------------------
                       16761

###On remarque donc que c'est le parti politique A qui a le plus de voix
 
###QUESTION 2. Quel candidat a gagné les élections ?
SELECT nom, prenom, MAX(nombre_de_voies) FROM candidat;

 nom     | prenom | system.max(nombre_de_voies)
---------+--------+-----------------------------
 LASALLE |   Jean |                       34567
 
 
 
###QUESTION 3. Le candidat ayant gagné les élections vient-il du parti politique ayant eu la majorité des voix ?
OUI


###########################################
###########################################
Exercice 2
###########################################
###########################################

###QUESTION 1. Quel est le parti politique ayant eu le plus de voix ?
###QUESTION 2. Quel est le parti politique ayant eu le moins de voix ?
###Comme j'ai dejà créé 2 candidats par parti, je n'ai pas besoin de rajouter de candidats et les résultats seront les mêmes que dans l'exo 1.

