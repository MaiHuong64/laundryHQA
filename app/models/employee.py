from migrations.config import db

class Employee(db.Model):
    __tablename__ = 'Employee'

    EmployeeID = db.Column(db.Integer, primary_key=True)
    EmployeeCode = db.Column(db.String(20), nullable=False)
    FullName = db.Column(db.String(50), nullable=False)
    Sex = db.Column(db.Char(1), nullable=False)
    PhoneNumber = db.Column(db.String(10), nullable=False)
    Address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Employee id={self.EmployeeID} name={self.FullName}>"