# Model Selection and Design Decisions

# Overview

RetailIQ integrates multiple Artificial Intelligence models, with each model selected based on the specific problem it solves. Instead of using a single algorithm for every task, the project follows the principle of choosing the most appropriate model for each business objective.

The project includes:

* XGBoost for Sales Forecasting
* Artificial Neural Network (ANN) for Product Recommendation
* MobileNetV2 for Product Classification
* Streamlit for Dashboard Development
* FAISS for Vector Search (RAG)
* Google Gemini for Generative AI

Each technology was selected after considering performance, scalability, deployment, and suitability for the problem.

---

# Why XGBoost for Sales Forecasting?

Sales forecasting is a regression problem involving structured tabular data with numerical and categorical features.

### Why XGBoost?

XGBoost is one of the most effective algorithms for structured datasets because it:

* Handles nonlinear relationships.
* Supports feature interactions automatically.
* Includes built-in regularization to reduce overfitting.
* Handles missing values efficiently.
* Provides fast training and inference.
* Delivers excellent predictive performance on tabular datasets.

### Why Not Linear Regression?

Linear Regression assumes a linear relationship between variables.

Retail sales depend on complex interactions involving promotions, holidays, competition, store type, seasonality, and customer behavior.

These relationships are nonlinear, making Linear Regression less suitable.

### Why Not Decision Trees?

A single Decision Tree tends to overfit the training data and usually has lower predictive performance than ensemble methods.

### Why Not Random Forest?

Random Forest is a strong baseline model, but XGBoost generally offers:

* Better predictive accuracy
* Gradient Boosting optimization
* Regularization
* Faster convergence
* Better handling of complex datasets

For these reasons, XGBoost was selected as the final forecasting model.

---

# Why ANN for Product Recommendation?

Product recommendation involves learning customer preferences rather than simply identifying similar customers.

The project implements a Neural Collaborative Filtering approach using an Artificial Neural Network.

### Why ANN?

The ANN model learns:

* Customer embeddings
* Product embeddings
* Hidden purchasing patterns
* Latent customer preferences

These learned representations allow the model to generate highly personalized recommendations.

### Why Not Only KNN?

KNN was implemented as a baseline collaborative filtering approach.

However, KNN has several limitations:

* Poor scalability
* Computationally expensive for large datasets
* Sensitive to sparse data
* Limited ability to learn complex relationships

ANN overcomes these limitations by learning meaningful representations during training.

---

# Why MobileNetV2 for Product Classification?

Image classification requires a Deep Learning model capable of extracting visual features efficiently.

### Why MobileNetV2?

MobileNetV2 offers:

* High classification accuracy
* Lightweight architecture
* Fast inference
* Low memory usage
* Efficient deployment on CPUs and edge devices

It is particularly suitable for production environments where both speed and accuracy are important.

---

# Why Transfer Learning?

Training a Convolutional Neural Network from scratch requires:

* Very large datasets
* Significant computational resources
* Long training times

Instead, Transfer Learning reuses knowledge learned from the ImageNet dataset.

Advantages include:

* Faster convergence
* Higher accuracy
* Reduced training time
* Better performance on limited datasets

This made MobileNetV2 with Transfer Learning the ideal choice for the classification module.

---

# Why Streamlit?

The project uses Streamlit to build an interactive web application.

### Advantages

* Rapid development
* Python-based
* Easy integration with Machine Learning models
* Interactive user interface
* Fast deployment
* Suitable for AI demonstrations and prototypes

---

# Why FAISS for Retrieval-Augmented Generation (RAG)?

The Project Assistant uses Retrieval-Augmented Generation (RAG) to answer questions about the RetailIQ project.

FAISS was selected because it:

* Performs fast similarity search
* Efficiently stores vector embeddings
* Scales to large document collections
* Integrates seamlessly with LangChain

Instead of relying solely on the LLM's knowledge, FAISS retrieves the most relevant project documents before generating an answer.

---

# Why Google Gemini?

Google Gemini was selected as the Large Language Model because it offers:

* Strong reasoning capabilities
* Fast response generation
* High-quality natural language understanding
* Excellent support for Retrieval-Augmented Generation
* Generous free tier for development and experimentation
* Easy integration with LangChain

Gemini generates answers using the retrieved project documents, reducing hallucinations and keeping responses grounded in the RetailIQ knowledge base.

---

# Design Philosophy

RetailIQ follows a modular architecture.

Each module is independent and optimized for its specific task:

* Forecasting uses Machine Learning.
* Recommendation uses Deep Learning.
* Classification uses Computer Vision.
* Project Assistant uses Generative AI with RAG.

This modular design improves maintainability, scalability, and extensibility.

---

# Technology Stack

### Machine Learning

* XGBoost
* Scikit-learn

### Deep Learning

* TensorFlow
* Keras

### Computer Vision

* MobileNetV2
* Pillow

### Recommendation System

* Neural Collaborative Filtering
* Embedding Layers

### Generative AI

* Google Gemini
* LangChain
* FAISS

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

---

# Frequently Asked Questions

## Why are different models used instead of one model for everything?

Different AI problems require different algorithms. A forecasting model cannot perform image classification, and an image classification model cannot generate personalized product recommendations. Each model was selected based on the nature of the task.

## Why was XGBoost preferred over Random Forest?

XGBoost generally provides better predictive accuracy, includes regularization to reduce overfitting, and is highly optimized for structured tabular datasets.

## Why was ANN selected for recommendations?

ANN learns latent customer and product representations through embeddings, allowing it to generate more personalized recommendations than traditional similarity-based methods.

## Why was MobileNetV2 selected instead of building a CNN from scratch?

MobileNetV2 with Transfer Learning provides higher accuracy, faster training, and lower computational cost while requiring less training data.

## Why does the project include RAG?

RAG enables the AI Project Assistant to answer questions using the project's own documentation rather than relying only on the language model's internal knowledge. This improves accuracy, transparency, and reduces hallucinations.

## Can additional AI modules be added?

Yes. The modular architecture allows future integration of demand planning, inventory optimization, anomaly detection, customer segmentation, sentiment analysis, or other AI-powered capabilities without affecting the existing modules.
