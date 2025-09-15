from app.extensions import db


class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True, index=True)
    main_dish = db.Column(db.String(255), nullable=False)
    side_dish = db.Column(db.String(255), nullable=False)
    salad = db.Column(db.String(255), nullable=False)
    dessert = db.Column(db.String(255), nullable=False)
    drink = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Menu id={self.id} date={self.date}>"
