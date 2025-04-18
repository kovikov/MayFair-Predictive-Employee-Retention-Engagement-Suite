# -*- coding: utf-8 -*-
"""MayFair Predictive Employee Retention & Engagement Suite.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gVJGuJE03k0_viM8DRluu8UkcL-2zhtX
"""

import pandas as pd

# Load the uploaded CSV file
file_path ="/content/data2 (1).csv"
df = pd.read_csv(file_path)

# Display basic info and first few rows to understand the structure
df.head()

df.info(),

"""**Nice, we’ve got a rich dataset with 4,365 employee records and 16 well-structured features that cover performance, engagement, and workplace dynamics. Let's make this project shine and impress the team with a creative, professional plan.**

🎯 Project Title:
MayFair Predictive Employee Retention & Engagement Suite (PERES)

🚀 Project Overview
We aim to develop a robust, automated, and scalable machine learning solution that leverages MayFair’s employee data to predict attrition risk, enhance engagement strategies, and provide intelligent HR insights. The solution will integrate MLOps pipelines, a REST API, and interactive dashboards, turning data into action.

🧠 Core Features & Deliverables
🔍 1. Exploratory Data Analysis (EDA)
Correlation heatmaps to identify drivers of attrition.

Trend analysis (e.g. attrition vs. engagement, satisfaction, manager feedback).

Departmental retention scorecards.

Salary tier and promotion impact assessments.

🛠️ 2. Data Preprocessing & Feature Engineering
Categorical encoding (e.g., salary, departments, job roles).

Normalize and scale features.

Create new features: e.g. Overworked flag, TenureBucket, FeedbackGap (Manager Score - Engagement Score).

🤖 3. Machine Learning Modeling
Classification models: Logistic Regression, Random Forest, XGBoost, and Neural Nets.

Model evaluation using Precision, Recall, F1-score, and ROC-AUC.

Feature importance using SHAP values to drive business interpretability.

🌐 4. Deployment as REST API
Expose the final model as an endpoint using FastAPI or Flask.



Accept employee profiles and return real-time attrition risk score and retention tips.

🔁 5. MLOps Integration
Automate:

Data pipeline: daily sync from HR systems.

Retraining schedule: monthly, or based on concept drift detection.

Monitoring: model performance drift and data anomalies.

Tools: MLflow for experiment tracking, Docker, GitHub Actions, AWS/GCP/Azure for hosting.

📊 6. Dashboards & Visualization
Interactive Power BI/Tableau dashboard:

Retention risk heatmaps.

Departmental risk rankings.

Impact of remote work and engagement trends.

Embedded API risk scoring widget for HR managers.

👥 Team Roles & Responsibilities
Role	Responsibility
Data Scientist	EDA, modeling, feature engineering, evaluation.
ML Engineer	REST API, deployment, performance tuning.
MLOps Specialist	CI/CD pipelines, model retraining, monitoring.
BI Developer	Power BI/Tableau dashboards, real-time metric tracking.
QA Analyst	Workflow validation, accuracy checks, pipeline testing.

💡 Bonus Creativity: Engagement Booster Engine
A rules-based system that suggests customized interventions based on:

Drop in satisfaction level

.Low manager feedback

.High absenteeism

.Overwork signals

Example:

“🟠 Warning: EMP05698 is showing signs of burnout. Suggest: wellness day + manager check-in.”
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for visualization
sns.set(style="whitegrid")

# Correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)

plt.title("🔍 Correlation Heatmap of Employee Features", fontsize=16)
plt.tight_layout()

plt.show();

"""📊 Key Takeaways from the Heatmap:
Satisfaction Level has a strong negative correlation with Quit the Company – lower satisfaction = higher attrition.

. Engagement Score and Manager Feedback Score are positively correlated with Satisfaction, hinting at areas for proactive HR intervention.

. Average Monthly Hours and Number of Projects show interesting interactions, possibly pointing to overwork-related attrition.

. Remote Work has a weak correlation with attrition – worth deeper segmentation.

✅ Next Up: Feature Engineering & Preprocessing

Let’s:

. Clean & transform categorical variables.

. Engineer smart new features like:

. Overworked Flag: Based on hours/project thresholds.

. Feedback Gap: Manager Score - Engagement Score.

. Tenure Buckets: Categorize TIME_SPEND_COMPANY.

. Risk Score Proxy: A blend of factors.
"""





# Copy the original DataFrame to avoid changes to the raw data
df_fe = df.copy()

# ---------------------------
# 1. Feature: Overworked Flag
# ---------------------------
# Define thresholds for overwork (e.g., >250 hours/month or >6 projects)
df_fe['OVERWORKED'] = np.where((df_fe['AVERAGE_MONTLY_HOURS'] > 250) | (df_fe['NUMBER_PROJECT'] > 6), 1, 0)

# ------------------------------------
# 2. Feature: Feedback Gap (Manager - Engagement)
# ------------------------------------
df_fe['FEEDBACK_GAP'] = df_fe['MANAGER_FEEDBACK_SCORE'] - df_fe['ENGAGEMENT_SCORE']

# ------------------------------------
# 3. Feature: Tenure Bucket
# ------------------------------------
df_fe['TENURE_BUCKET'] = pd.cut(df_fe['TIME_SPEND_COMPANY'],
                                 bins=[0, 2, 5, 10, np.inf],
                                 labels=["<2 Years", "2-5 Years", "5-10 Years", "10+ Years"])

# ------------------------------------
# 4. Categorical Encoding
# ------------------------------------
# One-hot encode categorical variables: DEPARTMENTS, SALARY, JOB_ROLE, TENURE_BUCKET
categorical_cols = ['DEPARTMENTS', 'SALARY', 'JOB_ROLE', 'TENURE_BUCKET']
df_fe_encoded = pd.get_dummies(df_fe, columns=categorical_cols, drop_first=True)

# Display the engineered feature columns
from IPython.display import display # Import the display function
display(df_fe_encoded) # Use display to show the dataframe

# Print the names of the engineered feature columns
engineered_features = ['OVERWORKED', 'FEEDBACK_GAP'] + [col for col in df_fe_encoded.columns if col.startswith(('DEPARTMENTS_', 'SALARY_', 'JOB_ROLE_', 'TENURE_BUCKET_'))]
print("Engineered Features:", engineered_features)

"""Boom 💥 — Feature engineering done!

✨ Newly Engineered Features:
OVERWORKED: Flags employees who may be overloaded with work (e.g., >250 hours/month or >6 projects).

FEEDBACK_GAP: Difference between manager feedback and self-engagement – helps spot disconnects.

TENURE_BUCKET: Groups employees by time spent in the company: <2, 2–5, 5–10, 10+ years.

Categorical Variables Encoded: All department, salary, job role, and tenure bucket info now converted into machine-readable features.

🧠 Next Step: Model Building
We’ll:

Train classification models to predict QUIT_THE_COMPANY.

Compare metrics (Accuracy, Precision, Recall, F1-score, AUC).

Pick the top model for deployment.
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay

# Drop non-numeric ID column for modeling
df_model = df_fe_encoded.drop(columns=["EMPLOYEE_ID"])

# Define features (X) and target (y)
X = df_model.drop(columns=["QUIT_THE_COMPANY"])
y = df_model["QUIT_THE_COMPANY"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=150, random_state=42)
rf_model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = rf_model.predict(X_test)
y_proba = rf_model.predict_proba(X_test)[:, 1]

# Generate performance report
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

# Display results
report, conf_matrix, roc_auc

"""🎉 Model training complete — and the results are 🔥 impressive!

✅ Random Forest Model Performance:
Accuracy: 97.5%

. ROC AUC Score: 0.99 → Excellent discrimination between those who quit vs. stayed.

. Precision & Recall:

. Stayed (0):

. Precision: 0.97

. Recall: 0.997

. Quit (1):

. Precision: 0.99

. Recall: 0.903

📌 Interpretation: The model performs well in identifying at-risk employees while minimizing false positives. Slight under-recall on the "quit" class may improve with fine-tuning or ensemble blending..

🧠 Next Phase:
Feature Importance Plot: See what’s driving attrition.

. Model Export: Save as .pkl for API use.

. Deployment Prep: REST API + scoring function.
"""

# Get feature importances from the model
importances = rf_model.feature_importances_
features = X.columns

# Create a DataFrame for sorting and plotting
feature_importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False).head(20)  # Top 20 features

# Plot
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title("🎯 Top 20 Most Influential Features for Employee Attrition", fontsize=16)
plt.xlabel("Feature Importance Score")
plt.ylabel("Features")
plt.tight_layout()
plt.show()

"""💡 Key Insights:
Satisfaction Level is by far the strongest predictor of whether someone quits.

. Engagement Score and Manager Feedback Score rank highly — HR goldmines!

. Feedback Gap and Overworked are highly impactful engineered features 🔧 — awesome job creating them!

Work accident, remote work status, and specific job roles also influence attrition risk.

Next step: let's package this model into a REST API for real-time predictions
"""

import joblib
import os # Import the os module

# Create the directory if it doesn't exist
os.makedirs("/mnt/data/", exist_ok=True)

# Save the trained model and features list to files
model_path = "/mnt/data/employee_attrition_model.pkl"
features_path = "/mnt/data/employee_attrition_features.pkl"

# Save the model and feature columns
joblib.dump(rf_model, model_path)
joblib.dump(list(X.columns), features_path)

model_path, features_path

"""✅ Your model is now saved and ready for deployment!

Model File: employee_attrition_model.pkl

Feature Schema: employee_attrition_features.pkl

🚀 Next Step: Build the REST API
I’ll create a simple and elegant FastAPI service that:

Accepts employee data via POST request.

Loads the trained model and features.

Returns:

Predicted attrition risk (0 or 1),

Probability,

HR-friendly risk level (Low, Medium, High).
"""

!pip install fastapi

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# Load model and features using the correct file paths
model = joblib.load("/mnt/data/employee_attrition_model.pkl")
feature_list = joblib.load("/mnt/data/employee_attrition_features.pkl")

# Initialize FastAPI
app = FastAPI(title="MayFair Employee Attrition Predictor")

# Define input schema
class EmployeeProfile(BaseModel):
    data: dict

# Risk level classifier
def risk_level(prob):
    if prob < 0.3:
        return "Low"
    elif prob < 0.7:
        return "Medium"
    else:
        return "High"



# Define prediction route
@app.post("/predict")
def predict_attrition(profile: EmployeeProfile):
    try:
        input_df = pd.DataFrame([profile.data])

        # Align with training features
        for col in feature_list:
            if col not in input_df.columns:
                input_df[col] = 0  # add missing columns with default value
        input_df = input_df[feature_list]  # keep only known columns

        # Prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "Attrition Risk (0=Stay, 1=Leave)": int(prediction),
            "Probability": round(probability, 4),
            "Risk Level": risk_level(probability)
        }

    except Exception as e:
        return {"error": str(e)}

"""✅ Your FastAPI service is ready!

🧪 Sample Usage
You can POST to /predict like this:
"""

{
  "data": {
    "SATISFACTION_LEVEL": 0.45,
    "LAST_EVALUATION": 0.78,
    "NUMBER_PROJECT": 5,
    "AVERAGE_MONTLY_HOURS": 230,
    "TIME_SPEND_COMPANY": 3,
    "WORK_ACCIDENT": 0,
    "PROMOTION_LAST_5YEARS": 0,
    "ABSENTEEISM": 4,
    "MANAGER_FEEDBACK_SCORE": 7.2,
    "REMOTE_WORK": 1,
    "ENGAGEMENT_SCORE": 0.55,
    "OVERWORKED": 1,
    "FEEDBACK_GAP": 1.0,
    "TENURE_BUCKET_2-5 Years": 1,
    "DEPARTMENTS_sales": 1,
    "SALARY_medium": 1,
    "JOB_ROLE_Sales Executive": 1
  }
}

{
  "Attrition Risk (0=Stay, 1=Leave)": 1,
  "Probability": 0.81,
  "Risk Level": "High"
}