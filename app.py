import streamlit as st 
from dotenv import load_dotenv
import os
import google.generativeai as genai
# load the environment
load_dotenv()
# Configure the GENAI Key
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))


# Designing the page
st.title("Image to Text Application")
user_input = st.text_input("Input Prompt:")

uploaded_file = st.file_uploader("Uploade the Image....",
                                 type=['jpg','jpeg','png'])

# Display the image on the page
from PIL import Image
img = ""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption="Uploaded The Image",use_column_width=True)

## Function for Evaluating the Image and Annotating it.
def gemini_response(user_input,img):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if user_input!='':
        response = model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text

# Create Submit Button and Map the GENAI function

submit = st.button("Submit")

if submit:
    response = gemini_response(user_input=user_input,img=img)
    st.subheader("The Response is:")
    st.write(response)