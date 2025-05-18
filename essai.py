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

import io

st.title("Lire un fichier texte avec io")

# Chargement du fichier par l'utilisateur
uploaded_file = st.file_uploader("Choisissez un fichier texte (.txt)", type=["txt"])

# Si un fichier est téléchargé
if uploaded_file is not None:
    # Lire le fichier en mémoire avec io.StringIO
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    
    # Lire tout le texte
    contenu = stringio.read()

    st.subheader("Contenu du fichier :")
    st.text(contenu)

import sys

st.title("Exemple avec le module sys")

# Afficher la version de Python
st.write("Version de Python :", sys.version)

# Afficher les chemins de recherche des modules
st.subheader("sys.path : chemins de recherche des modules")
for p in sys.path:
    st.text(p)


import re

st.title("Détecteur d'adresses e-mail avec re")

# Zone de texte pour l'utilisateur
texte = st.text_area("Entrez un texte contenant des adresses e-mail :")

# Bouton pour lancer l'extraction
if st.button("Extraire les e-mails"):
    # Expression régulière pour détecter les adresses e-mail
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    
    emails = re.findall(pattern, texte)
    
    if emails:
        st.success("Voici les e-mails détectés :")
        for email in emails:
            st.write(f"📧 {email}")
    else:
        st.warning("Aucune adresse e-mail trouvée.")
