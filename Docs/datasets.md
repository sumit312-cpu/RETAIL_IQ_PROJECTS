# datasets.md

# Datasets Used in RetailIQ

## 1. Rossmann Store Sales Dataset

Purpose

Sales Forecasting

Target Variable

Sales

Important Features

* Store
* DayOfWeek
* Promo
* Open
* SchoolHoliday
* StoreType
* Assortment
* CompetitionDistance
* CompetitionOpenSinceMonth
* CompetitionOpenSinceYear
* Promo2
* PromoInterval
* Date

Feature Engineering

* Year
* Month
* Day
* Week
* Quarter
* Weekend
* Holiday_Flag

Problem Type

Regression

---

## 2. Online Retail II Dataset

Purpose

Product Recommendation

Important Features

* Invoice
* StockCode
* Description
* Quantity
* Price
* Customer ID
* Country

Problem Type

Recommendation System

Preprocessing

* Removed cancelled orders
* Removed null Customer IDs
* Removed duplicates
* Encoded customers
* Encoded products
* Created interaction matrix

---

## 3. Fashion Product Dataset

Purpose

Product Classification

Categories

* Apparel
* Accessories
* Footwear
* Personal Care

Preprocessing

* RGB conversion
* Resize to 224×224
* Balanced categories
* Train/Validation/Test split

Problem Type

Image Classification

---

# Data Processing Libraries

* Pandas
* NumPy
* Scikit-learn

---

# Why Multiple Datasets?

Each AI problem requires a different type of data.

Sales Forecasting

→ Structured numerical data

Recommendation

→ Customer transaction data

Classification

→ Image data

---

# future_scope.md

# Future Scope

The project can be enhanced by adding:

* Real-time forecasting
* Inventory optimization
* Demand planning
* Customer segmentation
* Dynamic pricing
* Explainable AI
* Sales report summarization
* Marketing campaign generation
* OCR for invoices
* Object Detection using YOLO
* Product Similarity Search
* Voice-enabled AI assistant
* Cloud deployment using AWS/Azure/GCP
* Docker & Kubernetes
* CI/CD automation
* Multi-Agent AI
* Autonomous Retail Assistant

---

# Learning Outcomes

This project demonstrates:

* Machine Learning
* Deep Learning
* Recommendation Systems
* Transfer Learning
* Computer Vision
* Retrieval-Augmented Generation
* Large Language Models
* Streamlit Deployment
* End-to-End AI Engineering
