from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class SectorOut(BaseModel):
    id: int
    code: str
    name: str
    class Config:
        from_attributes = True

class ShopRegister(BaseModel):
    sector_code: str
    shop_name: str
    owner_phone: str
    password: str
    address: str
    city: str
    pincode: str
    lat: float
    lng: float
    license_no: Optional[str] = None
    gstin: Optional[str] = None

class ShopLogin(BaseModel):
    phone: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ItemCreate(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    price_min: float
    price_max: float
    image_urls: List[str] = []
    attributes: Dict[str, Any] = {}
    in_stock: bool = True

class ItemOut(BaseModel):
    id: int
    name: str
    category: str
    price_min: float
    price_max: float
    image_urls: List[str]
    attributes: Dict[str, Any]
    in_stock: bool
    class Config:
        from_attributes = True

class NearbyItem(BaseModel):
    item_id: int
    name: str
    category: str
    price_min: float
    price_max: float
    attributes: Dict[str, Any]
    shop_id: int
    shop_name: str
    address: str
    city: str
    pincode: str
    phone: str
    distance_km: float
    disclaimer: str = "Availability indicative hai — shop par confirm karein"

class LeadCreate(BaseModel):
    item_id: Optional[int] = None
    shop_id: int
    event_type: str

class ReferralCreate(BaseModel):
    service_name: str
    customer_phone: str
    shop_id: Optional[int] = None