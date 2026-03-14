import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

st.set_page_config(page_title="As de l'Adriatique", page_icon="🛩️",layout="wide",initial_sidebar_state="auto")

st.title("Fiche d'aviateur")
st.header("Identité")
st.subheader("Rentrez les informations demandées")

st.write(st.session_state)

titre=pd.DataFrame({'Titre':["Pas de titre","Espoir","Etoile Montante","As","As des As","Légende","Mythe"]})

if "genre" not in st.session_state:
    st.session_state.genre=''
if "nom" not in st.session_state:
    st.session_state.nom=''
if "prenom" not in st.session_state:
    st.session_state.prenom=''
if "age" not in st.session_state:
    st.session_state.age=''
if "nationalite" not in st.session_state:
    st.session_state.nationalite=''
if "gloire" not in st.session_state:
    st.session_state.gloire=''
if "surnom" not in st.session_state:
    st.session_state.surnom=''


def maj_perso():
    st.session_state.genre=st.session_state.newgenre
    st.session_state.nom=st.session_state.newnom
    st.session_state.prenom=st.session_state.newprenom
    st.session_state.age=st.session_state.newage
    st.session_state.nationalite=st.session_state.newnationalite
    st.session_state.surnom=st.session_state.newsurnom

def maj_gloire():
    st.session_state.gloire=st.session_state.newgloire

with st.sidebar:
    st.write("Bienvenue dans ce sidebar")

with st.form("Gloire"):
    gloire=st.slider("Gloire",0,36,key="newgloire")
    st.form_submit_button("Maj gloire", on_click=maj_gloire)
    
with st.expander("Aviateur"):
    with st.form("Aviateur"):
        with st.container(horizontal=True):
            prenom=st.text_input("Prénom", placeholder="Votre prénom",key='newprenom')
            nom=st.text_input("Nom", placeholder="Votre nom",key='newnom')
            genre=st.selectbox("Genre",["Masculin","Féminin","Indéterminé"],placeholder="Votre genre",key='newgenre')
        with st.container(horizontal=True):
            age=st.slider("Age",0,100,20,key='newage')
            nationalite=st.selectbox("Pays d'origine",["Angleterre","France", "Italie", "Allemagne", "Japon","Etats-Unis"],placeholder="Votre pays de naissance",key='newnationalite')
        with st.container(horizontal=True,horizontal_alignment="center"):
            surnom=st.text_input("Surnom",placeholder="Votre surnom",key="newsurnom")
        formulaire_perso=st.form_submit_button("Créez votre personnage", on_click=maj_perso)

votre_titre=titre['Titre'].loc[0]
if gloire%6==0:
            votre_titre=titre['Titre'].loc[gloire/6]
st.write("Votre titre est : "+votre_titre)
if formulaire_perso:
    st.write(f"Vous êtes {prenom} {nom}, pilote originaire de {nationalite} et agé de {age} ans.")
if gloire%3==0 and gloire != 0:
    st.success("Tu as une récompense !")

# with st.expander("Avion"):
#     with st.form("Avion"):
#         modele=st.selectbox("Modèle",["Avion 1","Avion 2","Avion 3"],placeholder="Votre avion")
#         nom_avion=st.text_input("Nom", placeholder="Le nom de votre avion")
#         couleur=st.color_picker("Couleur d'avion", value="#F50505")
#         formulaire_avion=st.form_submit_button("Créez votre avion")

# ça ne marche pas parce que quand tu cliques sur un autre bouton ça rerun et ça donc ça perd la mémoire de l'autre boutton
# if formulaire_perso and not formulaire_avion:
#     st.write("Maintenant, créez votre avion !")
# elif formulaire_perso and formulaire_avion:
#     st.write(f"Vous êtes {prenom} {nom}, pilote originaire de {nationalite} et agé de {age} ans.")
# else:
#     st.write("Créez votre personnage et votre avion!")


m=folium.Map(location=[44.138808, 13.806688], zoom_start=7)
st_data=st_folium(m,width=725,height=550)