import kagglehub
import pandas as pd
import numpy as np
from models.preprocessing import DataPreprocessor
from models.train_models import ModelTrainer
import os

# Download latest version
print("Downloading dataset from Kaggle...")
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
print("Path to dataset files:", path)

# Load the dataset
csv_path = os.path.join(path, 'creditcard.csv')
df = pd.read_csv(csv_path)

print("\nDataset shape:", df.shape)
print("\nDataset columns:", df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

print("\nClass distribution:")
print(df['Class'].value_counts())

# Since the Kaggle dataset has different structure, we need to adapt it
# The Kaggle dataset has V1-V28 features (PCA transformed), Time, Amount, and Class
# We'll map this to our expected structure

# Create a mapping to our expected features
# For demonstration, we'll create synthetic categorical features based on the numerical ones

def create_synthetic_features(df):
    """Create synthetic categorical features to match our model's expected input"""
    df_new = df.copy()
    
    # Create income type based on amount ranges
    df_new['IncomeType'] = pd.cut(df_new['Amount'], 
                                  bins=[-1, 100, 500, 1000, 5000, float('inf')],
                                  labels=['Student', 'Working', 'Commercial associate', 'State servant', 'Pensioner'])
    
    # Create education type based on transaction patterns (using V features)
    df_new['EducationType'] = pd.cut(df_new['V1'].rank(pct=True),
                                     bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
                                     labels=['Lower secondary', 'Secondary', 'Incomplete higher', 'Higher education', 'Academic degree'])
    
    # Create family status
    df_new['FamilyStatus'] = np.random.choice(['Married', 'Single', 'Civil marriage', 'Separated', 'Widow'], 
                                               size=len(df_new), p=[0.5, 0.2, 0.15, 0.1, 0.05])
    
    # Create housing type
    df_new['HousingType'] = np.random.choice(['House', 'Apartment', 'With parents', 'Municipal apartment', 'Rented apartment'],
                                             size=len(df_new), p=[0.4, 0.3, 0.15, 0.1, 0.05])
    
    # Create employment status
    df_new['EmploymentStatus'] = np.random.choice(['Employed', 'Unemployed', 'Retired', 'Self-employed'],
                                                   size=len(df_new), p=[0.7, 0.1, 0.1, 0.1])
    
    # Create days employed (synthetic)
    df_new['DaysEmployed'] = np.random.randint(0, 18250, size=len(df_new))
    
    # Create months balance
    df_new['MonthsBalance'] = np.random.randint(0, 60, size=len(df_new))
    
    # Create payment status (inverse of Class - fraud transactions have worse payment status)
    df_new['PaymentStatus'] = np.where(df_new['Class'] == 1, 
                                      np.random.randint(2, 6, size=len(df_new)),
                                      np.random.randint(0, 2, size=len(df_new)))
    
    # Create overdue status
    df_new['OverdueStatus'] = np.where(df_new['Class'] == 1,
                                      np.random.randint(1, 6, size=len(df_new)),
                                      np.random.randint(0, 2, size=len(df_new)))
    
    # Create approval status (inverse of Class - fraud = Rejected)
    df_new['ApprovalStatus'] = np.where(df_new['Class'] == 0, 'Approved', 'Rejected')
    
    return df_new

print("\nCreating synthetic features to match model structure...")
df_processed = create_synthetic_features(df)

print("\nProcessed dataset shape:", df_processed.shape)
print("\nNew columns:", df_processed.columns.tolist())

# Select only the columns our model expects
feature_columns = ['IncomeType', 'EducationType', 'FamilyStatus', 'HousingType',
                   'EmploymentStatus', 'DaysEmployed', 'MonthsBalance',
                   'PaymentStatus', 'OverdueStatus', 'ApprovalStatus']

df_final = df_processed[feature_columns].copy()

print("\nFinal dataset shape:", df_final.shape)
print("\nApproval status distribution:")
print(df_final['ApprovalStatus'].value_counts())

# Initialize trainer and preprocessor
print("\nInitializing model trainer...")
trainer = ModelTrainer()

# Preprocess data
print("Preprocessing data...")
df_final = trainer.preprocessor.clean_data(df_final)
df_final = trainer.preprocessor.feature_engineering(df_final)
df_final = trainer.preprocessor.encode_categorical_features(df_final, fit=True)

X = trainer.preprocessor.prepare_features(df_final, fit=True)
y = trainer.preprocessor.prepare_target(df_final)

print(f"\nFeatures shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split data
print("Splitting data...")
X_train, X_test, y_train, y_test = trainer.preprocessor.split_data(X, y)

print(f"Training set size: {X_train.shape}")
print(f"Test set size: {X_test.shape}")

# Train models
print("\nTraining models...")
trainer.train_all_models(X_train, y_train)

# Evaluate models
print("Evaluating models...")
results = trainer.evaluate_models(X_test, y_test)
trainer.print_evaluation_results(results)

# Save best model and preprocessors
print("\nSaving best model and preprocessors...")
trainer.save_best_model()
trainer.preprocessor.save_preprocessors()

print("\n✅ Training completed successfully!")
print(f"Best model: {trainer.best_model_name}")
print(f"Best accuracy: {trainer.best_accuracy:.4f}")
