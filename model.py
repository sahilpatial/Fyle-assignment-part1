from app import db


class Bank(db.Model):
    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)
    ifsc = db.Column(db.String())
    bank_id = db.Column(db.Integer())
    address = db.Column(db.String())
    city = db.Column(db.String())
    district = db.Column(db.String())
    state= db.Column(db.String())


    def __init__(self, ifsc, bank_id, address, city, district, state):
        self.ifsc = ifsc
        self.bank_id = bank_id
        self.address = address
        self.city = city
        self.district = district
        self.state = state

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'ifsc': self.ifsc,
            'babk_id': self.bank_id,
            'address': self.address,
            'city': self.city,
            'district': self.district,
            'state': self.state 
        }