# Product Recommendation Module

## Objective

The Product Recommendation module provides personalized product suggestions to customers based on their historical purchasing behavior.

The goal is to improve customer experience, increase sales, and enable personalized shopping by recommending products that a customer is likely to purchase.

---

# Dataset

**Dataset Used:**
Online Retail II Dataset

The dataset contains transactional records from an online retail store.

### Important Features

* Invoice
* StockCode
* Description
* Quantity
* InvoiceDate
* Price
* Customer ID
* Country

The dataset represents customer purchase history and is widely used for building recommendation systems.

---

# Data Preprocessing

The following preprocessing steps were performed:

* Removed missing Customer IDs.
* Removed cancelled transactions.
* Removed duplicate records.
* Created a Customer-Product interaction matrix.
* Encoded Customer IDs using LabelEncoder.
* Encoded Product IDs using LabelEncoder.
* Generated user-product interaction pairs for training.

---

# Models Used

Two recommendation approaches were implemented:

## 1. K-Nearest Neighbors (KNN)

KNN was used as a collaborative filtering baseline.

The customer-product interaction matrix was used to calculate similarities between customers using cosine similarity.

Products purchased by similar customers were recommended.

### Advantages

* Easy to understand.
* No training required.
* Effective for small datasets.

### Limitations

* Computationally expensive for large datasets.
* Struggles with sparse data.
* Difficult to scale.

---

## 2. Artificial Neural Network (Neural Collaborative Filtering)

The final recommendation system uses an Artificial Neural Network based on Neural Collaborative Filtering.

Instead of comparing customers directly, the model learns hidden representations (embeddings) of users and products.

These embeddings capture purchasing patterns and customer preferences.

---

# Why ANN Instead of KNN?

The ANN model was selected because:

* Learns complex customer-product relationships.
* Handles sparse datasets more effectively.
* Produces personalized recommendations.
* Faster inference after training.
* More scalable for large retail datasets.
* Captures latent features through embeddings.

---

# Model Architecture

The recommendation model consists of:

* User Embedding Layer
* Product Embedding Layer
* Flatten Layers
* Concatenation Layer
* Dense Hidden Layers
* Output Layer

The model predicts the likelihood that a customer will purchase a specific product.

---

# Recommendation Pipeline

The recommendation process follows these steps:

1. Select a customer.
2. Convert the Customer ID into an encoded value.
3. Generate all possible product IDs.
4. Predict a score for every product using the ANN model.
5. Rank products based on predicted scores.
6. Return the Top-N highest scoring products.

---

# Input

Customer ID

Example:

Customer ID = 17850

---

# Output

Top-N Personalized Product Recommendations

Example:

* WHITE HANGING HEART T-LIGHT HOLDER
* REGENCY CAKESTAND 3 TIER
* JUMBO BAG RED RETROSPOT
* LUNCH BAG RED RETROSPOT

---

# Evaluation

The recommendation model was evaluated using:

* Training Loss
* Validation Loss
* Recommendation Scores

The ANN achieved strong recommendation quality by learning meaningful user and product embeddings.

---

# Advantages

* Personalized recommendations
* Learns customer preferences
* Scalable architecture
* Handles large datasets
* Better performance than traditional collaborative filtering

---

# Limitations

* Cold start problem for new users.
* Requires historical purchase data.
* Performance improves with larger datasets.

---

# Future Improvements

Potential enhancements include:

* Hybrid Recommendation Systems
* Content-Based Filtering
* Transformer-based Recommenders
* Real-Time Recommendations
* Session-Based Recommendation Models

---

# Frequently Asked Questions

## What type of recommendation system is used?

A Neural Collaborative Filtering recommendation system based on an Artificial Neural Network.

## Why are embeddings used?

Embeddings convert users and products into dense numerical vectors that capture hidden purchasing patterns and similarities.

## Why was ANN preferred over KNN?

ANN provides better scalability, learns complex relationships, handles sparse data efficiently, and generates more personalized recommendations.

## What is collaborative filtering?

Collaborative filtering recommends products by learning from the behavior of similar users or similar purchase patterns.

## What is the output of this module?

A ranked list of products that are most likely to be purchased by the selected customer.
