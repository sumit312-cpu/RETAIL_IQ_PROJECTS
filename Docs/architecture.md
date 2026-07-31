# architecture.md

# RetailIQ System Architecture

## Overview

RetailIQ is an end-to-end AI-powered retail analytics platform developed using Machine Learning, Deep Learning, Computer Vision, and Generative AI. The application is built using a modular architecture where each AI module performs an independent task while sharing a common Streamlit interface.

---

# Overall Workflow

User Opens Streamlit Dashboard

↓

Selects one of the modules

↓

Forecasting
Recommendation
Classification
Project Assistant

↓

Model Prediction / AI Response

↓

Results displayed on Dashboard

---

# Module Architecture

## 1. Sales Forecasting

User Input

↓

Feature Engineering

↓

XGBoost Model

↓

Predicted Sales

---

## 2. Recommendation System

Customer ID

↓

User Encoding

↓

ANN Recommendation Model

↓

Predicted Scores

↓

Top-N Products

---

## 3. Product Classification

Upload Image

↓

Resize (224×224)

↓

Preprocessing

↓

MobileNetV2

↓

Category + Confidence

---

## 4. Project Assistant (RAG)

User Question

↓

Sentence Embedding

↓

FAISS Vector Search

↓

Relevant Project Documents

↓

Gemini LLM

↓

Final Answer

---

# Folder Structure

RetailIQ/

├── app.py

├── Models/

├── docs/

├── utils/

├── Assets/

├── VectorStore/

├── requirements.txt

└── README.md

---

# Technologies

Frontend

* Streamlit

Machine Learning

* XGBoost
* Scikit-learn

Deep Learning

* TensorFlow
* Keras

Computer Vision

* MobileNetV2

Generative AI

* Gemini
* LangChain
* FAISS

---

# Design Principles

* Modular architecture
* Reusable models
* Easy deployment
* Scalable design
* Maintainable codebase
* Independent AI modules

---

# Future Architecture

The project can be extended with:

* Inventory Prediction
* Customer Segmentation
* Sentiment Analysis
* Sales Report Generation
* Agentic AI
* Multi-Agent Workflows
* Cloud Deployment
* Docker
* CI/CD Pipelines
