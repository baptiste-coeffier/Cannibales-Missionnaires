# Cannibales-Missionnaires
Ce projet implémente le problème des cannibales et missionnaires en python.
Le jeu des cannibales et missionnaires est un jeu aux règles simple :
  - il y a n cannibales et n missionnaires,
  - le but est de faire traverser tous les cannibales et missionnaires de la rive gauche vers la rive droite au moyen d'une barque,
  - la barque ne peut se déplacer que vers la droite ou la gauche et avec au moins une personne,
  - la taille maximum de place dans la barque est défini par un paramètre p,
  - Si a tout moment sur une rive, il y a plus de cannibales que de missionnaires alors le jeu est perdu.

L'algorithme essaie de résoudre ce problème en fonction du nombre de cannibales/missionnaires et du nombre de place fournis par l'utilisateur. Si une solution existe, l'algorithme renverra le nombre de déplacement optimal ainsi que les déplacements à faire pour obtenir cette solution.

L'algorithme est une implémentation d'un parcours en longueur d'abord de manière récursive.

# Fonctionnement de l'algorithme

## Classe Arbre :

Cette classe représente un nœud dans un arbre de recherche. Chaque nœud contient :

  - Etat : Contient le nombre de missionnaires et de cannibales de chaque côté de la rivière, ainsi que la position de la barque.
  - fils : Une liste des nœuds enfants représentant les états suivants possibles.
  - parent : Le nœud parent, permettant de remonter à l'état précédent.

## Fonction but(tmpCg, tmpMg, bar) :

Vérifie si l'état actuel est l'état but, c'est-à-dire si tous les cannibales et missionnaires sont sur la rive droite et que la barque est également sur la rive droite.

## Fonction isvalid(tmpCg, tmpMg) :

Vérifie si l'état donné respecte les contraintes du problème :

  - Le nombre de missionnaires ou de cannibales ne peut pas être négatif ou dépasser le nombre initial.
  - Le nombre de cannibales ne doit jamais être supérieur au nombre de missionnaires sur une rive (sauf si aucun missionnaire n'est présent).

## Fonction doublon() :

Élimine les états déjà explorés de la liste des états à explorer (appelée Frontiere), afin d'éviter de revenir sur des états déjà visités.

## Fonction graphSearch() :

Implémente l'algorithme de recherche en profondeur (DFS) pour trouver une solution au problème :

La fonction commence en prenant l'état initial (tous les missionnaires et cannibales sur la rive gauche).
Elle explore tous les états possibles en déplaçant la barque avec des combinaisons de missionnaires et de cannibales.
À chaque état, elle vérifie s'il respecte les contraintes et si l'état but est atteint.
Les états explorés sont ajoutés à la liste Explorer, et les nouveaux états valides sont ajoutés à Frontiere pour exploration ultérieure.
La fonction s'appelle récursivement jusqu'à trouver une solution ou jusqu'à ce qu'il n'y ait plus d'états à explorer.

## Fonction Chemin(s) :
Retrace le chemin à partir de l'état solution trouvé par graphSearch() jusqu'à l'état initial :

En remontant dans l'arbre grâce aux nœuds parents, cette fonction affiche l'évolution des missionnaires et cannibales sur chaque rive après chaque traversée de la barque.
Elle affiche également le nombre total de déplacements effectués.

# Conclusion 

Cet algorithme implémente une solution de parcours en longueur d'abord de manière récursive, c'est une implémentation permettant de ressortir une solution quand celle ci existe.
