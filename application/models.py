from application import app,db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), default='income', nullable=False)
    category = db.Column(db.String(30), nullable=False, default='rent')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)
    __table_args__ = {'extend_existing': True}  

    def __str__(self):
        return self.id


class PlantData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(100), nullable=False)
    plant_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    health = db.Column(db.Float, nullable=False)  # Health score, could be a percentage
    last_checked = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Plant {self.plant_name} - Status: {self.status}>'


with app.app_context():
    db.create_all()