import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

st.set_page_config(page_title="As de l'Adriatique", page_icon="🛩️",layout="wide",initial_sidebar_state="auto")

st.title("Fiche d'aviateur")
st.header("Identité")
st.subheader("Rentrez les informations demandées")

# st.write(st.session_state)


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
if "surnom" not in st.session_state:
    st.session_state.surnom=''
if "signe_distinct" not in st.session_state:
    st.session_state.signe_distinct=''
if "adj1" not in st.session_state:
    st.session_state.adj1=''
if "adj2" not in st.session_state:
    st.session_state.adj2=''
if "adj3" not in st.session_state:
    st.session_state.adj3=''


def maj_perso():
    st.session_state.genre=st.session_state.newgenre
    st.session_state.nom=st.session_state.newnom
    st.session_state.prenom=st.session_state.newprenom
    st.session_state.age=st.session_state.newage
    st.session_state.nationalite=st.session_state.newnationalite
    st.session_state.surnom=st.session_state.newsurnom
    st.session_state.signe_distinct=st.session_state.newsigne_distinct
    st.session_state.adj1=st.session_state.newadj1
    st.session_state.adj2=st.session_state.newadj2
    st.session_state.adj3=st.session_state.newadj3
    


with st.sidebar:
    st.write("Bienvenue dans ce sidebar")


    
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
        with st.container(horizontal=True):
            adj1=st.text_input("Adjectif Positif 1",placeholder="Un adjectif positif",key='newadj1')
            adj2=st.text_input("Adjectif Positif 2",placeholder="Un autre adjectif positif",key='newadj2')
            adj3=st.text_input("Adjectif Négatif",placeholder="Un adjectif négatif",key='newadj3')
        signe_distinct=st.text_area("Signe distinctif", placeholder="Votre signe distinctif",key="newsigne_distinct")
        formulaire_perso=st.form_submit_button("Créez votre personnage", on_click=maj_perso)


if formulaire_perso:
    st.write(f"Vous êtes {prenom} {nom}, pilote originaire de {nationalite} et agé de {age} ans.")

m=folium.Map(location=[44.138808, 13.806688], zoom_start=7)
st_data=st_folium(m,width=725,height=550)