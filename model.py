from api import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relation

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

class Product_abbreviation(db.Model):
    _tablename_='product_abbreviation'
    ID = db.Column(db.Integer, primary_key=True)
    PROD_ABBR = db.Column(db.String(50), unique=True)

class State_abbreviation(db.Model):
    _tablename_='state_abbreviation'
    ID = db.Column(db.Integer, primary_key=True)
    STATE_ABBR = db.Column(db.String(50), unique=True)

class Product(db.Model):
    _tablename_='product'
    AGENCY_ID_PRIMARY=db.Column(db.Integer, primary_key=True)
    AGENCY_ID=db.Column(db.Integer)
    PROD_ABBR_ID=db.Column(db.Integer, ForeignKey('product_abbreviation.ID'))
    PROD_LINE=db.Column(db.String(2))
    STATE_ABBR_ID=db.Column(db.Integer, ForeignKey('state_abbreviation.ID'))
    STAT_PROFILE_DATE_YEAR=db.Column(db.Integer)
    RETENTION_POLY_QTY=db.Column(db.Integer)
    POLY_INFORCE_QTY=db.Column(db.Integer)
    PREV_POLY_INFORCE_QTY=db.Column(db.Integer)
    NB_WRTN_PREM_AMT=db.Column(db.Float)
    WRTN_PREM_AMT=db.Column(db.Float)
    PREV_WRTN_PREM_AMT=db.Column(db.Float)
    PRD_ERND_PREM_AMT=db.Column(db.Float)
    PRD_INCRD_LOSSES_AMT=db.Column(db.Float)
    MONTHS=db.Column(db.Integer)
    RETENTION_RATIO=db.Column(db.Float)
    LOSS_RATIO=db.Column(db.Float)
    LOSS_RATIO_3YR=db.Column(db.Float)
    GROWTH_RATE_3YR=db.Column(db.Float)
    AGENCY_APPOINTMENT_YEAR=db.Column(db.Integer)
    ACTIVE_PRODUCERS=db.Column(db.Integer)
    MAX_AGE=db.Column(db.Integer)
    MIN_AGE=db.Column(db.Integer)
    VENDOR_IND=db.Column(db.String(10))
    VENDOR=db.Column(db.String(10))
    PL_START_YEAR=db.Column(db.Integer)
    PL_END_YEAR=db.Column(db.Integer)
    COMMISIONS_START_YEAR=db.Column(db.Integer)
    COMMISIONS_END_YEAR=db.Column(db.Integer)
    CL_START_YEAR=db.Column(db.Integer)
    CL_END_YEAR=db.Column(db.Integer)
    ACTIVITY_NOTES_START_YEAR=db.Column(db.Integer)
    ACTIVITY_NOTES_END_YEAR=db.Column(db.Integer)
    CL_BOUND_CT_MDS=db.Column(db.Integer)
    CL_QUO_CT_MDS=db.Column(db.Integer)
    CL_BOUND_CT_SBZ=db.Column(db.Integer)
    CL_QUO_CT_SBZ=db.Column(db.Integer)
    CL_BOUND_CT_eQT=db.Column(db.Integer)
    CL_QUO_CT_eQT=db.Column(db.Integer)
    PL_BOUND_CT_ELINKS=db.Column(db.Integer)
    PL_QUO_CT_ELINKS=db.Column(db.Integer)
    PL_BOUND_CT_PLRANK=db.Column(db.Integer)
    PL_QUO_CT_PLRANK=db.Column(db.Integer)
    PL_BOUND_CT_eQTte=db.Column(db.Integer)
    PL_QUO_CT_eQTte=db.Column(db.Integer)
    PL_BOUND_CT_APPLIED=db.Column(db.Integer)
    PL_QUO_CT_APPLIED=db.Column(db.Integer)
    PL_BOUND_CT_TRANSACTNOW=db.Column(db.Integer)
    PL_QUO_CT_TRANSACTNOW=db.Column(db.Integer)

    product_abbrevation = relation(Product_abbreviation)
    state_abbreviation = relation(State_abbreviation)
