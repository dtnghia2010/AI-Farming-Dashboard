from application import app,db
from datetime import datetime
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    water_level = db.Column(db.Integer)
    light = db.Column(db.Integer)
    dust_density = db.Column(db.Float)
    co = db.Column(db.Float)
    co2 = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SensorData {self.temperature}, {self.water_level}, {self.light}, {self.dust_density}, {self.co}, {self.co2}>'

with app.app_context():
    db.create_all()  