from migrations.config import db

class Department(db.Model):
    __tablename__ = 'Department'

    DepartmentID = db.Column(db.Integer, primary_key=True)
    DepartmentCode = db.Column(db.String(50), nullable=False)
    FullName = db.Column(db.String(255), nullable=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customer.CustomerID'), nullable=False)
    def to_dict(self):
        return {
            'DepartmentID': self.DepartmentID,
            'DepartmentCode': self.DepartmentCode,
            'FullName': self.FullName,
            'CustomerID': self.CustomerID
        }