from employee_service.api.validation import validate_create, validate_update
from employee_service.db.api import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    delete_employee
)


def create_employee_api(data):
    validate_create(data)
    return create_employee(data)


def get_employee_api(emp_id):
    return get_employee(emp_id)


def get_all_employees_api():
    return get_all_employees()


def update_employee_api(emp_id, data):
    validate_update(data)
    return update_employee(emp_id, data)


def delete_employee_api(emp_id):
    return delete_employee(emp_id)
