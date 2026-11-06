@app.post("/shops/register")
def register_shop(payload: ShopRegister, db: Session = Depends(get_db)):
    # यह कोड चेक करेगा कि अगर डेटाबेस खाली है तो सेक्टर खुद बन जाएं
    if db.query(Sector).count() == 0:
        db.add_all([
            Sector(code="GJS", name="GJS Jewellery"),
            Sector(code="GES", name="GES Electronics"),
            Sector(code="GGS", name="GGS Grocery"),
            Sector(code="GMS", name="GMS Medicine")
        ])
        db.commit()

    # बाकी पुराना कोड वैसा ही रहेगा
    sector = db.query(Sector).filter(Sector.code == payload.sector_code.upper()).first()
    if not sector:
        raise HTTPException(404, "Invalid sector code")
        
    if db.query(ShopUser).filter(ShopUser.phone == payload.owner_phone).first():
        raise HTTPException(400, "Phone already registered")
        
    shop = Shop(
        sector_id=sector.id, 
        shop_name=payload.shop_name, 
        owner_phone=payload.owner_phone, 
        address=payload.address, 
        city=payload.city, 
        pincode=payload.pincode, 
        lat=payload.lat, 
        lng=payload.lng, 
        license_no=payload.license_no, 
        gstin=payload.gstin, 
        status="verified"
    )
    db.add(shop)
    db.flush()
    db.add(ShopUser(shop_id=shop.id, phone=payload.owner_phone, password_hash=hash_password(payload.password), role="owner"))
    db.commit()
    return {"status": "verified", "shop_id": shop.id, "message": "Shop live ho gayi"}