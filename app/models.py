class Employee:
    def __init__(self, employee_id, name, email, department, role):
        self.id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "role": self.role
        }