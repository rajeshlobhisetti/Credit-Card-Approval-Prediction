from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)
    Role = Column(Enum('admin', 'analyst', 'user'), default='user')
    
    # Relationships
    applicant_details = relationship("ApplicantDetail", back_populates="user")
    
    # Flask-Login required methods
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.UserID)

class ApplicantDetail(Base):
    __tablename__ = 'applicant_details'
    
    ApplicantID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    IncomeType = Column(String(50))
    EducationType = Column(String(50))
    FamilyStatus = Column(String(50))
    HousingType = Column(String(50))
    EmploymentStatus = Column(String(50))
    DaysEmployed = Column(Integer)
    
    # Relationships
    user = relationship("User", back_populates="applicant_details")
    credit_history = relationship("CreditHistory", back_populates="applicant")
    approval_predictions = relationship("ApprovalPrediction", back_populates="applicant")

class CreditHistory(Base):
    __tablename__ = 'credit_history'
    
    HistoryID = Column(Integer, primary_key=True, autoincrement=True)
    ApplicantID = Column(Integer, ForeignKey('applicant_details.ApplicantID'), nullable=False)
    MonthsBalance = Column(Integer)
    PaymentStatus = Column(String(20))
    OverdueStatus = Column(String(20))
    
    # Relationships
    applicant = relationship("ApplicantDetail", back_populates="credit_history")

class MLModel(Base):
    __tablename__ = 'ml_models'
    
    ModelID = Column(Integer, primary_key=True, autoincrement=True)
    ModelName = Column(String(100), nullable=False)
    AlgorithmType = Column(String(50), nullable=False)
    Accuracy = Column(Float)
    ModelFile = Column(String(255))
    CreatedDate = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    approval_predictions = relationship("ApprovalPrediction", back_populates="model")

class ApprovalPrediction(Base):
    __tablename__ = 'approval_predictions'
    
    PredictionID = Column(Integer, primary_key=True, autoincrement=True)
    ApplicantID = Column(Integer, ForeignKey('applicant_details.ApplicantID'), nullable=False)
    ModelID = Column(Integer, ForeignKey('ml_models.ModelID'), nullable=False)
    ApprovalResult = Column(String(20), nullable=False)  # 'Approved' or 'Rejected'
    RiskCategory = Column(String(20))
    PredictionDate = Column(DateTime, default=datetime.utcnow)
    ConfidenceScore = Column(Float)
    
    # Relationships
    applicant = relationship("ApplicantDetail", back_populates="approval_predictions")
    model = relationship("MLModel", back_populates="approval_predictions")
