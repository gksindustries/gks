from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Sector(Base):
    __tablename__ = "sectors"
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class SectorField(Base):
    __tablename__ = "sector_fields"
    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer, ForeignKey("sectors.id"))
    field_key = Column(String, nullable=False)
    field_type = Column(String, default="text")
    is_required = Column(Boolean, default=False)

class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer, ForeignKey("sectors.id"))
    shop_name = Column(String, nullable=False)
    owner_phone = Column(String, nullable=False)
    address = Column(Text)
    city = Column(String)
    pincode = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    license_no = Column(String, nullable=True)
    gstin = Column(String, nullable=True)
    status = Column(String, default="verified")
    created_at = Column(DateTime, default=datetime.utcnow)
    items = relationship("Item", back_populates="shop")

class ShopUser(Base):
    __tablename__ = "shop_users"
    id = Column(Integer, primary_key=True)
    shop_id = Column(Integer, ForeignKey("shops.id"))
    phone = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="owner")
    created_at = Column(DateTime, default=datetime.utcnow)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer, ForeignKey("sectors.id"))
    shop_id = Column(Integer, ForeignKey("shops.id"))
    name = Column(String, nullable=False)
    category = Column(String)
    description = Column(Text)
    price_min = Column(Float)
    price_max = Column(Float)
    image_urls = Column(JSON, default=list)
    attributes = Column(JSON, default=dict)
    is_active = Column(Boolean, default=True)
    in_stock = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    shop = relationship("Shop", back_populates="items")

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=True)
    shop_id = Column(Integer, ForeignKey("shops.id"))
    session_id = Column(String)
    event_type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Referral(Base):
    __tablename__ = "referrals"
    id = Column(Integer, primary_key=True)
    from_shop_id = Column(Integer, ForeignKey("shops.id"), nullable=True)
    to_shop_id = Column(Integer, ForeignKey("shops.id"), nullable=True)
    service_name = Column(String)
    customer_phone = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)