import streamlit as st
import os
from PIL import Image

# Set up the list of images (adjust the path to your images directory)
image_folder = '/scratch_tmp/prj/cb_normalbreast/prj_BreastAgeNet/thumbnails'

# Ensure image list is filtered correctly
images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Check if image_index is initialized in session state
if 'image_index' not in st.session_state:
    st.session_state['image_index'] = 0

# Add your classifications (checkboxes or dropdown options)
classification_options = ['<35y', '35-45y', '45-55y', '>55y']

# Store the classifications in a dictionary
if 'classifications' not in st.session_state:
    st.session_state['classifications'] = {}

# Set the index to navigate images
image_index = st.session_state['image_index']

# Display the current image
image_path = os.path.join(image_folder, images[image_index])
image = Image.open(image_path)

st.image(image, caption=f"Image {image_index + 1} of {len(images)}", use_column_width=True)

# Display classification options
st.write("Please classify the image:")

# Add selectbox for classification
classification = st.selectbox("Select Classification", classification_options)

# Save classification when the expert selects an option
if st.button('Save Classification'):
    st.session_state['classifications'][images[image_index]] = classification
    st.session_state['image_index'] += 1  # Optionally move to next image after saving

# Navigation buttons to go through images
col1, col2 = st.columns(2)

with col1:
    if st.button('Previous Image') and image_index > 0:
        st.session_state['image_index'] -= 1
    else:
        st.button('Previous Image', disabled=True)

with col2:
    if st.button('Next Image') and image_index < len(images) - 1:
        st.session_state['image_index'] += 1
    else:
        st.button('Next Image', disabled=True)

# Optionally, display the current classifications
if 'classifications' in st.session_state:
    st.sidebar.header("Current Classifications")
    for img, classification in st.session_state['classifications'].items():
        st.sidebar.write(f"{img}: {classification}")
