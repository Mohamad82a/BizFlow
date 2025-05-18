import uuid
from datetime import datetime
from enum import Enum as PyEnum


from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class OrderType(PyEnum):
    MACHINERY = "machinery"
    MATERIAL = "material"
    TRUCK_RENTAL = "truck_rental"
    BUNKER_RENTAL = "bunker_rental"
    LABOR = "labor"
    TOOLS = "tools"


class OrderStatus(PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    CANCELLED = "cancelled"



class Order(base):
    __tablename__ = 'order'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    requested_by_id = Column(UUID(as_uuid=True), nullable=False)
    type = Column(Enum(OrderType), nullable=False)
    item_id = Column(UUID(as_uuid=True), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)