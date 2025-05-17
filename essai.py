import streamlit as st
from streamlit import write
import matplotlib.pyplot as plt
import numpy as np

# Titre de l'application
st.title("Bienvenue sur mon application Streamlit")

# Saisie utilisateur
nom = st.text_input("Entrez votre prénom :")

# Si un prénom est entré, afficher un message de bienvenue
if nom:
    st.success(f"Bonjour, {nom} ! Ravie de vous voir ici 😊")

# Afficher un graphique simple
st.subheader("Un petit graphique pour vous")
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Courbe sinusoïdale")
st.pyplot(fig)
