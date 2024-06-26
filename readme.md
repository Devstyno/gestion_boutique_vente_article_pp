# Langage Algorithmique & Python : Collections de données (Les tableaux, les listes à une dimension)

## Problème : Gestion des activités d’une boutique de vente d’articles

Le propriétaire d’une boutique de ventes d’articles vous demande de lui mettre en place un système de gestion de ses activités.
Il souhaite principalement à partir du système, gérer ses articles ainsi que les ventes des articles.
Pour un article, il souhaite renseigner :

- Le libellé (nom) de l’article
- Le prix unitaire de l’article
- La quantité en stock de l’article

### Pour la gestion des articles, il souhaite

1. Enregistrer les articles

2. Afficher la liste des articles au format ci-dessous :

    `

        N°  Nom     Prix unitaire   Quantité en stock

        1   Art 1   1500            18

        2   Art 2   27000           52

        …   …       …               …

    `

3. Rechercher un article à partir de son nom et afficher les informations (prix unitaire, quantité en stock) de l’article.

### Pour la gestion des ventes, il souhaite

1. Enregistrer les ventes (une vente concerne un seul article).
Pour enregistrer une vente, l’utilisateur entre le nom de l’article, la quantité à acheter ; le système enregistre la vente en mettant à jour la quantité en stock de l’article acheté.
Avant l’enregistrement de l’article, le système vérifie que la quantité à acheter est inférieure ou égale à la quantité en stock ; sinon la vente doit être rejetée.
Si l’enregistrement est effectué, vous afficherez le prix total à payer.

2. Afficher la liste des ventes au format ci-dessous :

    `

        N°  Article     Prix unitaire   Quantité achetée    Prix total

        1   Art 1       1500            2                   3000

        2   Art 1       1500            5                   7500

        3   Art 2       27000           1                   27000

        …   …           …               …                   …

    `

3. Afficher le montant total des ventes effectuées ;

## Indications

Dans l’algorithme, utilisez différents tableaux pour stocker :

- Les libellés des articles
- Leurs prix unitaires
- Leurs quantités en stock

Dans ces tableaux, le premier article aura ses informations à l’indice 0 de chaque tableau, ainsi de suite.
Vous utiliserez également un autre tableau pour stocker la liste des ventes des articles.
Vous pouvez utiliser d’autres tableaux au besoin.
Créez des fonctions ou procédures correspondant à chaque opération que le propriétaire de la boutique pourra effectuer afin que votre programme soit bien modulaire.

## Fonctionnement

Vous pouvez utiliser un menu pour faciliter la gestion des opérations.

    `
    Menu
        Gestion des articles
            a- Saisie des articles
            b- Liste des articles
            c- Recherche d’un article
        Gestion des ventes :
            d- Enregistrement d’une vente
            e- Liste des ventes
            f- Montant total des ventes
    `

Avant de pouvoir enregistrer une vente, on doit saisir au moins un article. Il faut vérifier aussi que l’article existe avant l’enregistrement d’une vente le concernant.
Pour utiliser une fonctionnalité du menu, le propriétaire va saisir la lettre correspondante. Vous effectuez l’opération ; lui affichez le résultat et ensuite le menu pour lui permettre d’effectuer une autre opération.

## Travail à Faire

Ecrivez le programme principal ainsi que les différentes fonctions utilisées par le programme principal en Python.
Utilisez des noms explicites pour vos variables (variables simples, listes) et pour vos fonctions.

**NB :** _A la place des tableaux, vous pouvez utiliser les listes. Créez ici un module qui va contenir toutes les fonctions._
