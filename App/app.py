import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)



import os
import streamlit as st
import pandas as pd
import joblib

from tensorflow.keras.models import load_model

# -----------------------------
# Import UI Modules
# -----------------------------

from utils.forecasting_ui import forecasting_page
from utils.recommendation_ui import recommendation_page
from utils.classification_ui import classification_page
from utils.assistant_ui import assistant_page


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="RetailIQ",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)


# ==========================================================
# LOAD MODELS
# ==========================================================

@st.cache_resource
def load_models():

    xgb_model = joblib.load(
        os.path.join(
            MODEL_DIR,
            "xgboost_sales_forecaster.pkl"
        )
    )

    ann_model = load_model(
        os.path.join(
            MODEL_DIR,
            "ann_recommender.h5"
        ),
        compile=False
    )

    classification_model = load_model(
        os.path.join(
            MODEL_DIR,
            "mobilenetv2_classifier.keras"
        ),
        compile=False
    )

    return (
        xgb_model,
        ann_model,
        classification_model
    )


# ==========================================================
# LOAD ENCODERS & LOOKUP TABLES
# ==========================================================

@st.cache_resource
def load_resources():

    user_encoder = joblib.load(
        os.path.join(
            MODEL_DIR,
            "user_encoder.pkl"
        )
    )

    product_encoder = joblib.load(
        os.path.join(
            MODEL_DIR,
            "product_encoder.pkl"
        )
    )

    label_encoder = joblib.load(
        os.path.join(
            MODEL_DIR,
            "cnn_label_encoder.pkl"
        )
    )

    product_lookup = pd.read_csv(
        os.path.join(
            MODEL_DIR,
            "product_lookup.csv"
        )
    )

    return (
        user_encoder,
        product_encoder,
        label_encoder,
        product_lookup
    )


# ==========================================================
# LOAD EVERYTHING
# ==========================================================

with st.spinner("Loading AI Models..."):

    (
        xgb_model,
        ann_model,
        classification_model
    ) = load_models()

    (
        user_encoder,
        product_encoder,
        label_encoder,
        product_lookup
    ) = load_resources()


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🛒 RetailIQ")

    st.markdown("---")

    st.markdown(
        """
### AI Powered Retail Intelligence Platform
"""
    )

    st.success("Modules Included")

    st.markdown("""
✅ Sales Forecasting

✅ Product Recommendation

✅ Product Classification

✅ AI Project Assistant
""")

    st.markdown("---")

    st.info(
        """
This project demonstrates an
end-to-end AI Retail Platform
using Machine Learning,
Deep Learning and
Generative AI.
"""
    )

    st.markdown("---")

    st.subheader("Tech Stack")

    st.markdown("""
- Python
- Streamlit
- TensorFlow
- XGBoost
- FAISS
- Sentence Transformers
- Gemini 3.5 Flash
- ANN
- MobileNetV2
""")

    st.markdown("---")

    st.caption(
        "Developed for AI Portfolio"
    )


# ==========================================================
# MAIN HEADER
# ==========================================================

st.title("🛒 RetailIQ")

st.markdown(
"""
### AI Powered Retail Intelligence Platform

Predict • Recommend • Classify • Explain
"""
)

st.divider()


# ==========================================================
# HOME PAGE
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

[
    "🏠 Home",
    "📈 Forecasting",
    "🛒 Recommendation",
    "🖼️ Classification",
    "🤖 AI Assistant"
]

)

with tab1:

    st.header("Welcome to RetailIQ")

    st.markdown(
    """
RetailIQ is an end-to-end Artificial Intelligence platform
that demonstrates multiple Machine Learning, Deep Learning,
and Generative AI techniques in a single application.

---

### 🚀 Features

📈 Sales Forecasting

Predict future store sales using XGBoost.

---

🛒 Product Recommendation

Recommend products using Neural Collaborative Filtering.

---

🖼️ Product Classification

Classify retail products using MobileNetV2.

---

🤖 AI Project Assistant

Ask project-related questions using Retrieval Augmented
Generation (RAG) powered by FAISS + Gemini.

---
"""
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Machine Learning")

        st.markdown("""
- XGBoost

- Feature Engineering

- Sales Forecasting

- Recommendation System

- ANN Embeddings
""")

    with col2:

        st.subheader("Deep Learning & GenAI")

        st.markdown("""
- CNN

- MobileNetV2

- Transfer Learning

- FAISS

- Gemini API

- RAG Pipeline
""")

    st.divider()

    st.subheader("Project Workflow")

    st.markdown(
"""
Sales Data
⬇
Forecasting

Customer Purchase History
⬇
Recommendation System

Product Images
⬇
CNN Classification

Project Documents
⬇
FAISS
⬇
Gemini
⬇
AI Assistant
"""
    )

# ==========================================================
# FORECASTING TAB
# ==========================================================

with tab2:

    forecasting_page(
        xgb_model
    )


# ==========================================================
# RECOMMENDATION TAB
# ==========================================================

with tab3:

    recommendation_page(
        ann_model,
        user_encoder,
        product_encoder,
        product_lookup
    )


# ==========================================================
# CLASSIFICATION TAB
# ==========================================================

with tab4:

    classification_page(
        classification_model,
        label_encoder
    )


# ==========================================================
# AI ASSISTANT TAB
# ==========================================================

with tab5:

    assistant_page()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<div style='text-align:center'>

### 🛒 RetailIQ

An End-to-End AI Retail Intelligence Platform

Built using

XGBoost • TensorFlow • MobileNetV2 • ANN • FAISS •
Sentence Transformers • Gemini 3.5 Flash • Streamlit

</div>
""",
unsafe_allow_html=True
)