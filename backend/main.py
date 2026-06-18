from fastapi import FastAPI
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)
from sqlalchemy.orm import declarative_base, sessionmaker
import time

app = FastAPI()

DB_URL = "postgresql://admin:password@postgres-service:5432/employees"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))


# Wait for PostgreSQL and create table
for i in range(20):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connected successfully")
        break
    except Exception as e:
        print(f"Waiting for database... {e}")
        time.sleep(5)


@app.get("/")
def health():
    return {
        "status": "running"
    }


@app.get("/api/employees")
def get_employees():

    db = SessionLocal()

    try:

        employees = db.query(Employee).all()

        result = []

        for emp in employees:
            result.append({
                "id": emp.id,
                "name": emp.name,
                "email": emp.email
            })

        return result

    finally:
        db.close()


@app.post("/api/employee")
def add_employee(name: str, email: str):

    db = SessionLocal()

    try:

        employee = Employee(
            name=name,
            email=email
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return {
            "message": "Employee Added",
            "id": employee.id
        }

    finally:
        db.close()