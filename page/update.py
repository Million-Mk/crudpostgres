import streamlit as st

# # importing sys
import sys
sys.path.insert(1, 'controller')

import client as client 

def update():
    update_id = st.number_input(label='Input ID' ,format="%d",step=1 )
    input_fullname  = st.text_input(label='Full Name')
    input_email = st.text_input(label='Email')
    input_age = st.text_input(label='Age') 
    
    if st.button('Update'):
      
        client.update_by_id(input_fullname, input_email,input_age,update_id)
        st.success('Updated successfully!')
    
    