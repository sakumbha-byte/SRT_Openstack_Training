from employee_service.api.employee_api import (
    create_employee_api,
    get_employee_api,
    get_all_employees_api,
    update_employee_api,
    delete_employee_api
)


def run_test():

    print("\nEmployee Validation Test\n")

    try:
        print("---- Creating Employee ----")

        emp_data = {
            "name": "Sahil Kumbhar",
            "gender": "Male",
            "position": "Software Engineer Intern",
            "salary": 1500,
            "experience": 1,
            "birth_date": "2004-06-21"
        }

        emp = create_employee_api(emp_data)
        print("Created:", emp.id, emp.name)

        print("\n---- Fetching Employee ----")

        fetched = get_employee_api(emp.id)
        print("Fetched:", fetched.name)

        print("\n---- Updating Employee ----")

        updated = update_employee_api(emp.id, {"salary": 80000})
        print("Updated Salary:", updated.salary)

        print("\n---- Fetching All Employees ----")

        all_emp = get_all_employees_api()
        print("Total Active Employees:", len(all_emp))

        print("\n---- Soft Deleting Employee ----")

        delete_employee_api(emp.id)

        deleted = get_employee_api(emp.id)
        print("After Delete Fetch (Should be None):", deleted)

        print("\n---- Invalid Data Test ----")

        try:
            create_employee_api({
                "name": "",
                "gender": "InvalidGender",
                "salary": -1000
            })
        except Exception as e:
            print("Validation Error:", e)

        try:
            create_employee_api({
                "gender": "Male",
                "salary": -500
            })
        except Exception as e:
            print("Name Validation Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    print("\nTest Completed\n")


if __name__ == "__main__":
    run_test()
