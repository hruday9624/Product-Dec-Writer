import streamlit as st
import google.generativeai as genai

# Streamlit app layout
st.title('Personalized Product Description Writer')

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input fields for the product details
st.subheader("Enter Product Details:")
product_name = st.text_input('Product Name', '')
product_features = st.text_area('Product Features (comma separated)', '')
target_audience = st.text_input('Target Audience', '')

# Create the prompt based on user inputs
if product_name and product_features and target_audience:
    prompt = f"""
    Analyze the following product details:
    
    1. Generate a catchy product description:
       - Use a tone that resonates with the target audience (e.g., playful for gamers, professional for WFH employees).
       - Include a brief brand story or emotional appeal to connect with potential buyers.
       - Highlight the product's unique selling points (USP) that differentiate it from competitors.
       - Mention specific usage scenarios (e.g., long gaming sessions, remote work).
       - End with a strong call to action (e.g., "Level up your comfort today!").
    
    2. Extract key features from the product features provided:
       - Identify and list the most important and unique features of the product.
       - Explain each feature's benefit to the user.
       - Emphasize how these features contribute to a better user experience.
       - Organize features in a logical order.
       - Include secondary features that add value.

    3. Suggest marketing strategies based on the target audience (Indian market):

    4. Suggest some frequently asked questions FAQs
   

    Product Name: {product_name}
    Product Features: {product_features}
    Target Audience: {target_audience}
    """
if st.button("Generate"):
    # Call to Google Gemini API
    response = genai.generate(prompt)
    if response:
        st.subheader("Generated Product Description:")
        st.write(response)
    else:
        st.write("Error: Unable to generate the description.")


# Add some space or content in between
st.write("\n" * 20)  # You can adjust the number of lines to push the content down

# Footer
#st.sidebar.markdown("---")
st.markdown("Built with 🧠 by Hruday & Google Gemini")
