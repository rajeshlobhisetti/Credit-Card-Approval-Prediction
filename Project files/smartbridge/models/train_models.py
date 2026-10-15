import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import os
from datetime import datetime
from models.preprocessing import DataPreprocessor

class ModelTrainer:
    def __init__(self):
        self.models = {}
        self.best_model = None
        self.best_model_name = None
        self.best_accuracy = 0
        self.preprocessor = DataPreprocessor()
    
    def train_logistic_regression(self, X_train, y_train):
        """Train Logistic Regression model"""
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train, y_train)
        self.models['Logistic Regression'] = model
        return model
    
    def train_random_forest(self, X_train, y_train):
        """Train Random Forest model"""
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        self.models['Random Forest'] = model
        return model
    
    def train_xgboost(self, X_train, y_train):
        """Train XGBoost model"""
        model = XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss')
        model.fit(X_train, y_train)
        self.models['XGBoost'] = model
        return model
    
    def train_all_models(self, X_train, y_train):
        """Train all models"""
        print("Training Logistic Regression...")
        self.train_logistic_regression(X_train, y_train)
        
        print("Training Random Forest...")
        self.train_random_forest(X_train, y_train)
        
        print("Training XGBoost...")
        self.train_xgboost(X_train, y_train)
        
        print("All models trained successfully!")
    
    def evaluate_model(self, model, X_test, y_test):
        """Evaluate a single model"""
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
    
    def evaluate_models(self, X_test, y_test):
        """Evaluate all models"""
        results = {}
        self.best_accuracy = -1.0
        self.best_model = None
        self.best_model_name = None

        for name, model in self.models.items():
            results[name] = self.evaluate_model(model, X_test, y_test)
        
        # Find best model based on accuracy
        for name, metrics in results.items():
            if metrics['accuracy'] > self.best_accuracy:
                self.best_accuracy = metrics['accuracy']
                self.best_model_name = name
                self.best_model = self.models[name]
        
        return results
    
    def print_evaluation_results(self, results):
        """Print evaluation results"""
        print("\n" + "="*50)
        print("MODEL EVALUATION RESULTS")
        print("="*50)
        for name, metrics in results.items():
            print(f"\n{name}:")
            print(f"  Accuracy:  {metrics['accuracy']:.4f}")
            print(f"  Precision: {metrics['precision']:.4f}")
            print(f"  Recall:    {metrics['recall']:.4f}")
            print(f"  F1-Score:  {metrics['f1_score']:.4f}")
        
        print("\n" + "="*50)
        print(f"BEST MODEL: {self.best_model_name}")
        print(f"ACCURACY: {self.best_accuracy:.4f}")
        print("="*50 + "\n")
    
    def save_best_model(self, model_dir='models'):
        """Save the best model to disk"""
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        
        model_path = os.path.join(model_dir, 'best_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(self.best_model, f)
        
        # Save metadata
        metadata = {
            'model_name': self.best_model_name,
            'accuracy': float(self.best_accuracy),
            'algorithm_type': type(self.best_model).__name__ if self.best_model else 'Ensemble',
            'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        metadata_path = os.path.join(model_dir, 'model_metadata.pkl')
        with open(metadata_path, 'wb') as f:
            pickle.dump(metadata, f)
        
        print(f"Best model saved to {model_path}")
        print(f"Model metadata saved to {metadata_path}")
    
    def load_model(self, model_path):
        """Load a model from disk"""
        with open(model_path, 'rb') as f:
            self.best_model = pickle.load(f)
        
        # Load metadata
        metadata_path = model_path.replace('best_model.pkl', 'model_metadata.pkl')
        if os.path.exists(metadata_path):
            with open(metadata_path, 'rb') as f:
                metadata = pickle.load(f)
            self.best_model_name = metadata['model_name']
            self.best_accuracy = metadata['accuracy']
        
        print(f"Model loaded from {model_path}")
    
    def predict(self, X):
        """Make predictions using the best model"""
        if self.best_model is None:
            raise ValueError("No model loaded. Please train or load a model first.")
        
        prediction = self.best_model.predict(X)
        
        if hasattr(self.best_model, 'predict_proba'):
            probability = self.best_model.predict_proba(X)
        else:
            # For models without predict_proba, create binary probabilities
            probability = np.zeros((len(prediction), 2))
            for i, pred in enumerate(prediction):
                probability[i, int(pred)] = 1.0
        
        return prediction, probability
    
    def predict_proba(self, X):
        """Get prediction probabilities using the best model"""
        if self.best_model is None:
            raise ValueError("No model loaded. Please train or load a model first.")
        
        if hasattr(self.best_model, 'predict_proba'):
            return self.best_model.predict_proba(X)
        else:
            # For models without predict_proba, return binary predictions
            predictions = self.best_model.predict(X)
            proba = np.zeros((len(predictions), 2))
            for i, pred in enumerate(predictions):
                proba[i, int(pred)] = 1.0
            return proba
