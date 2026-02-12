from employee_service.db.api import (
    create_employee,
    get_employee,
    update_employee,
    delete_employee,
    get_all_employees
)

from datetime import date


def run_test():
    print("\n--- Creating Employee ---")
    emp_data = {
        "name": "John Doe",
        "gender": "Male",
        "position": "Software Engineer",
        "salary": 75000,
        "experience": 5,
        "birth_date": date(1995, 5, 17)
    }

    emp = create_employee(emp_data)
    print("Created:", emp.id, emp.name)

    print("\n--- Fetching Employee ---")
    fetched = get_employee(emp.id)
    print("Fetched:", fetched.name, fetched.position)

    print("\n--- Updating Employee ---")
    updated = update_employee(emp.id, {"salary": 80000})
    print("Updated Salary:", updated.salary)

    print("\n--- Fetching All Employees ---")
    all_emp = get_all_employees()
    print("Total Active Employees:", len(all_emp))

    print("\n--- Deleting Employee (Soft Delete) ---")
    delete_employee(emp.id)

    deleted = get_employee(emp.id)
    print("After Delete Fetch:", deleted)  # Should be None

    print("\n--- Test Completed Successfully ---")


if __name__ == "__main__":
    run_test() 
