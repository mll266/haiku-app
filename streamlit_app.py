import streamlit as st
from google import genai
from PIL import Image
from io import BytesIO

# Configure Google AI Client (store API key securely in Streamlit secrets)
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit UI
st.title("Photo to Haiku")
st.write("Upload an image and receive a beautiful haiku!")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Generate Haiku using Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[image, "You are a poet specializing in Haiku. Create a haiku based on the image. The haiku must have a 5-7-5 syllable structure, be beautiful, and meaningful."]
    )

    # Display the generated Haiku
    st.subheader("Generated Haiku:")
    haiku_lines = response.text.strip().split("\n")
    for line in haiku_lines:
        st.write(line)

