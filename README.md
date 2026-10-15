# Credit Card Approval Prediction System &mdash; CreditPulse AI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask 3.0](https://img.shields.io/badge/framework-Flask%203.0-green.svg)](https://flask.palletsprojects.com/)
[![Vercel Deployment](https://img.shields.io/badge/deploy-Vercel%20Serverless-black.svg?logo=vercel)](https://vercel.com/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn%20%7C%20XGBoost-orange.svg)](https://scikit-learn.org/)
[![Database SQLite](https://img.shields.io/badge/database-SQLite%20%7C%20SQLAlchemy-lightgrey.svg)](https://www.sqlite.org/)
[![Accuracy 99.5%](https://img.shields.io/badge/model%20accuracy-99.50%25-brightgreen.svg)]()

An end-to-end machine learning-powered credit card approval and risk assessment platform built with Flask, SQLAlchemy, scikit-learn, and XGBoost. Fully configured for **instant Vercel Serverless deployment** and local execution.

---

## 🌟 Key Features

- **Automated Credit Decision Engine**: Evaluates applicant socio-economic, employment, and historical repayment signals in &lt;15ms.
- **Multi-Model Benchmark Suite**: Compares Logistic Regression, Random Forest, and XGBoost classifiers; automatically deploys the champion model:
  - **Logistic Regression**: 96.50% Test Accuracy
  - **Random Forest**: 99.17% Test Accuracy
  - **XGBoost Classifier**: **99.50% Test Accuracy** (*Active Production Model*)
- **Granular Risk Categorization**: Classifies applications into **Low Risk**, **Medium Risk**, and **High Risk** tiers with calibrated confidence scores and underwriting limit recommendations.
- **Full Relational Persistence**: Complete SQLite database (`credit_approval.db`) with SQLAlchemy ORM and automatic `/tmp` fallback for Vercel serverless environments:
  - User accounts and authentication
  - Applicant socio-demographic details
  - Credit repayment histories
  - Registered ML models & benchmark accuracies
  - Auditable prediction decisions
- **Modern FinTech Frontend**:
  - **Executive Dashboard**: Real-time KPI summary cards and 3 live Chart.js visualizations.
  - **Assessment Studio**: 3-section structured form with **1-Click Test Scenarios** (*Low Risk Salaried*, *Medium Risk Associate*, *High Risk Profile*, *Borderline Case*).
  - **Decision Report**: Printable PDF-ready underwriting memo with animated confidence gauge.
  - **Audit Trail & History**: Complete log with real-time filters and direct CSV export.
  - **Model Training Studio**: Interactive model retraining and multi-metric comparison charts.

---

## 📁 Repository Structure

```
├── api/
│   └── index.py                       # Vercel Serverless Function entrypoint
├── app/                               # Flask application factory, blueprints, and routes
│   ├── __init__.py
│   ├── auth.py                        # User authentication routes (login, register, logout)
│   └── routes.py                      # Assessment, dashboard, history, and training routes
├── config/
│   └── database.py                    # Database engine & session configuration (with Vercel /tmp fallback)
├── database/
│   └── models.py                      # SQLAlchemy ORM schemas (Users, Applicants, Predictions)
├── data/
│   └── credit_approval_dataset.csv     # 3,000-sample balanced benchmark dataset
├── models/                            # ML pipeline & serializations
│   ├── preprocessing.py               # Feature engineering and encoding
│   ├── train_models.py                # Model training & cross-validation
│   ├── best_model.pkl                 # Trained champion model artifact
│   ├── scaler.pkl                     # Fitted numerical scaler
│   ├── label_encoders.pkl             # Fitted categorical encoders
│   └── feature_columns.pkl            # Expected feature vector alignment
├── templates/                         # Modern Jinja2 HTML templates
│   ├── base.html                      # Layout with navigation bar & footer
│   ├── index.html                     # Enterprise FinTech landing page
│   ├── predict.html                   # Credit evaluation form with test presets
│   ├── result.html                    # Executive underwriting decision memo
│   ├── dashboard.html                 # Real-time analytics dashboard with Chart.js
│   ├── history.html                   # Audit trail table with filters & CSV export
│   ├── train.html                     # Model Studio for retraining & comparisons
│   ├── login.html                     # Sign-in page with 1-click demo button
│   └── register.html                  # Account creation page
├── app.py                             # Local development entrypoint
├── credit_approval.db                 # SQLite persistent database
├── init_demo_data.py                  # Database seeder script
├── test_app.py                        # Automated test suite (all endpoints)
├── verify_test_cases.py               # Verification script for 10 test scenarios
├── requirements.txt                   # Python package dependencies
├── vercel.json                        # Vercel deployment configuration
└── README.md                          # Repository documentation
```

---

## ☁️ Deploy to Vercel (1-Click Ready)

The repository is pre-configured with `vercel.json`, `api/index.py`, and a fine-tuned `.vercelignore` to stay safely within Vercel's 500 MB serverless function limit:

1. **Import to Vercel**:
   - Go to [vercel.com](https://vercel.com/) and click **"Add New Project"** &rarr; **"Import Git Repository"**.
   - Select `https://github.com/rajeshlobhisetti/Credit-Card-Approval-Prediction`.

2. **Project Settings**:
   - **Framework Preset**: `Other`
   - **Root Directory**: `./` *(leave default root)*
   - **Build & Development Settings**: Leave default (Vercel uses `vercel.json` and `requirements.txt`).

3. **Deploy**:
   - Click **Deploy**. Vercel will build the serverless application and provide your live `.vercel.app` URL!

> [!TIP]
> If your Vercel project ever requires larger builds in the future, you can optionally enable Vercel's Large Functions (up to 5 GB) by adding `VERCEL_SUPPORT_LARGE_FUNCTIONS=1` in your Vercel Project Settings &rarr; Environment Variables.

---

## 💻 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rajeshlobhisetti/Credit-Card-Approval-Prediction.git
cd Credit-Card-Approval-Prediction
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Initialize Demo Data (Optional)
```bash
python init_demo_data.py
```

### 4. Run the Application
```bash
python app.py
```
Open your browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🔑 Default Reviewer Credentials

Sign in directly using:
- **Email**: `admin@creditapproval.ai` *(or `rajeshlobhisetti@gmail.com`)*
- **Password**: `Admin@123`
- *(Or click the **"Fill Demo Admin Credentials"** button on the login screen)*

---

## 🧪 Verification & Automated Testing

Run the full end-to-end test suite:
```bash
python test_app.py
```

Verify the model against all 10 standard test scenarios:
```bash
python verify_test_cases.py
```

---

## 📜 License & Acknowledgments

- Developed by **Rajesh Lobhisetti** for the **SmartBridge / IBM SkillsBuild** Internship Project.
- Built using Flask, SQLAlchemy, scikit-learn, XGBoost, Bootstrap 5.3, and Chart.js.
