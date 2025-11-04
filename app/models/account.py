from migrations.config import db

class Account(db.Model):
    __tablename__ = 'Account'

    AccountID = db.Column(db.Integer, primary_key=True)
    PhoneNumber = db.Column(db.String(10), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Role = db.Column(db.String(20), nullable=False)
    Status = db.Column(db.String(50), nullable=False)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('employee.EmployeeID'), nullable=False)


    def to_dict(self):
        return {
            'AccountID': self.AccountID,
            'PhoneNumber': self.PhoneNumber,
            'Password': self.Password,
            'Role': self.Role,
            'Status': self.Status,
            'EmployeeID': self.EmployeeID
        }