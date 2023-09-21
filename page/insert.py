import streamlit as st

# # importing sys
import sys
sys.path.insert(1, 'controller')

import client as client 

def insert():
    with st.form(key="insert"):
 
    
        st.write('Insert a new row in the database Please fill in the following fields:')
        input_fullname  = st.text_input(label='Full Name')
        
        input_email = st.text_input(label='Email')
        
        input_age = st.text_input(label='Age')
       

        button_submit = st.form_submit_button(label="Submit")

        if button_submit:
            client.insert(input_fullname, input_email,input_age)
            
            st.success('Inserted successfully!')
            
            # st.experimental_rerun()

        