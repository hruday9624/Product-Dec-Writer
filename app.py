import streamlit as st
import google.generativeai as genai

# Streamlit app layout
st.title('Personalized Product Description Writer')

# Input fields for the product details
st.subheader("Enter Product Details:")
product_name = st.text_input('Product Name', '')
product_features = st.text_area('Product Features (comma separated)', '')
target_audience = st.text_input('Target Audience', '')

# Footer
#st.sidebar.markdown("---")
st.markdown("Built with 🧠 by Hruday & Ollama")
