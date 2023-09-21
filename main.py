import streamlit as st 

 # importing sys
import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete
import service.connectpostgres as connect

# สร้างเมนูด้านซ้ายมือ 
st.sidebar.title('Menu')

page =st.sidebar.selectbox('    ',['Home', 'Insert','Update', 'Delete'])

if page == 'Home':
    st.title('Home')
    select.select_all()
elif page == 'Insert':
    st.title('Add new Person ')
    insert.insert()
elif page == 'Update':
    st.title('Update Person ')
    update.update()
elif page == 'Delete':
    st.title('Delete Person ')
    delete.delete()