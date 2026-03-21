import streamlit as st

st.write('Page de test pour les avantages pilote')

set_init={'Calme','Courage','Intuition','Casse-Cou','Journal intime','Base secrète'}
set_dep=set()
set_got=set()
set_used=set()

def maj_avantages(set_init,set_got,set_dep,choix):
    set_got.add(choix)
    set_dep=set_init.difference(set_got)
    return set_dep

choix=st.selectbox("Choix Avantages",set_init)
if choix:
    st.write(maj_avantages(set_init,set_got,set_dep,choix))
    st.write(set_got)

used=st.selectbox("Utilisation Avantages",set_got)