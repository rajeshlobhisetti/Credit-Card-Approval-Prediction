import os
import shutil
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Handle Vercel serverless environment
if os.environ.get('VERCEL'):
    # In Vercel serverless functions, the root filesystem is read-only.
    # /tmp is the only writable directory.
    tmp_db = '/tmp/credit_approval.db'
    src_db = os.path.join(BASE_DIR, 'credit_approval.db')
    if not os.path.exists(tmp_db) and os.path.exists(src_db):
        try:
            shutil.copy2(src_db, tmp_db)
        except Exception as e:
            print(f"Notice: copying DB to /tmp failed ({e})")
    DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{tmp_db}')
else:
    db_path = os.path.join(BASE_DIR, 'credit_approval.db')
    DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
