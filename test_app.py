import unittest
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from config.database import SessionLocal
from database.models import User, ApplicantDetail, ApprovalPrediction

class CreditApprovalAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['WTF_CSRF_ENABLED'] = False
        cls.client = cls.app.test_client()

    def test_01_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CreditPulse', response.data)
        print("PASS: Landing page /")

    def test_02_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome Back', response.data)
        print("PASS: Login page /login")

    def test_03_login_and_access_dashboard(self):
        # Login with admin
        response = self.client.post('/login', data={
            'email': 'admin@creditapproval.ai',
            'password': 'Admin@123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)
        print("PASS: Login & redirect to /dashboard")

    def test_04_prediction_flow(self):
        # Login first
        self.client.post('/login', data={
            'email': 'admin@creditapproval.ai',
            'password': 'Admin@123'
        })
        
        # Test Case 1: Low risk applicant
        post_data = {
            'income_type': 'Working',
            'education_type': 'Higher education',
            'family_status': 'Married',
            'housing_type': 'House',
            'employment_status': 'Employed',
            'days_employed': '1825',
            'months_balance': '24',
            'payment_status': '0',
            'overdue_status': '0'
        }
        response = self.client.post('/predict', data=post_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'APPROVED', response.data)
        self.assertIn(b'Low Risk', response.data)
        print("PASS: Prediction submission -> Approved, Low Risk")

    def test_05_prediction_high_risk_flow(self):
        # Login first
        self.client.post('/login', data={
            'email': 'admin@creditapproval.ai',
            'password': 'Admin@123'
        })
        
        # Test Case 3: High risk applicant
        post_data = {
            'income_type': 'Student',
            'education_type': 'Lower secondary',
            'family_status': 'Single',
            'housing_type': 'With parents',
            'employment_status': 'Unemployed',
            'days_employed': '0',
            'months_balance': '6',
            'payment_status': '5',
            'overdue_status': '4'
        }
        response = self.client.post('/predict', data=post_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'DECLINED', response.data)
        self.assertIn(b'High Risk', response.data)
        print("PASS: Prediction submission -> Declined, High Risk")

    def test_06_history_and_export(self):
        self.client.post('/login', data={
            'email': 'admin@creditapproval.ai',
            'password': 'Admin@123'
        })
        
        # View history
        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Underwriting Audit Trail', response.data)
        print("PASS: Audit History /history")

        # Export CSV
        export_resp = self.client.get('/history/export')
        self.assertEqual(export_resp.status_code, 200)
        self.assertEqual(export_resp.mimetype, 'text/csv')
        self.assertIn(b'Prediction ID,Applicant ID', export_resp.data)
        print("PASS: CSV Export /history/export")

    def test_07_model_studio_train_page(self):
        self.client.post('/login', data={
            'email': 'admin@creditapproval.ai',
            'password': 'Admin@123'
        })
        response = self.client.get('/train')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ML Model Training', response.data)
        print("PASS: Model Studio /train")

    def test_08_api_predict(self):
        payload = {
            'IncomeType': 'Working',
            'EducationType': 'Higher education',
            'FamilyStatus': 'Married',
            'HousingType': 'House',
            'EmploymentStatus': 'Employed',
            'DaysEmployed': 1825,
            'MonthsBalance': 12,
            'PaymentStatus': 0,
            'OverdueStatus': 0
        }
        response = self.client.post('/api/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        res_json = json.loads(response.data)
        self.assertEqual(res_json['approval_result'], 'Approved')
        self.assertIn('confidence_score', res_json)
        print(f"PASS: /api/predict -> {res_json['approval_result']} ({res_json['confidence_score']}%)")

if __name__ == '__main__':
    unittest.main()
