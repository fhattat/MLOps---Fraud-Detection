---
title: FraudGuard AI
emoji: 🛡️
colorFrom: red
colorTo: gray
sdk: docker
pinned: false
app_port: 7860
---

# 🛡️ FraudGuard: End-to-End Explainable Fraud Detection System

This project is a comprehensive **MLOps** application designed to detect credit card fraud in real-time. It transitions a machine learning model from a research environment to a production-ready, Dockerized microservice.

## 🚀 Project Overview
Fraud detection is a classic "needle in a haystack" problem. This project addresses the **class imbalance** challenge and focuses on **Explainable AI (XAI)** to provide transparent decision-making.

## 🛠️ Tech Stack & MLOps Lifecycle
* **Data Engineering:** High-performance processing with **DuckDB** and **Pandas**.
* **Modeling:** Anomaly detection using **XGBoost** with `scale_pos_weight` optimization.
* **Explainability (XAI):** **SHAP** integration for transparent predictions.
* **Backend:** **FastAPI** and **Pydantic** for real-time inference.
* **Ops & Deployment:** **Docker** on **Hugging Face Spaces**.
* **Monitoring:** Statistical **Drift Analysis** (using KS-Tests) for model reliability.

## 🧪 Test Scenarios
1. **Normal (False):** Amount: 120, hour_of_day: 14, is_night_transaction: 0
2. **Suspicious (True):** Amount: 45000, V1: -55.0, hour_of_day: 3, is_night_transaction: 1

---
**Developed by:** Dr. Fatih Hattatoglu
*Data Science Instructor & AI Engineer*

📂 **Source Code:** [Link to GitHub Repository]
