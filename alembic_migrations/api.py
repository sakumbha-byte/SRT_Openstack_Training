from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from employee_service.db.models import Employee
import datetime

DATABASE_URL = "mysql+pymysql://root:admin@localhost/employee_data"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False)


def create_employee(data):
    session = Session()
    emp = Employee(**data)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    return emp

def get_all_employees():
    session = Session()
    employees = session.query(Employee).filter_by(deleted=False).all()
    session.close()
    return employees

def get_employee(emp_id):
    session = Session()
    emp = session.query(Employee).filter_by(id=emp_id, deleted=False).first()
    session.close()
    return emp


def update_employee(emp_id, data):
    session = Session()
    emp = session.query(Employee).filter_by(id=emp_id, deleted=False).first()

    if not emp:
        return None

    for key, value in data.items():
        setattr(emp, key, value)

    emp.updated_at = datetime.datetime.utcnow()
    session.commit()
    session.close()
    return emp


def delete_employee(emp_id):
    session = Session()
    emp = session.query(Employee).filter_by(id=emp_id, deleted=False).first()

    if not emp:
        return None

    emp.deleted = True
    emp.deleted_at = datetime.datetime.utcnow()
    session.commit()
    session.close()
    return emp


