import os
import sys
from datetime import datetime, timedelta
import random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.database import init_db, SessionLocal
from database.models import User, ApplicantDetail, CreditHistory, MLModel, ApprovalPrediction
from werkzeug.security import generate_password_hash
import pickle

def seed():
    print("Initializing database schema...")
    init_db()
    db = SessionLocal()
    
    try:
        # 1. Seed or ensure users
        admin_email = 'admin@creditapproval.ai'
        admin_user = db.query(User).filter(User.Email == admin_email).first()
        if not admin_user:
            admin_user = User(
                Name="System Administrator",
                Email=admin_email,
                Password=generate_password_hash("Admin@123", method="pbkdf2:sha256"),
                Role="admin"
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print(f"Created admin user: {admin_email} / Admin@123")
        else:
            print(f"Admin user already exists: {admin_email}")

        # Ensure rajesh user has known password
        rajesh = db.query(User).filter(User.Email == 'rajeshlobhisetti@gmail.com').first()
        if rajesh:
            rajesh.Password = generate_password_hash("Admin@123", method="pbkdf2:sha256")
            db.commit()
            print("Updated rajeshlobhisetti@gmail.com password to Admin@123")

        # 2. Seed ML Model entry
        active_model = db.query(MLModel).first()
        meta = {}
        if os.path.exists('models/model_metadata.pkl'):
            with open('models/model_metadata.pkl', 'rb') as f:
                meta = pickle.load(f)
        
        model_name = meta.get('model_name', 'XGBoost')
        algo_type = meta.get('algorithm_type', 'XGBClassifier')
        acc = float(meta.get('accuracy', 0.995))
        
        if not active_model:
            active_model = MLModel(
                ModelName=model_name,
                AlgorithmType=algo_type,
                Accuracy=acc,
                ModelFile="models/best_model.pkl",
                CreatedDate=datetime.utcnow()
            )
            db.add(active_model)
            db.commit()
            db.refresh(active_model)
            print(f"Registered ML Model in database: {model_name} ({acc:.4f})")
        else:
            active_model.ModelName = model_name
            active_model.AlgorithmType = algo_type
            active_model.Accuracy = acc
            db.commit()
            print(f"Updated ML Model in database: {model_name}")

        # 3. Seed demo predictions if empty
        existing_preds = db.query(ApprovalPrediction).count()
        if existing_preds < 5:
            print("Seeding demo applications & prediction records...")
            demo_cases = [
                {
                    "income_type": "Working",
                    "education_type": "Higher education",
                    "family_status": "Married",
                    "housing_type": "House",
                    "employment_status": "Employed",
                    "days_employed": 2100,
                    "months_balance": 18,
                    "payment_status": "0",
                    "overdue_status": "0",
                    "result": "Approved",
                    "risk": "Low Risk",
                    "confidence": 98.4,
                    "days_ago": 6
                },
                {
                    "income_type": "Commercial associate",
                    "education_type": "Higher education",
                    "family_status": "Single",
                    "housing_type": "Apartment",
                    "employment_status": "Employed",
                    "days_employed": 1460,
                    "months_balance": 24,
                    "payment_status": "0",
                    "overdue_status": "0",
                    "result": "Approved",
                    "risk": "Low Risk",
                    "confidence": 96.2,
                    "days_ago": 5
                },
                {
                    "income_type": "Commercial associate",
                    "education_type": "Secondary",
                    "family_status": "Civil marriage",
                    "housing_type": "Apartment",
                    "employment_status": "Employed",
                    "days_employed": 730,
                    "months_balance": 12,
                    "payment_status": "1",
                    "overdue_status": "0",
                    "result": "Approved",
                    "risk": "Medium Risk",
                    "confidence": 74.5,
                    "days_ago": 4
                },
                {
                    "income_type": "State servant",
                    "education_type": "Academic degree",
                    "family_status": "Married",
                    "housing_type": "House",
                    "employment_status": "Employed",
                    "days_employed": 3650,
                    "months_balance": 36,
                    "payment_status": "0",
                    "overdue_status": "0",
                    "result": "Approved",
                    "risk": "Low Risk",
                    "confidence": 99.1,
                    "days_ago": 3
                },
                {
                    "income_type": "Working",
                    "education_type": "Incomplete higher",
                    "family_status": "Single",
                    "housing_type": "Rented apartment",
                    "employment_status": "Self-employed",
                    "days_employed": 365,
                    "months_balance": 8,
                    "payment_status": "2",
                    "overdue_status": "1",
                    "result": "Rejected",
                    "risk": "Medium Risk",
                    "confidence": 68.3,
                    "days_ago": 2
                },
                {
                    "income_type": "Working",
                    "education_type": "Secondary",
                    "family_status": "Separated",
                    "housing_type": "Municipal apartment",
                    "employment_status": "Unemployed",
                    "days_employed": 0,
                    "months_balance": 6,
                    "payment_status": "4",
                    "overdue_status": "3",
                    "result": "Rejected",
                    "risk": "High Risk",
                    "confidence": 94.7,
                    "days_ago": 1
                },
                {
                    "income_type": "Student",
                    "education_type": "Secondary",
                    "family_status": "Single",
                    "housing_type": "With parents",
                    "employment_status": "Unemployed",
                    "days_employed": 0,
                    "months_balance": 3,
                    "payment_status": "5",
                    "overdue_status": "4",
                    "result": "Rejected",
                    "risk": "High Risk",
                    "confidence": 98.9,
                    "days_ago": 0
                }
            ]

            target_user = admin_user or rajesh

            for case in demo_cases:
                applicant = ApplicantDetail(
                    UserID=target_user.UserID,
                    IncomeType=case["income_type"],
                    EducationType=case["education_type"],
                    FamilyStatus=case["family_status"],
                    HousingType=case["housing_type"],
                    EmploymentStatus=case["employment_status"],
                    DaysEmployed=case["days_employed"]
                )
                db.add(applicant)
                db.flush()

                history = CreditHistory(
                    ApplicantID=applicant.ApplicantID,
                    MonthsBalance=case["months_balance"],
                    PaymentStatus=case["payment_status"],
                    OverdueStatus=case["overdue_status"]
                )
                db.add(history)

                pred_date = datetime.utcnow() - timedelta(days=case["days_ago"], hours=random.randint(1, 10))
                prediction = ApprovalPrediction(
                    ApplicantID=applicant.ApplicantID,
                    ModelID=active_model.ModelID,
                    ApprovalResult=case["result"],
                    RiskCategory=case["risk"],
                    PredictionDate=pred_date,
                    ConfidenceScore=case["confidence"]
                )
                db.add(prediction)

            db.commit()
            print(f"Seeded {len(demo_cases)} demo applicant predictions!")

    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed()
