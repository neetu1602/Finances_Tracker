from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.user import User
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Database connected:", result.scalar())

print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
  return {"message":"Finance Tracker API"}

@app.get("/health")
def health():
    return{
       "status": "ok"
    }