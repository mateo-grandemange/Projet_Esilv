# Projet_Esilv

Pour réaliser ce projet, j'ai utilisé le site Boursorama.com, et plus précisemment la page sur la valeur de l'action de la société générale.

J'ai donc commencé par récuperer la donnée, avec le code présent dans le fichier "Recuperation donnée" en utilisant la command ```curl``` .
Cette requête a donc été mise dans la table cron, qui aura pour but de récuperer la donnée toutes les 5 minutes.

Ensuite, j'ai écrit un code dans le langage python, que l'on peut retrouver dans le fichier app.py, afin d'afficher cette valeur dans un dashboard, avec un graphique, en utilisant le package dash.
Dans le code python, le graphe n'affiche que les valeurs entre 9h et 17h30, puisque les marchés sont ouverts durant ces horaires. Il s'agit d'un graphique journalier, qui affiche le cours de l'action chaque jour.
Le code permet aussi d'afficher un petit récap de la journée, à partir de 20h. Si l'on visite le site avant 20h, le visiteur est informé que les statistiques de la journée ne seront disponibles qu'à partir de 20h.
Ce code a été mis dans un fichier, dans mon directory "projet".

Ensuite, dans une fenetre tmux, j'execute le code, pour que celui-ci tourne en continu. On peut retrouver cette requête dans le fichier tmux.
