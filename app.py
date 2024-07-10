import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Exemple de visualisation avec Streamlit")

# Génération de données
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

# Slider pour choisir le nombre de points à afficher
num_points = st.slider('Nombre de points à afficher', 1, 10, 5)

# Affichage des données sous forme de tableau
st.write(f"Affichage des {num_points} premiers points :")
st.dataframe(data.head(num_points))

# Création d'un graphique
fig, ax = plt.subplots()
ax.plot(data['x'][:num_points], data['y'][:num_points])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graphique linéaire')

# Affichage du graphique
st.pyplot(fig)
