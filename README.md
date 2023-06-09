# Projet_2_Books_To_Scrap
Le site https://books.toscrape.com/ est un site répertoriant un ensemble de livres par catégorie.

Notre mission est la suivante, nous devons récupérer les informations de tout les produits 
sur le site http://books.toscrape.com/. Ces informations sont les suivantes:

- Se connecter sur le site afin de récupérer le contenu de la page HTML (module requests)
- A l'aide du module beautifulsoup, nous allons récupérer l'ensemble des urls de chaque catégories puis de chaque livres
- Une fois les urls récupérées, nous devons récupérer les informations suivantes dans chaque livres
  - URL du livre
  - Universal Product Code (upc)
  - Titre du livre
  - Prix, taxe incluse
  - Prix, taxe exclue
  - Quantité disponible
  - Description du produit
  - Catégorie
  - Rating
  - URL de l'image
  - Chemin local de l'image téléchargée

En plus de cela, les images des livres sont téléchargées. Ces données sont ensuite classées par catégories et inscrites
dans un fichier CSV correspondant. Les données sont générées à la racine du projet suivant cette arborescence:

```
|-- data/
    |-- categorie1/
        |-- categorie1.csv
        |-- imgs/
            |-- img1.jpg
            |-- img2.jpg
            ...etc
    |-- categorie2/
    ...etc
```

# Installation :

Prerequis : 
- Python
- Git

Une fois les prérequis installés, placez vous dans un répertoire souhaité puis clonez le repository :
```
git clone https://github.com/matthiascarmona25/Projet_2_Books_To_Scrap.git
```

Placez vous dans le dossier Projet_2_Books_To_Scrap puis créez un nouvel environnement virtuel :
```
python -m venv .env
```

Ensuite activez cette environnement virtuel :

Windows :
```
.env\scripts\activate.bat
```

Linux :
```
source .env\scripts\activate
```

Pour finir installer les packages nécesaaires :
```
pip install -r requirements.txt
```

Vous pouvez enfin lancer le script:
```
python main.py
```