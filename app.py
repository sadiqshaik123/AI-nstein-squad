
import streamlit as st, requests
st.title('Supplier Risk Assessment POC')
supplier = st.text_input('Supplier')
if st.button('Analyze'):
    r = requests.post('http://localhost:8000/analyze', json={'supplier': supplier})
    st.json(r.json())
