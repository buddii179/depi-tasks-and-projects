import csv


class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email

    def to_dict(self):
        return {
            'ID': self.emp_id,
            'Name': self.name,
            'Position': self.position,
            'Salary': self.salary,
            'Email': self.email
        }

class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee = Employee(
                        emp_id=row['ID'],
                        name=row['Name'],
                        position=row['Position'],
                        salary=row['Salary'],
                        email=row['Email']
                    )
                    self.employees.append(employee)
        except FileNotFoundError:
            open(self.filename, mode='w').close()

    def save_data(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Position', 'Salary', 'Email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for employee in self.employees:
                writer.writerow(employee.to_dict())

    def add_employee(self, emp_id, name, position, salary, email):
        if any(emp.emp_id == emp_id for emp in self.employees):
            print("Error: Employee ID already exists.")
            return
        new_employee = Employee(emp_id, name, position, salary, email)
        self.employees.append(new_employee)
        self.save_data()
        print("Employee added successfully.")

    def update_employee(self, emp_id, name=None, position=None, salary=None, email=None):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.update_details(name, position, salary, email)
                self.save_data()
                print("Employee updated successfully.")
                return
        print("Error: Employee not found.")

    def delete_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                self.save_data()
                print("Employee deleted successfully.")
                return
        print("Error: Employee not found.")

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee found:", employee.to_dict())
                return
        print("Error: Employee not found.")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print("Employee List:")
        for employee in self.employees:
            print(employee.to_dict())


def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")
            manager.add_employee(emp_id, name, position, salary, email)

        elif choice == '2':
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to skip): ")
            position = input("Enter new Position (leave blank to skip): ")
            salary = input("Enter new Salary (leave blank to skip): ")
            email = input("Enter new Email (leave blank to skip): ")
            manager.update_employee(emp_id, name or None, position or None, salary or None, email or None)

        elif choice == '3':
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)

        elif choice == '4':
            emp_id = input("Enter Employee ID to search: ")
            manager.search_employee(emp_id)

        elif choice == '5':
            manager.list_employees()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
