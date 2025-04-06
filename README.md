# MayFair-Predictive-Employee-Retention-Engagement-Suite

![image](https://github.com/user-attachments/assets/c10bf1c7-93e3-4357-94af-ff4178b1607e)



## 🧠 Empowering HR with Data-Driven Intelligence

In today's hyper-competitive talent market, **employee retention** is more than a metric — it's a mission. At MayFair, we set out to transform raw HR data into a powerful predictive engine, enabling our People team to make *smarter*, *faster*, and *more human-centric* decisions.

This project delivers a full-stack, production-ready **ML-powered Retention Risk Platform** using the best of **Data Science**, **MLOps**, and **API-first architecture**.

---

## 📌 Problem Statement

> “Why are valuable employees leaving—and what can we do about it?”

Understanding attrition patterns requires more than spreadsheets. It needs intelligence. This project builds a system that:
- **Predicts attrition risk** at the employee level
- **Surfaces root causes** like disengagement, overwork, or feedback gaps
- **Equips HR** with tailored, data-backed intervention strategies

---

## 🔍 Solution Overview

### 🎯 Core Features

| Module                         | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 📊 **EDA & Visualization**      | Trend analysis, heatmaps, correlation insights                              |
| 🛠 **Feature Engineering**      | Custom predictors: overwork flag, feedback gap, tenure buckets              |
| 🤖 **ML Model Development**     | Random Forest classifier with 97.5% accuracy and 0.99 AUC                   |
| 🌐 **REST API (FastAPI)**       | Real-time scoring engine with risk level classification                     |
| ⚙️ **MLOps Ready (Docker)**     | Fully containerized with deployment guide for cloud or local setup          |

---

## 🔬 Data Highlights

We analyzed over **4,300 employee records** featuring:
- Satisfaction & Engagement Scores
- Monthly Hours, Projects, Absenteeism
- Manager Feedback
- Promotions, Accidents, Remote Work
- Job Roles, Departments, and Tenure

---

## 🧪 Model Performance

| Metric             | Score   |
|--------------------|---------|
| Accuracy           | 97.5%   |
| ROC AUC            | 0.99    |
| F1 Score (Leave)   | 94.4%   |
| F1 Score (Stay)    | 98.4%   |

> Key Predictors: `Satisfaction Level`, `Engagement Score`, `Manager Feedback`, `Feedback Gap`, `Overwork Flag`

---

## ⚡ How It Works

1. 🧠 An employee profile is submitted via API
2. ⚙️ The model processes it against 30+ engineered features
3. 🎯 The result is a **binary risk prediction**, a **probability score**, and a **risk tier** (Low, Medium, High)
4. 📈 HR can use this insight to trigger interventions

---

## 🚀 Deployment (Dockerized)

### 📁 Project Structure

