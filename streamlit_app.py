import streamlit as st

st.title("MNIST Digit Classifier")
st.write("Upload an image of a handwritten digit, and I'll predict it!")

uploaded_file = st.file_uploader("Choose a PNG image of a digit", type="png")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded digit", use_column_width=True)
    st.write("Prediction: (simulate here)")
