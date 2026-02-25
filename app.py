import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.title("SMS Spam Classifier")

text = st.text_input("Enter your message")

if st.button("Predict"):
    data = cv.transform([text])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.write("Spam 🚫")
    else:
        st.write("Not Spam ✅")