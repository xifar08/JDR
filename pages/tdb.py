import streamlit as st
import pandas as pd

# st.write(st.session_state)

set_init={'Calme','Courage','Intuition','Casse-Cou','Journal intime','Base secrète'}
set_init_avion={'Armement de guerre', 'Blindage', 'Manoeuvrabilité', 'Vitesse', 'Matériel de navigation', 'Moteur', 'Parachute'}
titre=pd.DataFrame({'Titre':["Pas de titre","Espoir","Etoile Montante","As","As des As","Légende","Mythe"]})



if "set_got" not in st.session_state:
    st.session_state.set_got=set()
if "set_used" not in st.session_state:
    st.session_state.set_used=set()
if "set_got_avion" not in st.session_state:
    st.session_state.set_got_avion=set()
if "set_used_avion" not in st.session_state:
    st.session_state.set_used_avion=set()
if "nostalgie" not in st.session_state:
    st.session_state.nostalgie=0
if "jauge" not in st.session_state:
    st.session_state.jauge=4
if "gloire" not in st.session_state:
    st.session_state.gloire=0
if "titre" not in st.session_state:
    st.session_state.titre=titre['Titre'].loc[0]

def maj_etat():
    st.session_state.nostalgie=st.session_state.newnostalgie
    st.session_state.jauge=st.session_state.newjauge

def maj_set_got_avion():
    st.session_state.set_got_avion.add(st.session_state.newset_got_avion)

def maj_set_used_avion():
    st.session_state.set_used_avion.add(st.session_state.newset_used_avion)

def maj_set_recharge_avion():
    st.session_state.set_got_avion.add(st.session_state.newset_recharge_avion)
    st.session_state.set_used_avion.discard(st.session_state.newset_recharge_avion)

def maj_set_got():
    st.session_state.set_got.add(st.session_state.newset_got)

def maj_set_used():
    st.session_state.set_used.add(st.session_state.newset_used)

def maj_set_recharge():
    st.session_state.set_got.add(st.session_state.newset_recharge)
    st.session_state.set_used.discard(st.session_state.newset_recharge)

def reinit_avantages():
    st.session_state.set_got.clear()
    st.session_state.set_used.clear()

def reinit_avantages_avion():
    st.session_state.set_got_avion.clear()
    st.session_state.set_used_avion.clear()

def reinit_nostjauge():
    st.session_state.nostalgie=0
    st.session_state.jauge=4

def maj_gloire():
    st.session_state.gloire=st.session_state.newgloire

def maj_titre(gloire):
    st.session_state.titre=titre['Titre'].loc[gloire/6]


st.title('Tableau de bord')

st.subheader(f"Ta nostalgie est de {st.session_state.nostalgie} et ta jauge est à {st.session_state.jauge}.")
if st.session_state.nostalgie==10 or st.session_state.jauge==0:
    st.error("Il est temps de raccrocher...")
else :
    st.success("Tu peux voler tranquille.")



if st.session_state.gloire%6==0:
            maj_titre(st.session_state.gloire)
            
st.subheader(f"Ta gloire est de {st.session_state.gloire}. Ton titre est {st.session_state.titre}")

if st.session_state.gloire%3==0 and st.session_state.gloire != 0:
    st.success("Tu as une récompense !")


avantages = pd.DataFrame({
    'Avantages à acquérir' : pd.Series(list(set_init.difference(st.session_state.set_got))),
    'Avantages dispo': pd.Series(list(st.session_state.set_got.difference(st.session_state.set_used))),
    'Avantages à recharger': pd.Series(list(st.session_state.set_used))
})

avantages_avion = pd.DataFrame({
    'Avantages à acquérir' : pd.Series(list(set_init_avion.difference(st.session_state.set_got_avion))),
    'Avantages dispo': pd.Series(list(st.session_state.set_got_avion.difference(st.session_state.set_used_avion))),
    'Avantages à recharger': pd.Series(list(st.session_state.set_used_avion))
})

st.subheader('Tes avantages disponibles :')
st.dataframe(avantages)
st.dataframe(avantages_avion)

with st.expander('Nostalgie et jauge'):
    with st.form("Etat"):
        with st.container(horizontal=True):
            nostalgie=st.slider("Nostalgie",0,10,key="newnostalgie")
            jauge=st.slider("Jauge", 0,5,value=4,key="newjauge")
        st.form_submit_button("Maj état",on_click=maj_etat)
    st.button("Réinitialiser la nostalgie et la jauge",on_click=reinit_nostjauge)

with st.expander('Gloire'):
    with st.form("Gloire"):
        gloire=st.slider("Gloire",0,36,key="newgloire")
        st.form_submit_button("Maj gloire", on_click=maj_gloire)

with st.expander('Avantages du pilote'):
    with st.form('Avantages pilote, choix'):
        choix=st.selectbox("Choix des avantages",set_init.difference(st.session_state.set_got),key='newset_got')
        st.form_submit_button("Maj",on_click=maj_set_got)

    with st.form('Avantages pilote, utilisation'):
        utilisation=st.selectbox("Utilisation des avantages",st.session_state.set_got.difference(st.session_state.set_used),key='newset_used')
        st.form_submit_button("Maj",on_click=maj_set_used)

    with st.form('Avantages pilote, recharger'):
        recharge=st.selectbox('Recharger les avantages', st.session_state.set_used,key='newset_recharge')
        st.form_submit_button("Maj",on_click=maj_set_recharge)  
    st.button("Réinitialiser les avantages",on_click=reinit_avantages)

with st.expander("Avantages de l'avion"):
    with st.form('Avantages avion, choix'):
        choix_avion=st.selectbox("Choix des avantages",set_init_avion.difference(st.session_state.set_got_avion),key='newset_got_avion')
        st.form_submit_button("Maj avion",on_click=maj_set_got_avion)

    with st.form('Avantages avion, utilisation'):
        utilisation_avion=st.selectbox("Utilisation des avantages",st.session_state.set_got_avion.difference(st.session_state.set_used_avion),key='newset_used_avion')
        st.form_submit_button("Maj avion",on_click=maj_set_used_avion)

    with st.form('Avantages avion, recharger'):
        recharge_avion=st.selectbox('Recharger les avantages', st.session_state.set_used_avion,key='newset_recharge_avion')
        st.form_submit_button("Maj avion",on_click=maj_set_recharge_avion)  
    st.button("Réinitialiser les avantages de l'avion",on_click=reinit_avantages_avion)




