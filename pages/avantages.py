import streamlit as st

st.title('Page de test pour les avantages pilote')

st.write(st.session_state)

set_init={'Calme','Courage','Intuition','Casse-Cou','Journal intime','Base secrète'}

if "set_got" not in st.session_state:
    st.session_state.set_got=set()
if "set_used" not in st.session_state:
    st.session_state.set_used=set()
# if "set_dep" not in st.session_state:
#     st.session_state.set_dep=set_init


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
# used=st.selectbox("Avantages à utiliser",set_got)
# if maj:
#     st.write(maj_avantages(set_init,set_got,set_dep,choix))
#     st.write(set_got)

