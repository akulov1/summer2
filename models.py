from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Float, nullable=False)
    job = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Employee(name='{self.name}', age='{self.age}', job='{self.job}')"

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Currency(name='{self.name}', rate='{self.rate}')"

class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    fromName = db.Column(db.String(250), nullable = False)
    toName = db.Column(db.String(250), nullable = False)

    def __repr__(self):
        return f"Operation(Value: '{self.value}', from: '{self.fromName}', to: {self.toName})"