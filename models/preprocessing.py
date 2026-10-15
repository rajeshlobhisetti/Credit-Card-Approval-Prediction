import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle
import os

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_columns = None
        
    def load_data(self, filepath):
        """Load data from CSV file"""
        return pd.read_csv(filepath)
    
    def clean_data(self, df):
        """Handle missing values and clean data"""
        # Fill missing values
        df = df.fillna({
            'IncomeType': df['IncomeType'].mode()[0] if not df['IncomeType'].mode().empty else 'Unknown',
            'EducationType': df['EducationType'].mode()[0] if not df['EducationType'].mode().empty else 'Unknown',
            'FamilyStatus': df['FamilyStatus'].mode()[0] if not df['FamilyStatus'].mode().empty else 'Unknown',
            'HousingType': df['HousingType'].mode()[0] if not df['HousingType'].mode().empty else 'Unknown',
            'EmploymentStatus': df['EmploymentStatus'].mode()[0] if not df['EmploymentStatus'].mode().empty else 'Unknown',
            'DaysEmployed': df['DaysEmployed'].median(),
            'MonthsBalance': df['MonthsBalance'].median(),
            'PaymentStatus': df['PaymentStatus'].mode()[0] if not df['PaymentStatus'].mode().empty else 'Unknown',
            'OverdueStatus': df['OverdueStatus'].mode()[0] if not df['OverdueStatus'].mode().empty else 'Unknown'
        })
        
        # Remove outliers for DaysEmployed (cap at 365*50 = 18250 days)
        df['DaysEmployed'] = df['DaysEmployed'].clip(upper=18250)
        
        return df
    
    def encode_categorical_features(self, df, fit=True):
        """Encode categorical features using Label Encoding"""
        categorical_columns = ['IncomeType', 'EducationType', 'FamilyStatus', 
                              'HousingType', 'EmploymentStatus', 'PaymentStatus', 'OverdueStatus']
        
        for col in categorical_columns:
            if col in df.columns:
                if fit:
                    le = LabelEncoder()
                    df[col] = le.fit_transform(df[col].astype(str))
                    self.label_encoders[col] = le
                else:
                    if col in self.label_encoders:
                        # Handle unseen categories
                        df[col] = df[col].astype(str).apply(
                            lambda x: x if x in self.label_encoders[col].classes_ else 
                            self.label_encoders[col].classes_[0]
                        )
                        df[col] = self.label_encoders[col].transform(df[col])
        
        return df
    
    def feature_engineering(self, df):
        """Create additional features"""
        df = df.copy()
        # Create risk score based on payment history
        if 'PaymentStatus' in df.columns and 'OverdueStatus' in df.columns:
            payment_num = pd.to_numeric(df['PaymentStatus'], errors='coerce').fillna(0)
            overdue_num = pd.to_numeric(df['OverdueStatus'], errors='coerce').fillna(0)
            df['RiskScore'] = payment_num * 0.6 + overdue_num * 0.4
        
        # Employment years
        if 'DaysEmployed' in df.columns:
            days_num = pd.to_numeric(df['DaysEmployed'], errors='coerce').fillna(0)
            df['EmploymentYears'] = days_num / 365
        
        return df
    
    def prepare_features(self, df, fit=True):
        """Prepare features for model training"""
        # Select feature columns
        feature_cols = ['IncomeType', 'EducationType', 'FamilyStatus', 'HousingType',
                       'EmploymentStatus', 'DaysEmployed', 'MonthsBalance', 
                       'PaymentStatus', 'OverdueStatus']
        
        # Add engineered features if they exist
        if 'RiskScore' in df.columns:
            feature_cols.append('RiskScore')
        if 'EmploymentYears' in df.columns:
            feature_cols.append('EmploymentYears')
        
        # Filter to only existing columns
        feature_cols = [col for col in feature_cols if col in df.columns]
        
        if fit:
            self.feature_columns = feature_cols
        
        X = df[feature_cols].copy()
        
        # Scale numerical features
        numerical_cols = ['DaysEmployed', 'MonthsBalance', 'EmploymentYears', 'RiskScore']
        numerical_cols = [col for col in numerical_cols if col in X.columns]
        
        for col in numerical_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce').fillna(0)
        
        if numerical_cols and fit:
            X[numerical_cols] = self.scaler.fit_transform(X[numerical_cols])
        elif numerical_cols:
            X[numerical_cols] = self.scaler.transform(X[numerical_cols])
        
        return X
    
    def prepare_target(self, df, target_column='ApprovalStatus'):
        """Prepare target variable"""
        if target_column in df.columns:
            # Convert to binary (1 for Approved, 0 for Rejected)
            y = df[target_column].apply(lambda x: 1 if x == 'Approved' else 0)
            return y
        return None
    
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """Split data into train and test sets"""
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    def save_preprocessors(self, output_dir='models'):
        """Save fitted preprocessors"""
        os.makedirs(output_dir, exist_ok=True)
        
        with open(os.path.join(output_dir, 'scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f)
        
        with open(os.path.join(output_dir, 'label_encoders.pkl'), 'wb') as f:
            pickle.dump(self.label_encoders, f)
        
        with open(os.path.join(output_dir, 'feature_columns.pkl'), 'wb') as f:
            pickle.dump(self.feature_columns, f)
    
    def load_preprocessors(self, input_dir='models'):
        """Load fitted preprocessors"""
        with open(os.path.join(input_dir, 'scaler.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)
        
        with open(os.path.join(input_dir, 'label_encoders.pkl'), 'rb') as f:
            self.label_encoders = pickle.load(f)
        
        with open(os.path.join(input_dir, 'feature_columns.pkl'), 'rb') as f:
            self.feature_columns = pickle.load(f)
