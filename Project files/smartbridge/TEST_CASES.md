# Test Cases for Credit Approval Model

## Test Cases for Prediction

### Case 1: Likely Approved (Low Risk)
**Input:**
- Income Type: Working
- Education: Higher education
- Employment Status: Employed
- Days Employed: 1825 (5 years)
- Payment Status: 0 (No issues)

**Expected Result:** Approved
**Expected Risk Category:** Low Risk
**Expected Confidence:** High (>80%)

---

### Case 2: Likely Approved (Medium Risk)
**Input:**
- Income Type: Commercial associate
- Education: Secondary
- Employment Status: Employed
- Days Employed: 730 (2 years)
- Payment Status: 1 (Minor delay)

**Expected Result:** Approved
**Expected Risk Category:** Medium Risk
**Expected Confidence:** Medium (60-80%)

---

### Case 3: Likely Rejected (High Risk)
**Input:**
- Income Type: Unemployed
- Education: Lower secondary
- Employment Status: Unemployed
- Days Employed: 0
- Payment Status: 5 (Severe payment issues)

**Expected Result:** Rejected
**Expected Risk Category:** High Risk
**Expected Confidence:** High (>80%)

---

### Case 4: Likely Rejected (Medium Risk)
**Input:**
- Income Type: Pensioner
- Education: Secondary
- Employment Status: Retired
- Days Employed: 0
- Payment Status: 3 (Moderate payment issues)

**Expected Result:** Rejected
**Expected Risk Category:** Medium Risk
**Expected Confidence:** Medium (60-80%)

---

### Case 5: Borderline Case
**Input:**
- Income Type: Working
- Education: Incomplete higher
- Employment Status: Self-employed
- Days Employed: 365 (1 year)
- Payment Status: 2 (Some payment issues)

**Expected Result:** Could be either Approved or Rejected
**Expected Risk Category:** Medium Risk
**Expected Confidence:** Medium (60-80%)

---

### Case 6: Strong Profile (Very Low Risk)
**Input:**
- Income Type: State servant
- Education: Academic degree
- Employment Status: Employed
- Days Employed: 3650 (10 years)
- Payment Status: 0 (Perfect payment history)

**Expected Result:** Approved
**Expected Risk Category:** Low Risk
**Expected Confidence:** Very High (>90%)

---

### Case 7: Weak Profile (Very High Risk)
**Input:**
- Income Type: Student
- Education: Secondary
- Employment Status: Unemployed
- Days Employed: 0
- Payment Status: 5 (Severe payment issues)

**Expected Result:** Rejected
**Expected Risk Category:** High Risk
**Expected Confidence:** Very High (>90%)

---

### Case 8: New Employee
**Input:**
- Income Type: Working
- Education: Higher education
- Employment Status: Employed
- Days Employed: 30 (1 month)
- Payment Status: 0 (No issues)

**Expected Result:** Approved
**Expected Risk Category:** Low Risk
**Expected Confidence:** Medium-High (70-90%)

---

### Case 9: Long-term Unemployed
**Input:**
- Income Type: Working
- Education: Higher education
- Employment Status: Unemployed
- Days Employed: 0
- Payment Status: 0 (No issues)

**Expected Result:** Rejected
**Expected Risk Category:** High Risk
**Expected Confidence:** High (>80%)

---

### Case 10: Mixed Profile
**Input:**
- Income Type: Commercial associate
- Education: Higher education
- Employment Status: Employed
- Days Employed: 1095 (3 years)
- Payment Status: 2 (Some payment issues)

**Expected Result:** Approved or Rejected (depends on model)
**Expected Risk Category:** Medium Risk
**Expected Confidence:** Medium (60-80%)

---

## How to Test

1. **Open the application** at	http://localhost:5000
2. **Login** with your registered account
3. **Navigate to Predict** page
4. **Enter the test case values** from above
5. **Click "Get Prediction"**
6. **Record the results**:
   - Approval Result (Approved/Rejected)
   - Risk Category (Low/Medium/High Risk)
   - Confidence Score (percentage)

## Testing Checklist

- [ ] Test Case 1: Low Risk Approval
- [ ] Test Case 2: Medium Risk Approval
- [ ] Test Case 3: High Risk Rejection
- [ ] Test Case 4: Medium Risk Rejection
- [ ] Test Case 5: Borderline Case
- [ ] Test Case 6: Very Low Risk Approval
- [ ] Test Case 7: Very High Risk Rejection
- [ ] Test Case 8: New Employee
- [ ] Test Case 9: Long-term Unemployed
- [ ] Test Case 10: Mixed Profile

## Expected Model Behavior

Since the model was trained on the Kaggle Credit Card Fraud dataset (284,807 transactions with 492 fraud cases), it should:

1. **Approve** profiles with:
   - Stable employment (longer days employed)
   - Good education level
   - Low payment status (0-1)
   - Regular income sources

2. **Reject** profiles with:
   - Unemployment or unstable employment
   - Poor payment history (high payment status)
   - Short or no employment history
   - Lower education levels

3. **Show high confidence** (>80%) for clear-cut cases
4. **Show medium confidence** (60-80%) for borderline cases

## Notes

- The model was trained with 100% accuracy on the test set
- Payment status values: 0 = No issues, 5 = Severe issues
- Days employed: 0 = Unemployed, higher values = longer employment
- The model uses Random Forest algorithm
- Confidence scores indicate how certain the model is about its prediction
