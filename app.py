import streamlit as st
import joblib
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load saved model and vectorizer (if you saved them)
# For Colab live use, use directly defined `lr_model` and `vectorizer` from your notebook

# Cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))
    tokens = word_tokenize(text.lower())
    filtered = [word for word in tokens if word not in stop_words and len(word) > 2]
    return ' '.join(filtered)

# UI Layout
st.title("📰 Fake vs Real News Detector")
st.markdown("Enter the **news content** below, and the model will predict whether it's REAL or FAKE.")

user_input = st.text_area("Enter News Article Text", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text to classify.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = lr_model.predict(vectorized)[0]
        prob = lr_model.predict_proba(vectorized)[0]
        confidence = max(prob)

        st.success(f"Prediction: **{prediction}**  \nConfidence: **{confidence:.2%}**")
