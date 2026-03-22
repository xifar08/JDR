import streamlit as st

# st.write(st.session_state)

set_init={'Calme','Courage','Intuition','Casse-Cou','Journal intime','Base secrète'}

if "set_got" not in st.session_state:
    st.session_state.set_got=set()
if "set_used" not in st.session_state:
    st.session_state.set_used=set()
if "nostalgie" not in st.session_state:
    st.session_state.nostalgie=''
if "jauge" not in st.session_state:
    st.session_state.jauge=''


def maj_etat():
    st.session_state.nostalgie=st.session_state.newnostalgie
    st.session_state.jauge=st.session_state.newjauge

def maj_set_got():
    st.session_state.set_got.add(st.session_state.newset_got)

def maj_set_used():
    st.session_state.set_used.add(st.session_state.newset_used)

def maj_set_recharge():
    st.session_state.set_got.add(st.session_state.newset_recharge)
    st.session_state.set_used.discard(st.session_state.newset_recharge)

def reinit():
    st.session_state.set_got.clear()
    st.session_state.set_used.clear()

with st.form("Etat"):
    with st.container(horizontal=True):
        nostalgie=st.slider("Nostalgie",0,10,key="newnostalgie")
        jauge=st.slider("Jauge", 0,5,value=4,key="newjauge")
    st.form_submit_button("Maj état",on_click=maj_etat)


with st.expander('Avantages'):
    with st.form('Avantages pilote, choix'):
        choix=st.selectbox("Choix des avantages",set_init.difference(st.session_state.set_got),key='newset_got')
        st.form_submit_button("Maj",on_click=maj_set_got)

    with st.form('Avantages pilote, utilisation'):
        utilisation=st.selectbox("Utilisation des avantages",st.session_state.set_got.difference(st.session_state.set_used),key='newset_used')
        st.form_submit_button("Maj",on_click=maj_set_used)

    with st.form('Avantages pilote, recharger'):
        recharge=st.selectbox('Recharger les avantages', st.session_state.set_used,key='newset_recharge')
        st.form_submit_button("Maj",on_click=maj_set_recharge)  
    st.button("Réinitialiser les avantages",on_click=reinit)



if nostalgie==10 or jauge==0:
    st.error("Il est temps de raccrocher...")
