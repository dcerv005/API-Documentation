from models.production import Production
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select

def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(product_id=production_data["product_id"], quantity_produced = production_data["quantity_produced"], date_produced = production_data["date_produced"])
            session.add(new_production)
            session.commit()
        session.refresh(new_production)
        return new_production

def find_all():
    query = select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions