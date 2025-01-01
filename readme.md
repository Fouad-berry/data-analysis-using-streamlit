# Exemple de visualisation avec Streamlit

Cette application Streamlit permet de visualiser un ensemble de données aléatoires et de sélectionner le nombre de points à afficher à l'aide d'un curseur.

## Installation
Bienvenue sur notre application crée pour l'ananlyse des données en utilisant stremlit en python

Pour exécuter cette application, vous devez avoir Python installé ainsi que les bibliothèques suivantes :

- streamlit
- pandas
- numpy
- matplotlib

Vous pouvez installer toutes ces dépendances en utilisant pip :

```bash
pip install streamlit pandas numpy matplotlib
```

## Exécution

Une fois les dépendances installées, vous pouvez exécuter l'application en lançant le script `app.py` :

```bash
streamlit run app.py
```

## Description

L'application crée un ensemble de données aléatoires à l'aide de la fonction `numpy.random.randn(n, 2)`. Le nombre de points `n` est défini par un curseur dans l'interface Streamlit. Les points sont ensuite affichés à l'aide de la fonction `matplotlib.pyplot.scatter`.
