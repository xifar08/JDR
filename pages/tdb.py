import streamlit as st


st.write(st.session_state)

if "nostalgie" not in st.session_state:
    st.session_state.nostalgie=''
if "jauge" not in st.session_state:
    st.session_state.jauge=''


def maj_etat():
    st.session_state.nostalgie=st.session_state.newnostalgie
    st.session_state.jauge=st.session_state.newjauge



with st.form("Etat"):
    with st.container(horizontal=True):
        nostalgie=st.slider("Nostalgie",0,10,key="newnostalgie")
        jauge=st.slider("Jauge", 0,5,value=4,key="newjauge")
    st.form_submit_button("Maj état",on_click=maj_etat)





if nostalgie==10 or jauge==0:
    st.error("Il est temps de raccrocher...")
