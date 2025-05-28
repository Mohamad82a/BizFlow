from sqlalchemy.orm import Session
from uuid import UUID
from . import models, schemas

def create_order(db: Session, order_data: schemas.OrderCreate):
    order = models.Order(**order_data.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_order(db: Session, order_id: UUID):
    return db.query(models.Order).filter(models.Order.id == order_id).first()