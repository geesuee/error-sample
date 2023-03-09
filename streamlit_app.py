import streamlit as st
from st_pages import show_pages_from_config
from streamlit_extras.switch_page_button import switch_page

show_pages_from_config()

st.title("Home")

if st.button("move to page1"):
    switch_page("New Page")
