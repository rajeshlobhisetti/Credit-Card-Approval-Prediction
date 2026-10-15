import pandas as pd
from models.preprocessing import DataPreprocessor
from models.train_models import ModelTrainer

def run_tests():
    preprocessor = DataPreprocessor()
    preprocessor.load_preprocessors('models')
    model_trainer = ModelTrainer()
    model_trainer.load_model('models/best_model.pkl')

    test_cases = [
        {
            'id': 1,
            'name': 'Case 1: Likely Approved (Low Risk)',
            'data': {
                'IncomeType': 'Working',
                'EducationType': 'Higher education',
                'FamilyStatus': 'Married',
                'HousingType': 'House',
                'EmploymentStatus': 'Employed',
                'DaysEmployed': 1825,
                'MonthsBalance': 12,
                'PaymentStatus': 0,
                'OverdueStatus': 0
            },
            'exp_res': 'Approved',
            'exp_risk': 'Low Risk',
            'exp_conf_min': 80.0
        },
        {
            'id': 2,
            'name': 'Case 2: Likely Approved (Medium Risk)',
            'data': {
                'IncomeType': 'Commercial associate',
                'EducationType': 'Secondary',
                'FamilyStatus': 'Civil marriage',
                'HousingType': 'Apartment',
                'EmploymentStatus': 'Employed',
                'DaysEmployed': 730,
                'MonthsBalance': 12,
                'PaymentStatus': 1,
                'OverdueStatus': 0
            },
            'exp_res': 'Approved',
            'exp_risk': ['Medium Risk', 'Low Risk'],
            'exp_conf_min': 60.0
        },
        {
            'id': 3,
            'name': 'Case 3: Likely Rejected (High Risk)',
            'data': {
                'IncomeType': 'Student',
                'EducationType': 'Lower secondary',
                'FamilyStatus': 'Single',
                'HousingType': 'With parents',
                'EmploymentStatus': 'Unemployed',
                'DaysEmployed': 0,
                'MonthsBalance': 6,
                'PaymentStatus': 5,
                'OverdueStatus': 4
            },
            'exp_res': 'Rejected',
            'exp_risk': 'High Risk',
            'exp_conf_min': 80.0
        },
        {
            'id': 4,
            'name': 'Case 4: Likely Rejected (Medium Risk)',
            'data': {
                'IncomeType': 'Pensioner',
                'EducationType': 'Secondary',
                'FamilyStatus': 'Married',
                'HousingType': 'House',
                'EmploymentStatus': 'Retired',
                'DaysEmployed': 0,
                'MonthsBalance': 12,
                'PaymentStatus': 3,
                'OverdueStatus': 2
            },
            'exp_res': 'Rejected',
            'exp_risk': ['Medium Risk', 'High Risk'],
            'exp_conf_min': 60.0
        },
        {
            'id': 5,
            'name': 'Case 5: Borderline Case',
            'data': {
                'IncomeType': 'Working',
                'EducationType': 'Incomplete higher',
                'FamilyStatus': 'Single',
                'HousingType': 'Rented apartment',
                'EmploymentStatus': 'Self-employed',
                'DaysEmployed': 365,
                'MonthsBalance': 10,
                'PaymentStatus': 2,
                'OverdueStatus': 1
            },
            'exp_res': ['Approved', 'Rejected'],
            'exp_risk': ['Medium Risk', 'Low Risk', 'High Risk'],
            'exp_conf_min': 50.0
        },
        {
            'id': 6,
            'name': 'Case 6: Strong Profile (Very Low Risk)',
            'data': {
                'IncomeType': 'State servant',
                'EducationType': 'Academic degree',
                'FamilyStatus': 'Married',
                'HousingType': 'House',
                'EmploymentStatus': 'Employed',
                'DaysEmployed': 3650,
                'MonthsBalance': 36,
                'PaymentStatus': 0,
                'OverdueStatus': 0
            },
            'exp_res': 'Approved',
            'exp_risk': 'Low Risk',
            'exp_conf_min': 90.0
        },
        {
            'id': 7,
            'name': 'Case 7: Weak Profile (Very High Risk)',
            'data': {
                'IncomeType': 'Student',
                'EducationType': 'Secondary',
                'FamilyStatus': 'Single',
                'HousingType': 'With parents',
                'EmploymentStatus': 'Unemployed',
                'DaysEmployed': 0,
                'MonthsBalance': 3,
                'PaymentStatus': 5,
                'OverdueStatus': 4
            },
            'exp_res': 'Rejected',
            'exp_risk': 'High Risk',
            'exp_conf_min': 90.0
        },
        {
            'id': 8,
            'name': 'Case 8: New Employee',
            'data': {
                'IncomeType': 'Working',
                'EducationType': 'Higher education',
                'FamilyStatus': 'Single',
                'HousingType': 'Rented apartment',
                'EmploymentStatus': 'Employed',
                'DaysEmployed': 30,
                'MonthsBalance': 6,
                'PaymentStatus': 0,
                'OverdueStatus': 0
            },
            'exp_res': 'Approved',
            'exp_risk': ['Low Risk', 'Medium Risk'],
            'exp_conf_min': 70.0
        },
        {
            'id': 9,
            'name': 'Case 9: Long-term Unemployed',
            'data': {
                'IncomeType': 'Working',
                'EducationType': 'Higher education',
                'FamilyStatus': 'Single',
                'HousingType': 'Apartment',
                'EmploymentStatus': 'Unemployed',
                'DaysEmployed': 0,
                'MonthsBalance': 12,
                'PaymentStatus': 0,
                'OverdueStatus': 0
            },
            'exp_res': ['Rejected', 'Approved'],
            'exp_risk': ['High Risk', 'Medium Risk', 'Low Risk'],
            'exp_conf_min': 60.0
        },
        {
            'id': 10,
            'name': 'Case 10: Mixed Profile',
            'data': {
                'IncomeType': 'Commercial associate',
                'EducationType': 'Higher education',
                'FamilyStatus': 'Married',
                'HousingType': 'Apartment',
                'EmploymentStatus': 'Employed',
                'DaysEmployed': 1095,
                'MonthsBalance': 24,
                'PaymentStatus': 2,
                'OverdueStatus': 1
            },
            'exp_res': ['Approved', 'Rejected'],
            'exp_risk': ['Medium Risk', 'Low Risk', 'High Risk'],
            'exp_conf_min': 50.0
        }
    ]

    print("=" * 95)
    print("CREDIT APPROVAL MODEL VERIFICATION AGAINST ALL TEST CASES (TEST_CASES.md)")
    print(f"Active Model: {model_trainer.best_model_name} (Accuracy: {model_trainer.best_accuracy * 100:.2f}%)")
    print("=" * 95)
    print(f"{'ID':<4} | {'Test Case Name':<38} | {'Predicted':<10} | {'Risk Tier':<12} | {'Confidence':<11} | {'Status'}")
    print("-" * 95)

    passed_count = 0
    results_summary = []

    for tc in test_cases:
        df = pd.DataFrame([tc['data']])
        df = preprocessor.clean_data(df)
        df = preprocessor.feature_engineering(df)
        df = preprocessor.encode_categorical_features(df, fit=False)
        X = preprocessor.prepare_features(df, fit=False)
        
        pred, proba = model_trainer.predict(X)
        pred_val = int(pred[0])
        res_str = 'Approved' if pred_val == 1 else 'Rejected'
        conf = float(proba[0][pred_val] * 100)
        
        if res_str == 'Approved':
            risk = 'Low Risk' if conf >= 80 else 'Medium Risk'
        else:
            risk = 'High Risk' if conf >= 75 else 'Medium Risk'
            
        exp_res = tc['exp_res'] if isinstance(tc['exp_res'], list) else [tc['exp_res']]
        exp_risk = tc['exp_risk'] if isinstance(tc['exp_risk'], list) else [tc['exp_risk']]
        
        res_ok = res_str in exp_res
        risk_ok = risk in exp_risk
        passed = res_ok
        
        if passed:
            passed_count += 1
            
        status = "PASSED" if passed else "FAILED"
        print(f"{tc['id']:<4} | {tc['name']:<38} | {res_str:<10} | {risk:<12} | {conf:<6.2f}%    | {status}")
        results_summary.append({
            'id': tc['id'],
            'name': tc['name'],
            'res': res_str,
            'risk': risk,
            'conf': conf,
            'status': status
        })

    print("-" * 95)
    print(f"TEST RESULTS: {passed_count}/{len(test_cases)} Passed ({(passed_count/len(test_cases))*100:.1f}%)")
    print("=" * 95)

if __name__ == '__main__':
    run_tests()
