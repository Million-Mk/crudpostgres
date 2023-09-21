import streamlit as st

# # importing sys
import sys
sys.path.insert(1, 'controller')

import client as client 

def select_all():
    # st.sidebar.subheader('Select All Person')
    st.title('Select All')
    rows = client.select_all()

    if rows:
        st.table(rows)
    else:
        st.write('No person selected')
