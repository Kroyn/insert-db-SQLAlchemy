from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    
    store_id = db.Column(
        db.Integer, 
        db.ForeignKey("stores.id"), 
        nullable=False
    )
    store = db.relationship("StoreModel", back_populates="items")
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id