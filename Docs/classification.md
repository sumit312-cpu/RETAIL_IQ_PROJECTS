# Product Classification Module

## Objective

The Product Classification module automatically classifies retail product images into predefined categories using Deep Learning and Transfer Learning.

The primary objective is to reduce manual effort in product categorization, improve inventory management, and streamline e-commerce workflows.

---

# Dataset

**Dataset Used:**
Fashion Product Dataset

The dataset consists of thousands of retail product images along with metadata describing each product.

### Categories Used

* Apparel
* Accessories
* Footwear
* Personal Care

Each image belongs to one of the above categories.

---

# Data Preprocessing

The following preprocessing steps were performed before training:

* Removed invalid image records.
* Balanced the dataset across all categories.
* Resized every image to **224 × 224** pixels.
* Converted images into RGB format.
* Applied MobileNetV2 preprocessing.
* Split the dataset into Training, Validation, and Test sets.

---

# Model Used

**Model:** MobileNetV2

**Technique:** Transfer Learning

---

# What is Transfer Learning?

Transfer Learning is a Deep Learning technique where a model that has already been trained on a very large dataset is reused for a new but related task.

Instead of training a CNN from scratch, MobileNetV2 already contains rich feature representations learned from millions of images in the ImageNet dataset.

Only the final classification layers are modified and trained for the retail product classification task.

---

# Why MobileNetV2?

MobileNetV2 was selected because it provides an excellent balance between speed, memory usage, and accuracy.

### Advantages

* Lightweight architecture
* Fast inference
* High classification accuracy
* Suitable for deployment
* Optimized for real-world applications
* Performs well even on CPUs

---

# Why Not Build a CNN From Scratch?

Although a custom CNN can solve the problem, it generally requires:

* More training time
* Larger datasets
* Higher computational resources

Transfer Learning significantly reduces training time while improving accuracy.

---

# Model Architecture

The classification model consists of:

* MobileNetV2 Base Model (Pretrained on ImageNet)
* Global Average Pooling Layer
* Dense Layer
* Dropout Layer
* Softmax Output Layer

The Softmax layer predicts the probability of each product category.

---

# Input

Input Image

Requirements:

* RGB Image
* Resized to **224 × 224**
* Preprocessed using MobileNetV2 preprocessing

Supported image formats:

* JPG
* JPEG
* PNG
* WEBP
* AVIF

---

# Output

The model predicts:

* Product Category
* Confidence Score
* Top-3 Predictions

Example:

Predicted Category: Footwear

Confidence: 98.38%

Top Predictions:

1. Footwear
2. Accessories
3. Apparel

---

# Evaluation

The model achieved approximately **98.38% classification accuracy** on the test dataset.

Evaluation metrics included:

* Accuracy
* Validation Accuracy
* Training Loss
* Validation Loss

---

# Advantages

* High prediction accuracy
* Fast inference
* Lightweight architecture
* Efficient deployment
* Excellent generalization capability

---

# Limitations

* Performance depends on image quality.
* Very blurry or occluded images may reduce prediction accuracy.
* Limited to the categories used during training.

---

# Future Improvements

Possible enhancements include:

* Multi-label classification
* Object Detection using YOLO
* Product Attribute Recognition
* Background Removal
* Automatic Image Captioning using Vision-Language Models
* Image Similarity Search

---

# Frequently Asked Questions

## Why was MobileNetV2 selected?

MobileNetV2 provides high accuracy while remaining lightweight and computationally efficient, making it ideal for deployment.

## What is Transfer Learning?

Transfer Learning reuses knowledge learned from a previously trained model to solve a new task with less data and training time.

## Why resize images to 224 × 224?

MobileNetV2 expects input images of size 224 × 224 pixels.

## What activation function is used in the output layer?

Softmax is used to predict the probability distribution across all product categories.

## What is the output of this module?

The module predicts the product category along with the confidence score and the top three most probable classes.
