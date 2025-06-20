import streamlit as st
import joblib
from url_features import extract_features

# Load the trained model
model = joblib.load("phishing_model.pkl")

# Streamlit app layout
st.set_page_config(page_title="Phishing URL Detector")
st.title("🔐 Phishing URL Detector")
st.markdown("Enter a URL below to check if it's **phishing** or **legitimate**.")

# Input field
url_input = st.text_input("🌐 Enter URL:")

# Predict button
if st.button("🚀 Check URL"):
    if url_input:
        try:
            features_df = extract_features(url_input)
            prediction = model.predict(features_df)[0]

            if prediction == 1:
                st.error("🚨 Warning: This URL is likely a **Phishing Website**.")
            else:
                st.success("✅ Safe: This URL appears to be **Legitimate**.")
        except Exception as e:
            st.exception(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a URL.")
