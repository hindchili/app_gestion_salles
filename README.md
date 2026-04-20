Application de gestion des salles



Hind Chili



 Description du projet

Ce projet consiste à développer une application en Python permettant de gérer des salles.
L’utilisateur peut ajouter, modifier, supprimer et afficher des salles à partir d’une interface graphique.

L’application est connectée à une base de données MySQL et utilise une architecture en plusieurs couches.



 Architecture du projet

Le projet est organisé de la manière suivante :

* models/ : contient la classe Salle
* Data/ : contient le DAO et le fichier de configuration de la base de données
* services/ : contient la logique métier
* views/ : contient l’interface graphique
* main.py : permet de lancer l’application

---

 Base de données

Nom de la base : db_salles

Table utilisée : salle

Champs :

* code (clé primaire)
* description
* categorie
* capacite

---

 Fonctionnalités

L’application permet de :

* Ajouter une salle
* Modifier une salle
* Supprimer une salle
* Afficher la liste des salles

---

Actualisation automatique de la liste

La méthode `lister()` permet de mettre à jour le tableau des salles.

Elle est appelée :

* au lancement de l’application
* à la fin des méthodes ajouter, modifier et supprimer

Cela permet d’assurer un affichage dynamique des données.

---

 Tests de l’application

Les tests réalisés sont :

* Vérification de l’affichage initial des salles
* Test de l’ajout d’une salle
* Test de la modification d’une salle
* Test de la suppression d’une salle
* Vérification de la mise à jour automatique de la liste

---

Lancement de l’application

Dans le terminal, exécuter la commande suivante :

```bash id="qg1w8q"
python main.py
```

---

Validation et publication

Le projet a été testé et fonctionne correctement.
Les modifications ont été validées avec Git et publiées sur GitHub.



Conclusion

Ce projet m’a permis de comprendre :

* la connexion à une base de données MySQL
* l’organisation d’une application en plusieurs couches
* la création d’une interface graphique avec Python
* la gestion dynamique des données


 Résultat final

L’application fonctionne correctement avec :

* une interface claire
* un affichage dynamique
* toutes les opérations CRUD fonctionnelles

---
