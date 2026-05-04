# 🍱 Malaysian Food Classification: Custom CNN vs. ResNet-50

---

## 🚀 Overview
This repository contains a deep learning project aimed at classifying popular Malaysian food items. We explore two different approaches:
1. **Custom CNN**: A deep convolutional neural network built from scratch in PyTorch.
2. **ResNet-50 (Transfer Learning)**: A pre-trained ResNet-50 model fine-tuned for our specific dataset.

The goal is to compare **accuracy, training time, and convergence speed** between a "from-scratch" model and a "pre-trained" state-of-the-art model.

---

## 📂 Dataset
The dataset consists of 5 categories of Malaysian food:
- **Ayam Goreng** (Fried Chicken)
- **Burger**
- **Curry Puff**
- **Laksa**
- **Rice**

### Data Preparation
The raw data is organized in the `data/` folder. We use the `split_dataset.py` script to automatically partition the images into:
- **Train (80%)**
- **Validation (10%)**
- **Test (10%)**

---

## 🏗️ Project Structure
```text
.
├── data/                    # Raw image folders
├── train/                   # Processed training set
├── val/                     # Processed validation set
├── test/                    # Processed test set
├── CustomCNN.ipynb          # Training & Evaluation for Custom CNN
├── ResNet50_TransferLearning.ipynb # Training & Evaluation for ResNet-50
├── split_dataset.py         # Utility script for data organization
└── README.md                # Project documentation
```

---

## 📊 Performance Comparison

| Metric | Custom CNN | ResNet-50 (Transfer Learning) |
| :--- | :--- | :--- |
| **Final Validation Accuracy** | **75.51%** | **96.94%** |
| **Time per Epoch** | **~16.76 seconds** | **~13.19 seconds** |
| **Convergence Epoch** | **~25-30 epochs** | **~2-5 epochs** |
| **Total Parameters** | ~1.5 Million | ~23 Million |

### 💡 Key Observations:
1. **Accuracy**: **ResNet-50** significantly outperformed the Custom CNN. By leveraging weights pre-trained on ImageNet, it was able to identify complex food textures much more effectively.
2. **Training Efficiency**: ResNet-50 was faster per epoch because the backbone was frozen, meaning the model only had to calculate gradients for the final classification layer.
3. **Convergence**: ResNet-50 reached **>90% accuracy in just 2 epochs**, whereas the Custom CNN required nearly 30 epochs to reach its peak.

---

## 🛠️ How to Run
1. **Organize Data**: Run `python split_dataset.py` to prepare your folders.
2. **Train Custom CNN**: Open `CustomCNN.ipynb` and run all cells.
3. **Train ResNet-50**: Open `ResNet50_TransferLearning.ipynb` and run all cells.
4. **Compare Results**: The comparison charts and table are generated at the end of the ResNet notebook.

---

## 📜 License
This project is for educational purposes. 
