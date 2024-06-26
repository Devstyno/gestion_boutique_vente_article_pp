# FONCTIONS
def recherche(liste, nom):
    for item in liste:
        if nom.lower() == item["libelle"].lower():
            return item # item found
    return None # item not found

## Gestion articles
def enregistrer_article(liste_articles : list):
    print("ENREGISTREMENT D'ARTICLE")
    libelle = input("Le libellé (nom) de l'article: ")
    result = recherche(liste_articles, libelle)
    if result != None:
        print("Cet article existe deja !")
    else:
        prix_unitaire = input("Le prix unitaire de l'article: ")
        while prix_unitaire.isalpha():
            prix_unitaire = input("Le prix unitaire doit etre une valeur decimale: ")
        prix_unitaire = float(prix_unitaire)
        
        quantite = input("La quantité en stock de l'article: ")
        while not quantite.isdigit():
            quantite = input("La quantite doit etre une valeur entiere: ")
        quantite = int(quantite)
        if quantite <= 0:
            quantite = 0

        article = {
            "libelle" : libelle,
            "prix_unitaire" : prix_unitaire,
            "quantite" : quantite
        }

        liste_articles.append(article)
        print("Article enregistre avec succes !")

def afficher_les_articles(liste_articles : list):
    if len(liste_articles) > 0:
        print("LISTE DES ARTICLES")
        id = 1
        print("N°\t\t\tNom\t\t\tPrix unitaire\t\t\tQuantité en stock")
        for article in liste_articles:
            print(f"{id}\t\t\t{article["libelle"]}\t\t\t{article["prix_unitaire"]}\t\t\t{article["quantite"]}")
            id += 1
    else:
        print("Aucun article enregistré. Veuillez en ajouter !")

def rechercher_article(liste_articles : list):
    if len(liste_articles) > 0:
        print("RECHERCHER UN ARTICLE")
        nom = input("Veuillez saisir le nom de l'article : ")
        result = recherche(liste_articles, nom)
        if result == None:
            print("Aucun article ne correspond au nom que vous avez saisi.")
            return result
        else:
            article = result
            print(f"Prix unitaire: {article["prix_unitaire"]}\tQuantite en stock: {article["quantite"]}")
            return article
    else:
        print("Il n'existe aucun article. Veuillez en ajouter !")

## Gestion des ventes d'articles
def enregistrer_vente(liste_articles : list, liste_ventes : list):
    if len(liste_articles) > 0:
        print("ENREGISTREMENT DE VENTE")
        nom = input("Veuillez saisir le nom de l'article : ")
        result = recherche(liste_articles, nom)
        if result != None:
            article = result
            print(f"Prix unitaire: {article["prix_unitaire"]}\tQuantite en stock: {article["quantite"]}")
        else:
            print("Desole, il n'existe pas d'article en ce nom.")
            return

        quantite = input("Quelle quantite voulez-vous acheter ? ")
        while not quantite.isdigit():
            quantite = input("La quantite doit etre une valeur entiere strictement positive: ")
        quantite = int(quantite)
        if quantite <= article["quantite"] and quantite > 0:
            vente = {
                "article" : article["libelle"],
                "prix_unitaire" : article["prix_unitaire"],
                "quantite_achetee" : quantite,
                "prix_total" : article["prix_unitaire"] * quantite
            }
            print(f"Prix total a payer : {vente["prix_total"]}")
            liste_ventes.append(vente)
            print("Vente enregistree avec succes !")
            article["quantite"] -= quantite
        else:
            print("La vente est rejettée ; la quantite en stock est insuffisante !")
    else:
        print("Vous n'avez pas d'article a vendre. Veuillez en ajouter !")

def afficher_les_ventes(liste_ventes : list):
    if len(liste_ventes) > 0:
        print("LISTE DES VENTES EFFECTUEES")
        id = 1
        print("N°\t\t\tArticle\t\t\tPrix unitaire\t\t\tQuantité achetée\t\t\tPrix total")
        for vente in liste_ventes:
            print(f"{id}\t\t\t{vente["article"]}\t\t\t{vente["prix_unitaire"]}\t\t\t{vente["quantite_achetee"]}\t\t\t{vente["prix_total"]}")
            id += 1
    else:
        print("Aucune vente enregistrée. Veuillez proceder a une vente !")

def montant_total_ventes(liste_ventes : list):
    if len(liste_ventes) > 0:
        print("AFFICHAGE DU MONTANT TOTAL DES VENTES")
        total = 0
        for vente in liste_ventes:
            total += vente["prix_total"]
        
        print(f"Montant total des ventes effectuées : {total}")
    else:
        print("Aucune vente n'a ete effectuee a ce jour.")

## Choix menu
def faire_choix_menu(liste_articles : list, liste_ventes : list):
    choix = input("[a/b/c/d/e/f]: ")
    if choix not in ["a", "b", "c", "d", "e", "f"]:
        return
    else:
        if choix == "a":
            enregistrer_article(liste_articles)
        elif choix == "b":
            afficher_les_articles(liste_articles)
        elif choix == "c":
            rechercher_article(liste_articles)
        elif choix == "d":
            enregistrer_vente(liste_articles, liste_ventes)
        elif choix == "e":
            afficher_les_ventes(liste_ventes)
        else:
            montant_total_ventes(liste_ventes)
