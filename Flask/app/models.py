from . import db
from werkzeug.security import generate_password_hash

class Account(db.Model):
    __tablename__ = 'account'
    #i kept id just incase we'll need it later on for goals. so if you dont want it feel free to delete it
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def __repr__(self):
        return '<Account %r>' % self.email


class ExpenseList(db.Model):
    __tablename__ = 'expense_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    expense = db.Column(db.Numeric(10, 2))
    tier = db.Column(db.Integer)
    category = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    def __init__(self, name, expense, tier, category, date):
        self.name = name
        self.expense = expense
        self.tier = tier
        self.category = category
        self.date = date

    def __repr__(self):
        return '<ExpenseList %r>' % self.name



class ExpenseCategories(db.Model):
    __tablename__ = 'expense_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ttlCost = db.Column(db.Numeric(10, 2))

    def __init__(self, name, ttlCost):
        self.name = name
        self.ttlCost = ttlCost

    def __repr__(self):
        return '<ExpenseCategories %r>' % self.name

    

class IncomeChannel(db.Model):
    __tablename__ = 'income_channel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    monthlyEarning = db.Column(db.Numeric(10, 2))

    def __init__(self, name, monthlyEarning):
        self.name = name
        self.monthlyEarning = monthlyEarning

    def __repr__(self):
        return '<IncomeChannel %r>' % self.namex
    
