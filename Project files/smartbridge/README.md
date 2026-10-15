# Credit Card Approval Prediction System

This project implements a machine learning-based credit card approval prediction system using Flask and MongoDB.

## Features

- **Machine Learning Models**: Implements Logistic Regression, Random Forest, and XGBoost classifiers
- **Data Preprocessing**: Automated data cleaning, feature engineering, and encoding
- **Web Interface**: User-friendly web UI for making predictions and viewing results
- **Model Training**: Train and evaluate models with custom or sample data
- **API Endpoints**: RESTful API for programmatic access to predictions
- User registration and prediction history retrieval.
- **Risk Assessment**: Automatic risk categorization (Low, Medium, High) based on prediction confidence

## Architecture

1. **User Layer**: Interacts via a web browser.
2. **Presentation Layer**: Web UI components including home page, input form, prediction result display, and history.
3. **Application Layer**: Flask server handling request lifecycle, form validation, data preprocessing, and prediction generation.
4. **Machine Learning Layer**: Trains and evaluates models, selects the best model for deployment.
5. **Data Layer**: Handles data preprocessing and feature engineering.
6. **Deployment Layer**: CI/CD pipeline for deploying the application to IBM Cloud.

1. **User Layer**: Interacts via a web browser.
2. **Presentation Layer**: Web UI components including home page, input form, prediction result display, and history.
3. **Application Layer**: Flask server handling request lifecycle, form validation, data preprocessing, and prediction generation.
4. **Machine Learning Layer**: Trains and evaluates models, selects the best model for deployment.
5. **Data Layer**: Handles data preprocessing and feature engineering.
6. **Deployment Layer**: CI/CD pipeline for deploying the application to IBM Cloud.
2. **ML Layer**: Model training, evaluation, and selection
3. **Application Layer**: Flask web application with REST API
4. **Presentation Layer**: Bootstrap-based web UI
5. **Database Layer**: SQLAlchemy ORM for data persistence

## Project Structure

This project follows a structured format to maintain code organization and clarity.

```
smartbridge/
├── app/
│   ├── __init__.py          # Flask app initialization
│   └── routes.py            # Application routes and API endpoints
├── config/
│   └── database.py          # Database configuration and session management
├── database/
│   └── models.py            # SQLAlchemy ORM models based on ER diagram
├── models/
│   ├── preprocessing.py    # Data preprocessing and feature engineering
│   └── train_models.py      # ML model training and evaluation
├── templates/               # HTML templates
│   ├── base.html           # Base template with navigation
│   ├── index.html          # Home page
│   ├── predict.html        # Prediction form
│   ├── result.html         # Prediction results
│   ├── history.html        # Prediction history
│   ├── dashboard.html      # Dashboard
│   └── train.html          # Model training interface
├── static/                 # Static assets (CSS, JS, images)
├── data/                   # Training data files
├── app.py                  # Application entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd smartbridge
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   The database will be automatically created when you run the application for the first time.

## Usage

### Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   Open your browser and navigate to `http://localhost:5000`

### Training the Model

1. Navigate to the **Train Model** page
2. Upload your training data (CSV format) or use sample data
3. Click **Start Training**
4. View the training results and model performance metrics

### Making Predictions

1. Navigate to the **Predict** page
2. Fill in the applicant details form
3. Click **Get Prediction**
4. View the approval result, risk category, and confidence score

### API Usage

**Make a Prediction**:
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "IncomeType": "Working",
    "EducationType": "Higher education",
    "FamilyStatus": "Married",
    "HousingType": "House",
    "EmploymentStatus": "Employed",
    "DaysEmployed": 1000,
    "MonthsBalance": 12,
    "PaymentStatus": 0,
    "OverdueStatus": 0
  }'
```

**Train Models**:
```bash
curl -X POST http://localhost:5000/api/train \
  -F "data_file=@your_data.csv"
```

## Data Format

### Training Data CSV Format

The training data should include the following columns:

- `IncomeType`: Working, Commercial associate, Pensioner, State servant, Student
- `EducationType`: Secondary, Higher education, Incomplete higher, Lower secondary, Academic degree
- `FamilyStatus`: Married, Single, Civil marriage, Separated, Widow
- `HousingType`: House, Apartment, With parents, Municipal apartment, Rented apartment
- `EmploymentStatus`: Employed, Unemployed, Retired, Self-employed
- `DaysEmployed`: Number of days employed (integer)
- `MonthsBalance`: Months balance (integer)
- `PaymentStatus`: Payment status (0-5)
- `OverdueStatus`: Overdue status (0-5)
- `ApprovalStatus`: Target variable (Approved/Rejected)

## Database Schema

The system uses the following entities based on the ER diagram:

- **Users**: User accounts with authentication
- **Applicant_Details**: Applicant information and demographics
- **Credit_History**: Historical credit data
- **ML_Model**: Machine learning model metadata
- **Approval_Prediction**: Prediction results and history

## Model Performance

The system automatically selects the best model based on accuracy. Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

## Deployment

### IBM Cloud Deployment

The system is designed to be deployed on IBM Cloud with the following services:

1. **IBM Cloud Foundry**: For application hosting
2. **IBM Watson Machine Learning**: For model deployment and serving
3. **IBM Cloud Object Storage**: For storing model artifacts and data

### Deployment Steps

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Deploy to IBM Cloud**:
   - Create an IBM Cloud account
   - Install IBM Cloud CLI
   - Login to IBM Cloud
   - Create a Cloud Foundry organization and space
   - Push the application:
     ```bash
     ibmcloud cf push credit-approval-system
     ```

3. **Configure IBM Watson Machine Learning**:
   - Create a Watson Machine Learning service instance
   - Deploy your trained model
   - Update the application with the deployment credentials

## Development

### Adding New Features

1. **Add new routes**: Edit `app/routes.py`
2. **Add new templates**: Create HTML files in `templates/`
3. **Add new models**: Edit `database/models.py`
4. **Modify ML pipeline**: Edit `models/train_models.py` or `models/preprocessing.py`

### Testing

Run the application in debug mode:
```bash
python app.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is for educational purposes.

## Contact

For questions or support, please open an issue in the repository.

## Acknowledgments

- Built with Flask and SQLAlchemy
- Machine learning models using scikit-learn and XGBoost
- UI components using Bootstrap 5
- Designed for IBM Cloud deployment
