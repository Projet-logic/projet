# Game overview
- Hashiwokakero (ou Bridges) est un jeu de réflexion et de logique d'origine japonaise.
- Dans ce jeu, on vous donne une grille de carrés avec un certain nombre de colonnes et de lignes contenant le nombre de ponts. Votre objectif est de relier toutes les îles par des ponts pour former un réseau invisible.
- Chaque île de la grille a un certain nombre de ponts qui lui sont attachés, et les ponts ne peuvent être attachés que dans des directions horizontales ou verticales. Aucun pont n'est autorisé à traverser et une ligne ne peut pas traverser un autre pont.
- Le jeu Hashiwokakero demande aux joueurs de penser logiquement et de développer des compétences en résolution de problèmes. Cela peut être un jeu amusant et stimulant pour les amateurs de puzzle.

![image](https://user-images.githubusercontent.com/78409997/234302292-ab4b6b0c-988f-47c8-80dc-1861a78916af.png)


# Variable and constant definition :
- Définition constante variable :
     - les constantes sont T pour True et F pour False et elles doivent être importées comme "from Vaiable_constant_d.constant import T,F"
    
     - La variable est un objet qui a un attribut appelé nom et dans le cas d'une affectation, il aura un autre attribut appelé valeur
     - La variable de classe a une méthode appelée "affect" qui doit être importée avec "from Vaiable_constant_d.Variable import affect" ou affectée à un local - Variables avec 'from Variable_constant_d import Variable | affect = Variable.affect' et l'utilisation est comme " A affecte T "
- Définition des connecteurs :
     - comme nous essayons de créer les clauses, nous n'aurons donc besoin que de 'AND' et 'OR', vous pouvez importer ces connecteurs logiques en
     - "à partir de connector_d.connector importer ET, OU"
Définitions des formules :
     - une formule est un type récursif qui est défini par sa sous-formule gauche, sa sous-formule droite et son connecteur
     - ses sous-formules peuvent être soit une variable, une valeur constante ou une formule
     
# Exécuter les étapes:
  I) Initialiser le jeu
  - Exécuter le module Input.py pour saisir les données nécessaires à l'initialisation de la grille de jeu et des îles     
     - vous saisissez la valeur souhaitée dans les 4 cases correspondant à la taille de la grille carrée, la position horizontale et verticale et la valeur de l'île
     - Après chaque fois, entrez suffisamment de paramètres, je vous recommande d'appuyer sur le bouton Check pour vérifier leur exactitude
     - Après que le programme indique que vos valeurs ont été acceptées :
        - Vous pouvez enregistrer et afficher la valeur de l'île que vous venez d'entrer à l'aide des boutons Save et Show
        - Si vous ignorez l'étape de sauvegarde et entrez une autre valeur dans l'une des 4 cases ci-dessus, votre valeur actuelle sera perdue
        - Notez qu'à cette étape votre île n'a pas été ajoutée à notre programme
        - Pour ce faire, vous appuyez sur le bouton Save_Info et toutes les valeurs que vous avez enregistrées seront acceptées par notre programme.
        - Continuez à taper jusqu'à ce que vous souhaitiez arrêter, appuyez sur le bouton Quit
        - Après avoir fermé la fenêtre d'interface, les informations de votre jeu seront désormais affichées dans le fichier information.txt 
        - Vous pouvez vérifier et modifier directement dans ce fichier si vous le souhaitez
               
  II) Obtenir le résultat
  - Exécuter le module main.py, toutes vos solutions et l'interface de la grille de jeu apparaîtront.
      - Le fichier sat.cnf sera également enregistré à cette étape
      - vous pouvez tester et comparer avec les résultats que vous obtenez
  
