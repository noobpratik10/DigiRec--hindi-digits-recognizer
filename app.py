import streamlit as st
from streamlit_option_menu import option_menu
from recognizer import make_prediction

#Set the configurations
st.set_page_config(
    page_title="DigiRec",
    page_icon="static/img/Logo.png",
)

# Streamlit UI
st.image('static/img/Banner Image.png', use_container_width=True)

# model  menu
st.header('Choose your model!')
model_selected = option_menu(
    menu_title=None,
    options=['ANN', 'CNN'],
    default_index=0,
    menu_icon=None,
    icons=['lightbulb-fill','lightbulb-fill'],
    orientation='horizontal',
)

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image file",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # display the image
    st.subheader('Uploaded Image:')
    st.image(
        uploaded_file,
        caption=None,
        width=400
    )
    # make prediction
    result = make_prediction(uploaded_file, model_selected)
    # display the result
    st.subheader('Result: '+str(result[0]))
