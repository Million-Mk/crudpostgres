import streamlit as st

# # importing sys
import sys
sys.path.insert(1, 'controller')

import client as client 

def delete():
    delete_id = st.number_input(label='Input ID' ,format="%d",step=1 )
    if st.button('Delete'):
      
        client.delete_by_id(delete_id)
        st.success('Delete successfully!')
    
    