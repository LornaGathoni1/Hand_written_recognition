import streamlit as st
import numpy as np
import tensorflow as tf
import cv2
from streamlit_drawable_canvas import st_canvas  # Correct import

# Load the pre-trained model
model = tf.keras.models.load_model('/content/hand_written_digit_recognition_model.keras')

st.title("Handwritten Digit Recognition")

# Create a drawable canvas
st.markdown("## Draw a Digit Below:")
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=15,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Process the image and make a prediction
if canvas_result.image_data is not None:
    # Convert canvas to grayscale and resize
    image = cv2.cvtColor(canvas_result.image_data.astype("uint8"), cv2.COLOR_RGBA2GRAY)
    image = cv2.resize(image, (28, 28))
    image = np.invert(image)
    image = image.reshape(1, 28, 28, 1).astype("float32") / 255.0

    # Predict the digit
    output = model.predict(image)
    st.write(f"Predicted Digit: {np.argmax(output)}")
