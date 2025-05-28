from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from enum import Enum


class OrderType(str, Enum):
    MACHINERY = "machinery"
    MATERIAL = "material"
    TRUCK_RENTAL = "truck_rental"
    BUNKER_RENTAL = "bunker_rental"
    LABOR = "labor"
    TOOLS = "tools"


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    CANCELLED = "cancelled"


class OrderCreate(BaseModel):
    requested_by_id : UUID
    type : OrderType
    item_id : UUID
    quantity : int = Field(..., gt=0)

class OrderRead(BaseModel):
    id : UUID
    requested_by_id : UUID
    type : OrderType
    item_id : UUID
    quantity : int
    status : OrderStatus
    created_at : datetime

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    id: UUID
    username : str
    department : str
    role: str
    full_name : str
    email : str



class OrderWithUser(BaseModel):
    requested_by: UserInfo
    id : UUID
    order_type: OrderType
    item_id : UUID
    quantity : int
    status : OrderStatus
    created_at : datetime

    class Config:
        orm_mode = True